# 06 Recursion 递归

## 函数原理
函数名：函数语法说明/签名 signature
```python
def sqrt(x):
    """Assuming x >= 0 PreCondition
    return approximation to square root of X. PostCondition"""
    # 对于用户来说，函数是功能抽象。知道如何使用方法。
    # 对于实现者，关心计算正确结果。不关心值（参数）来自哪里。
    # 不断选择抽象，分离关注点，分治法，分成较小的部分处理。
```

## 递归
### Linear Recursion 线性递归
```python
def sum_squares(N):
    """Return The sum of K**2 for K from 1 to N(inclusive)."""
    if N < 1:
        return 0
    else:
        return N**2 + sum_squares(N - 1)
    # 自己调用自己，最多一次，线性递归
```

### Tail Recursion 尾递归
```python
def sum_squares(N):
    def part_sum(accum, k):
        if k <= N:
            return part_sum(accum + k**2, k + 1)
        else:
            return accum # 将累加的值，逐层、直接返回
    return part_sum(0, 1)
print(sum_squares(3))
```
尾递归，部分语言会优化成while。如Schema，但是python, java, javascript等语言不会做优化。

### 递归思想
调用方法、库，要着眼于文档（如何使用）而不是具体实现。

### 预防无限递归
“最小”值

### Induction 归纳法
①基本条件 p(b)成立
②假设p(k)成立，推导前一个数成立 p(k - 1)成立，k>b
③p(k) k>=b成立

Noetherian induction / well-founded induction
https://zh.wikipedia.org/wiki/%E8%89%AF%E5%9F%BA%E5%85%B3%E7%B3%BB

### Recursion and Induction
递归是一种归纳法：
推断函数适用于所有小于给定输入的参数，输入最终终止（不能小于某一数值），得出结论（程序有效）


sierpinski's triangle: page 27