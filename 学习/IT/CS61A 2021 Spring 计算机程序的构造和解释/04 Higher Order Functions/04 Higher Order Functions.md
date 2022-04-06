# 04 Higher Order Functions 高阶函数

## 额外内容

### 测试

```console
python -m doctest -v xxx.py
```

### 文档注释 Doc Comment
可用于解释说明<br>
也可以用于测试

```python
def add(x, y):
    """ 
    将两数相加
    >>> add(3,4)
    7
    >>> add(1, -1)
    0
    """
    return x+y
```
测试驱动开发：先写出注释和测试，再编写代码，逐步测试可行


## 迭代
例子： 03.py => is_prime

## 函数设计

设计原则：
1. Functions should do one well-defined thing. 做**一件**明确地事
2. DRY Don't Repeat Yourself 避免重复代码（same_length）

## 高阶函数 Higher Order Functions

> Higher Order Functions: functions that take fucntions and return functions.
> 
> 高阶函数：一个函数接受函数并返回函数

### Functions As Template 函数作为计算模板

### Functions on Functions 函数传入函数参数
```python
def summation(N, term):
    k = 1
    sum = 0
    while k <= N:
        sum += term(k)
        k += 1
    return sum
def square(x):
    return x*x
summation(5, square)
summation(5, lambda x: x*x)
summation(10, lambda x: x**3)
summation(10, lambda x: 1 / x)
summation(10, lambda k: x**(k-1) / factorial(k-1)) # Approximate e**x
```

### Functions that Produce Functions (return functions) 函数返回函数
```python
def add_func(f, g): # higher order functions 高阶函数
    """Return function that return F(x)+G(x) for argument x."""
    def adder(x):
        return f(x) + g(x)
    return adder # or return lambda x: f(x) + g(x)

from math import sin, cos, pi
h = add_func(sin, cos)
h(pi / 4)
```