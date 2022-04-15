# Data Abstration

## 序列
### Multiple Variables 多个变量
deconstructed: 解构
```python
x, y = (1, 9)

for x, y in [(1, 2), (3, 4)]:
    # ...

# zip() return generator生成器.
list(zip([1, 2], [3, 4, 5])) # return [(1, 3), (2, 4)]

beasts = ["a", "b"]
for n, animal in zip(range(1, 5), beasts):
    # ...
```

### 修改list
```python
L = [1, 2, 3, 4, 5]
L[2] = 6
L[1:3] = [9 ,8] # 删除后插入 [1, 9, 8, 4, 5]   左闭右开
L[2:4] = [] # 仅删除 [1, 9, 5]
L[1:1] = [2, 3, 4, 5] # 仅插入 [1, 2, 3, 4, 5, 9, 5]
L[len(L):] = [10, 11] # 尾部插入 [1, 2, 3, 4, 5, 9, 5, 10, 11]
L[0:0] = range(-3, 0) # 头部插入 [-3, -2, -1, 1, 2, 3, 4, 5, 9, 5, 10, 11]
          # ↑ 可以是任何序列，range, list, turple,  zip etc.
[0] * 3 # [0, 0, 0] == [0] + [0] + [0]
"a" * 3 # aaa
```

### List Comprehension
```python
[ x*x for x in range(2, 101) if isprime(x)]
[(a, b) for a in range(10, 13) for b in range(2)]
[ 0 for _ in range(5) ] # 通常 _变量名，可以忽略的值的变量。
```

### 练习
```python
def matches(a, b):
    """ 返回A[k] == B[k],符合条件的k的数量
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens", "indolence")
    4
    """

    #sum = 0
    #for x, y in zip(a, b):
    #    if x == y:
    #        sum += 1
    #return sum

    # one line
    # return sum([a[x] == b[x] for x in range(len(a))]) # 利用了布尔值相加
    return sum([1 for x, y in zip(a, b) if x == y])

# 三角形矩阵
def triangle(n):
    """ 假设N >= 0，返回包含N的列表
    >>> triangle(0)
    []
    >>> triangle(1)
    [[1]]
    >>> triangle(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """

    return [list(range(1, i+1)) for i in range(1, n+1)]
```

## Data Abstration 数据抽象
面向过程，不利于程序组织与程序的编程。使用数据类型组织程序。

抽象数据类型(abstract data type ADT)

接口(interface)

数据类型上定义操作：构造函数、accessors(访问器，读)、Mutators(变异器，写)

```python
# 有理数
from math import gcd

def make_rate(n, d): # Constructor
    """ 有理数 N/D， 假设 N, D是整数， D!=0
    """
    g = gcd(n, d)
    n //= g; d //= g
    return (n, d)

def numer(r): # Accessor
    """ 有理数 R 的最小分子
    """
    return r[0]

def denom(r): # Accessor
    """ 有理数 R 的最小分母
    """
    return r[1]

def add_rat(x, y):
    # n0, d0 = x <- 打破了抽象，知道了数据的组织方式
    # n1, d1 = y <- 打破了抽象，知道了数据的组织方式
    # n = n0 * d1 + n1 * d0
    # d = d0 * d1
    ## g = gcd(n, d)
    ## n //= g; d //= g
    ## return (n, d) <- 打破了抽象，知道了数据的组织方式
    # return make_rat(n, d) 
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))

def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))

def str_rat(r):
    return str(numer(r)) if denom(r) == 1 else f"{numer(r)/{denom(r)}}"

def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

# 使用
def extra_harmonic_number(n):
    """ 返回 1 + 1/2 + 1/3 + ... + 1/N 的有理数
    """
    s = make_rate(0, 1)
    for k in range(1, n+1):
        s = add_rat(s, make_rat(1, k))
    return s
```

用户不需要知道数据的组织方式， 各种的运算实现。
