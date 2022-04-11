# Environment 环境

1
```python
def f():
    return 0

def g():
    print(f())

def h():
    def f():
        return 1
    g()

h()
# print 0
```

2
```python
def f():
    return 0

g = f

def f():
    return 1

print(g())
# print 0
```

3
```python
def f():
    return 0

def g():
    print(f())

def f():
    return 1

g()
# print 1
```

4
```python
def f(f):
    f(1)

def g(x):
    print(x)

f(g)
# print 1
```

5
```python
def f():
    return 0

def g()
    return f()

def h(k)
    def f():
        return 1
    p = k
    return p()

print(h(g))
# print 0
```

6
```python
def f(p, k):
    def g():
        print(k)
    if k == 0:
        f(g, 1)
    else:
        p()

f(None, 0)
# print 0
# 最后f2调p()的时候，调的是f1的g()，print(k)的k是f1的0
```

7
```python
def f(x):
    x = x + 1

y = 4
f(y)
x = 2
f(x)
print(y, x)
# print 4 2
```

8
```python
def f(x):
    def g(y)
        x = y
    g(4)
    return x

print(f(3))
# print 3
# 注意：如果用js类比，需要注意其中的区别。js中使用var x = y在g(y)中重新定义一个x变量，则与该python代码运行一致。但是如果使用的是x = y这样的语句，那么x将指向f(x)环境中的x，g(y)中对x的修改，将影响到f(x)中x的值，运行结果将是return 4。
```

9
```python
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

print_sums(1)(3)(5)
# print 1 4 9
```

10
```python
# currying
def curry2(f):
    return lambda x: \
        lambda y: \
            f(x, y)

from operator import add
print(curry2(add)(30)(12)) # print 30 + 12 => 42
print(curry2(add)(30)) # print function value
```