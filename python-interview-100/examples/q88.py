# 对应题目：Q88 mock 应该 mock 什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

with patch('orders.service.payment_client.charge') as charge:
    charge.return_value = Receipt('ok')
    result = place_order(...)
    assert result.ok
