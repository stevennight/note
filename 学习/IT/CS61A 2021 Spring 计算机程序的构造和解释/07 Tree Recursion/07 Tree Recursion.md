# 07 Tree Recursion 树形递归

sierpinski's triangle: make_gasket()是一个树形递归

```python
def find_zero(lowest, highest, func):
    """Return a value v such taht LOWEST <= v <= HIGHEST and
    FUNC(v) == 0, or None if there is no such value.
    Assumes that FUNC is a non-decreasing function from integers to integers
    (that is, if a < b, then FUNC(a) <= FUNC(b)). """

    if lowest > highest: # Base Case
        return None
    elif func(lowest) == 0: # Base Case
        return lowest
    else: # Inductive Case
        return find_zero(lowest + 1, highest, func)
# 线性递归（尾递归）


def find_zero(lowest, highest, func):
    if lowest > highest: # Base Case
        return None

    middle = (lowest + highest) // 2
    if func(middle) == 0: 
        return middle
    elif func(middle) < 0:
        return find_zero(middle + 1, highest, func)
    else: # Inductive Case
        return find_zero(lowest, middle - 1, func)
# 线性递归（尾递归）
```

```python
# 不使用if语句 用and/or
def is_a_zero(lowest, highest, func):
    """Return true if there is a value v such that LOWEST <= v <= HIGHEST
    and FUNC(v) == 0. Assume that FUNC is a non-decreasing function
    from integers to integers."""
    middle = (lowest + highest) // 2
    return lowest <= highest \
        and (func(middle) == 0 \
            or (func(middle) < 0 and is_a_zero(middle + 1, highest, func))
            or (func(middle) < 0 and is_a_zero(lowest, middle - 1, func)))
# 线性递归

def is_a_zero(lowest, highest, func):
    """Return true if there is a value v such that LOWEST <= v <= HIGHEST
    and FUNC(v) == 0. Assume that FUNC is a non-decreasing function
    from integers to integers."""
    middle = (lowest + highest) // 2
    return lowest <= highest \
        and (func(middle) == 0 \
            or (func(middle) < 0 and is_a_zero(middle + 1, highest, func))
            or is_a_zero(lowest, middle - 1, func))
# 树形递归
# 有可能同时调用 is_a_zero(middle + 1, highest, func) is_a_zero(lowest, middle - 1, func))
```

## Finding a Path
Page 29
Page 31 

## 分析
线性递归，与次数成正比
is_path,3**y0，指数增长

## 分区计数
```python
def partition(n, k):
    ...
partition(6, 3)
```

每步划分为：<br/>
取k partition(n-k, k)<br/>
不取k partition(n, k-1)

## Recurrences

## The Towers of Hanoi 汉诺塔（树形递归）
```python
def move_tower(n, start_peg, end_peg):
    """Perform moves that transfer an ordered tower of N > 0 disks in the 
    Towers of Hanoi puzzle from peg START_PEG to peg END_PEG, where
    1 <= START_PEG, END_PEG <= 3, and START_PEG != END_PEG.
    Assumes the disks to be moved are all smaller than those on the other 
    pegs."""

    ## exception for 不遵循输入规则
    ## lecture 8

    if n == 1:
        #...
    else:
        # ...
        # 1 + 2 + 3 - start - end = 空余柱子编号
        spare_peg = 6- start_peg - end_peg 
        # 可以看看课程源码他是怎么在控制台中输出 字符图像 过程的。
