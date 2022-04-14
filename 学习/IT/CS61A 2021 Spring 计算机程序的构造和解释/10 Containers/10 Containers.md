# 10 Containers
## Simple Pairs
创建“一对数”的表示方式。
```python
# 整数表示对
def pair(a, b):
    """返回一对非负整数（A, B）"""
    return 2**a * 3**b

def left(p):
    return multiplicity(2, p)
def right(p):
    return multiplicity(3, p)
def multiplicty(factor, n):
    """假设factor, n是整数，factor > 1。返回n可以被factor整除的次数。"""
    # 实现
    # 待运行看看对不对。
    if n % 3 != 0:
        return 0
    return 1 + multiplicty(factor, n / 3)


# 通过函数表示对
def pair(a, b):
    return lambda which: a if which == 0 else b

def left(p):
    return p(0)
def right(p):
    return p(1)

# 以上的表示、实现方式的改变，对使用者来说是不需要作改变的。理想状态。
```

## Nonlocal
```python
def set_left(p, v):
    """给予一对数(x, y)p，改变成(v, y)。没有返回。"""
def set_right(p, v):
    """给予一对数(x, y)p，改变成(x, v)。没有返回。"""

def pair(a, b):
    def pair_func(which, v=None):
        nonlocal a, b # 赋值可以赋值到父级框架中的变量。【很少用】 应该就类似php的global了吧（但是php的global应该是全局框架而不是父级？待确定）
        if which == 0:
            return a
        elif which == 1:
            return b
        elif which == 2:
            a = v
        else:
            b = v
    return pair_func
```

## Sequences 序列
由一堆变量组成。可以有限或无限。
可变或不可变。可以索引。可以可迭代。

Python的序列类型：
tuple, list【可变】, string【str字符的序列】, range, iterator, generator

非序列的数据集合：
sets, dictionaries

```python
# tuple
(1, "Hello", (2, 3))
()

# list
[1, "hello", (2, 3)]
[]

# range 左闭右开
range(4) # 0 1 2 3
range(2,5) # 2 3 4
range(1, 12, 2) # 1 3 5 7 9 11
range(4, 0, -1) # 4 3 2 1

# string
'xxx'
"xxx"
"""多行
第二行"""
'''同样多行'''
"转义\n哈哈\\."
"unicode \u0395"
r"\这里的\n不转换"

# Tuple, List, Range, String
t = (1, 2, 3)
l = [1, 2, 3]
r = range(2, 13)
s = "Hello, World!"

t[2]
l[2]
r[2]
t[-1] == t[len(t) - 1] # 最后一个
s[1]

# 切片 左闭右开
t[1:4] == (t[1], t[2], t[3])
t[2:] == t[2:len(t)]
t[::2] == t[0, len(t): 2] # 第三个参数是step
t[::-1] # 反向递减
s[0:5]
s[0:5:2]
s[4::-1] # 字符串反转输出
s[1:2] == s[1]

# 序列类型转换
list((1, 2, 3)) == [1, 2, 3]
tuple([1, 2, 3]) == (1, 2, 3)
list(range(2, 10, 2)) == [2, 4, 6, 8]
list("ABCD") == ['A', 'B', 'C', 'D']

# 组合
A = [1, 2, 3, 4]
B = [7, 8 ,9]
A + B == [1, 2, 3, 4, 7, 8, 9]
A[1:3] + B[1:]
(1, 2, 3, 4) + (7, 8, 9) == (1, 2, 3, 4, 7, 8, 9)
"Hello," + " " + "world"

# 序列循环
for x in t:
    # ...

for x in r:
    # ...
```