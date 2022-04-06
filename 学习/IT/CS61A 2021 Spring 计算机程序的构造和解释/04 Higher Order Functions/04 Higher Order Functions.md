# 04 Higher Order Functions 高阶函数


测试：
```shell
python -m doctest -v xxx.py
```

doc comment 文档注释 - 测试

先写出注释和测试， 逐步测试可行 测试驱动开发


迭代

**课程中的same_length代码是不是有问题，如果//整除是四舍五入，确认一下。比如数字是999=>//=>100而不是99**


设计原则：
1. Functions should do one well-defined thing.
2. DRY Don't Repeat Yourself

Functions As Template 函数作为计算模板

Functions on Functions 函数传入函数参数
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

Functions that Produce Functions (return functions) 函数返回函数
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

> Higher Order Functions: functions that take fucntions and return functions.
> 
> 高阶函数：一个函数接受函数并返回函数