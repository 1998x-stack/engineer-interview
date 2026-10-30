"""Independent oracle checks for deep-learning reference implementations."""
import sys
from pathlib import Path

import pytest
import torch
import torch.nn.functional as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from examples.numerics_reference import (
    cross_entropy_logits, adamw_step, batchnorm2d_train,
    batchnorm2d_eval, reference_attention, symmetric_infonce,
)


@pytest.mark.parametrize("batch,classes", [(1, 2), (5, 11), (8, 4)])
def test_cross_entropy_forward_gradient_matches_torch(batch, classes):
    torch.manual_seed(4)
    x = (torch.randn(batch, classes, dtype=torch.float64) * 900).requires_grad_()
    labels = torch.randint(0, classes, (batch,))
    actual = cross_entropy_logits(x, labels)
    oracle = F.cross_entropy(x, labels)
    torch.testing.assert_close(actual, oracle, rtol=1e-12, atol=1e-12)
    torch.testing.assert_close(
        torch.autograd.grad(actual, x, retain_graph=True)[0],
        torch.autograd.grad(oracle, x)[0], rtol=1e-12, atol=1e-12,
    )


def test_cross_entropy_gradient_is_softmax_minus_onehot():
    x = torch.tensor([[5., -2., 3.]], dtype=torch.float64, requires_grad=True)
    expected = torch.softmax(x.detach(), dim=-1) - F.one_hot(torch.tensor([2]), 3)
    grad = torch.autograd.grad(cross_entropy_logits(x, torch.tensor([2])), x)[0]
    torch.testing.assert_close(grad, expected)


@pytest.mark.parametrize("bad_x,bad_y", [
    (torch.ones(2, 3), torch.tensor([0])),
    (torch.ones(2, 3), torch.tensor([0, 3])),
    (torch.tensor([[float("nan"), 0.]]), torch.tensor([0])),
    (torch.ones(2, 3, dtype=torch.int64), torch.tensor([0, 1])),
    (torch.ones(2, 3), torch.tensor([0, 1], dtype=torch.int32)),
])
def test_cross_entropy_rejects_bad_inputs(bad_x, bad_y):
    with pytest.raises(ValueError):
        cross_entropy_logits(bad_x, bad_y)


@pytest.mark.parametrize("batch,channels,height,width", [(2, 3, 4, 5), (1, 2, 2, 3)])
def test_batchnorm_train_forward_and_gradients(batch, channels, height, width):
    torch.manual_seed(17)
    x = torch.randn(batch, channels, height, width, dtype=torch.float64, requires_grad=True)
    gamma = torch.randn(channels, dtype=torch.float64, requires_grad=True)
    beta = torch.randn(channels, dtype=torch.float64, requires_grad=True)
    actual = batchnorm2d_train(x, gamma, beta, eps=1e-5)
    expected = F.batch_norm(x, None, None, gamma, beta, training=True, eps=1e-5)
    torch.testing.assert_close(actual, expected, rtol=1e-10, atol=1e-10)
    gs = torch.autograd.grad(actual.square().sum(), (x, gamma, beta), retain_graph=True)
    gt = torch.autograd.grad(expected.square().sum(), (x, gamma, beta))
    for a, b in zip(gs, gt):
        torch.testing.assert_close(a, b, rtol=1e-9, atol=1e-9)


def test_batchnorm_eval_parity():
    torch.manual_seed(1)
    x = torch.randn(2, 3, 4, 4, dtype=torch.float64)
    gamma = torch.randn(3, dtype=torch.float64)
    beta = torch.randn(3, dtype=torch.float64)
    mean = torch.randn(3, dtype=torch.float64)
    var = torch.rand(3, dtype=torch.float64) + .1
    torch.testing.assert_close(
        batchnorm2d_eval(x, gamma, beta, mean, var),
        F.batch_norm(x, mean, var, gamma, beta, training=False),
        atol=1e-12, rtol=1e-12
    )


def test_batchnorm_one_value_per_channel_rejected():
    with pytest.raises(ValueError, match=">1"):
        batchnorm2d_train(torch.ones(1, 2, 1, 1), torch.ones(2), torch.zeros(2))


def test_batchnorm_invalid_running_stats_rejected():
    with pytest.raises(ValueError):
        batchnorm2d_eval(torch.ones(2, 2, 1, 1), torch.ones(2), torch.zeros(2),
                         torch.zeros(2), torch.tensor([1., -1.]))


@pytest.mark.parametrize("weight_decay", [0., .05])
def test_adamw_matches_torch_across_multiple_steps(weight_decay):
    torch.manual_seed(31)
    initial = torch.tensor([.3, -1.2, 2.3], dtype=torch.float64)
    p = torch.nn.Parameter(initial.detach().clone())
    opt = torch.optim.AdamW([p], lr=.02, betas=(.8, .99), eps=1e-8, weight_decay=weight_decay)
    manual = initial.clone()
    m, v = torch.zeros_like(manual), torch.zeros_like(manual)
    for step in range(1, 5):
        grad = torch.randn_like(manual)
        p.grad = grad.clone()
        opt.step()
        p.grad = None
        manual, m, v = adamw_step(manual, grad, m, v, step=step, lr=.02,
                                  beta1=.8, beta2=.99, weight_decay=weight_decay)
        torch.testing.assert_close(manual, p.detach(), rtol=1e-12, atol=1e-12)


