# 代码题检查清单

## 正确性
- [ ] 输入/输出 shape 明确
- [ ] 边界条件明确
- [ ] mask / axis / broadcasting 明确

## 数值
- [ ] overflow/underflow
- [ ] dtype 与精度
- [ ] division by zero / log(0)

## 性能
- [ ] 时间复杂度
- [ ] 空间复杂度
- [ ] 是否有可向量化的 Python loop
- [ ] 是否产生不必要的大中间矩阵/重复 copy

## PyTorch
- [ ] contiguous/view/reshape 是否安全
- [ ] device/dtype 一致
- [ ] train/eval 行为
- [ ] no_grad/inference_mode 使用场景

## 测试
- [ ] tiny deterministic example
- [ ] random property test
- [ ] extreme values
- [ ] reference implementation parity
