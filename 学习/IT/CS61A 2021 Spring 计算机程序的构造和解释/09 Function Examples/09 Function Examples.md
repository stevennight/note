# 09 Function Examples

## 练习
反转一个数字
```python
def reverse_digits(n):
    """ 假设n是>0的整数。返回10进制表示的N的反转。
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1)
    1
    >>> reverse_digits(1234)
    4321
    >>> reverse_digits(10)
    1
    >>> reverse_digits(12321)
    12321
    >>> reverse_digits(111)
    111
    """
    # 前置检查
    assert type(n) is int and n >= 0

    if n < 10:
        return n
    
    return reverse_digits(n // 10) + (n % 10) * 10 ** (num_digits(n) - 1)

def num_digits(n):
    digits_count = 1
    if (n >= 10):
        digits_count += 1
        n = n // 10
    return digits_count
```

P.S.
1. 测试确保涵盖了主要的例子，但不关心内部结构（黑盒测试） 
2. 了解具体实现，想确保例子会执行代码的某部分（白盒测试）

## 交错数字
假设A/B数字位数相同
```python
def interleave_digits(a, b):
    """ 假设 A B是位数相同的非负整数的十进制数字。返回10进制表示的A、B交错的数字。
    由A开始。
    >>> interleave_digits(1,2)
    12
    >>> interleave_digits(0,1)
    1
    >>> interleave_digits(1,0)
    10
    >>> interleave_digits(123,456)
    142536
    >>> interleave_digits(111111,222222)
    121212121212
    """
    if a <= 9:
        return a * 10 + b
    # stringy tree 弘树
    # 左边是很长的分支，右边是一个小分支
    return interleave_digits(a // 10, b // 10) * 100 + \
        interleave_digits(a % 10, b % 10)
```

## Enviorment Detective
Page 5
```python
# 变量交换
flip, flop = flop, flip
```

## Tracing 跟踪
```python
# ↓高阶函数
def trace1(f):
    def traced(x):
        print("->", x)
        r = f(x)
        print("<-", r)
        return r
    return traced

# decorators 装饰器
# 下面square可以理解为 square = trace1(square)
@trace1
def square(x):
    # ...
```