def test_adam_and_adamw_decay_are_distinct():
    initial = torch.nn.Parameter(torch.tensor([.3, 3.], dtype=torch.float64))
    p_adam = torch.nn.Parameter(initial.detach().clone())
    p_w = torch.nn.Parameter(initial.detach().clone())
    a = torch.optim.Adam([p_adam], lr=.01, weight_decay=.1)
    b = torch.optim.AdamW([p_w], lr=.01, weight_decay=.1)
    for _ in range(2):
        for p in (p_adam, p_w):
            p.grad = torch.tensor([.2, 1.], dtype=torch.float64)
        a.step()
        b.step()
    assert not torch.allclose(p_adam, p_w, rtol=1e-6, atol=1e-6)


@pytest.mark.parametrize("bad", [{"step": 0}, {"lr": -1.}, {"beta1": 1.}, {"eps": 0.}])
def test_adamw_invalid_optimizer_config(bad):
    p = torch.ones(2)
    args = {"step": 1, "lr": .01, **bad}
    with pytest.raises(ValueError):
        adamw_step(p, p, p, p, **args)


@pytest.mark.parametrize("causal", [False, True])
def test_attention_forward_and_gradients_vs_sdpa(causal):
    torch.manual_seed(42)
    q, k, v = [
        torch.randn(2, 3, 4, 8, dtype=torch.float64, requires_grad=True)
        for _ in range(3)
    ]
    keep = torch.tensor([[True, True, True, True], [True, True, False, False]])
    visible = keep[:, None, None, :]
    if causal:
        visible = visible & torch.ones(4, 4, dtype=torch.bool).tril()[None, None, :, :]
    actual = reference_attention(q, k, v, causal=causal, padding_keep=keep)
    expected = F.scaled_dot_product_attention(q, k, v, attn_mask=visible, dropout_p=0.)
    torch.testing.assert_close(actual, expected, rtol=1e-10, atol=1e-10)
    ga = torch.autograd.grad(actual.square().sum(), (q, k, v), retain_graph=True)
    gb = torch.autograd.grad(expected.square().sum(), (q, k, v))
    for a, b in zip(ga, gb):
        torch.testing.assert_close(a, b, rtol=1e-9, atol=1e-9)


def test_attention_all_masked_rejected():
    q = torch.ones(1, 2, 3, 4)
    with pytest.raises(ValueError, match="all-masked"):
        reference_attention(q, q, q, padding_keep=torch.zeros(1, 3, dtype=torch.bool))


def test_attention_causal_suffix_consistency_and_future_isolation():
    torch.manual_seed(99)
    q, k, v = [torch.randn(1, 2, 5, 4) for _ in range(3)]
    full = reference_attention(q, k, v, causal=True)
    suffix = reference_attention(q[:, :, -2:, :], k, v, causal=True)
    torch.testing.assert_close(full[:, :, -2:, :], suffix)
    k[:, :, -1, :] += 123.
    v[:, :, -1, :] -= 321.
    changed = reference_attention(q, k, v, causal=True)
    torch.testing.assert_close(full[:, :, :-1, :], changed[:, :, :-1, :])


@pytest.mark.parametrize("shape", [(2, 4), (5, 9)])
def test_infonce_matches_clip_style_oracle_and_gradient(shape):
    torch.manual_seed(20)
    q = torch.randn(shape, dtype=torch.float64, requires_grad=True)
    k = torch.randn(shape, dtype=torch.float64, requires_grad=True)
    x = F.normalize(q, dim=-1) @ F.normalize(k, dim=-1).T / .13
    labels = torch.arange(shape[0])
    oracle = (F.cross_entropy(x, labels) + F.cross_entropy(x.T, labels)) / 2
    actual = symmetric_infonce(q, k, temperature=.13)
    torch.testing.assert_close(actual, oracle, rtol=1e-12, atol=1e-12)
    ga = torch.autograd.grad(actual, (q, k), retain_graph=True)
    gb = torch.autograd.grad(oracle, (q, k))
    for a, b in zip(ga, gb):
        torch.testing.assert_close(a, b, rtol=1e-12, atol=1e-12)


def test_infonce_single_direction_oracle():
    q = torch.eye(3, dtype=torch.float64)
    k = torch.eye(3, dtype=torch.float64)
    logits = q @ k.T / .2
    oracle = F.cross_entropy(logits, torch.arange(3))
    torch.testing.assert_close(symmetric_infonce(q, k, temperature=.2, symmetric=False), oracle)


@pytest.mark.parametrize("bad_tau", [0., -1., float("inf"), float("nan")])
def test_infonce_bad_temperature(bad_tau):
    with pytest.raises(ValueError):
        symmetric_infonce(torch.eye(2), torch.eye(2), temperature=bad_tau)


def test_infonce_zero_vector_rejected():
    with pytest.raises(ValueError):
        symmetric_infonce(torch.zeros(2, 4), torch.ones(2, 4))
