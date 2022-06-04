# 36 Review Linked Lists + Trees

## Linked-List 特性

Complexity:
1. 找常量k的#k的节点 θ(1) 【渐进符号θ性质：讨论常量时，永远都是θ(1)。在讨论变量时（k是函数），才有对应更复杂的表达式】
2. 前头加节点 θ(1)
3. 在节点M后加节点（假设M已找到） θ(1)
4. 找任意的#k节点 θ(k)，最坏θ(N)
5. list长度或者在list中找元素 最坏θ(N)

前头/中间插入快（已知节点），随机存取 差。
与python list相反。

## Linked-List Class
```python
class Link:
    """ A linked list node. """
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        """ Return string denotation of SELF as Link(first, rest). """
    def __str__(self):
        """ Return string denotation of SELF as <item item ...>."""

def toLinked(L):
    if len(L) == 0:
        return Link.empty
    result = last = Link(L[0], Link.empty)
    for item in L[1:]:
        last.rest = Link(item)
        last = last.rest
    return result
#### 能否让他用于 嵌套的Python list?
```

## 练习：Find Node k in List
```python
def split(L):
    """ Returns (Mid, Last, Length), where Last is the last node in linked list L, Mid is the node at or (for even length) just before the middle, and Length is the length. 
    If L is empty, return (empty, empty, 0).
    >>> split(toLinked([1, 2, 3, 4, 5]))
    (Link(3, Link(4, Link(5))), Link(5), 5)
    >>> split(toLinked([1, 2, 3, 4]))
    (Link(2, Link(3, Link(4))), Link(4), 4)
    """
    if L is Link.empty:
        return (L.empty, L.empty, 0)

    Mid = L
    Length = 1
    while L.rest is not Link.empty:
        Length += 1
        if Length % 2 == 1:
            Mid = Mid.rest
        L = L.rest

    return (Mid, L, Length)
```

## 练习：Itersperse List(ⅠⅡⅢ)
```python
# 非破坏性
def intersperse(L, pred, inserts): 
    """Returns a copy of linked list L in which the items whose values satisfy PRED (a one-argument, boolean function) are followed by successive values from linked list INSERTS, until INSERTS is exhausted. The function is non-destructive. 
    >>> data = toLinked([1, 2, 3, 4, 5]) 
    >>> alt = toLinked([10, 11, 12, 13]) 
    >>> print(intersperse(data, lambda x: x % 2 == 1, alt)) 
    <1 10 2 3 11 4 5 12> 
    >>> print(intersperse(data, lambda x: True, alt)) 
    <1 10 2 11 3 12 4 13 5> 
    """

    if L is Link.empty or inserts is Link.empty
        return L
    if pred(L.first):
        return Link(L.first, Link(inserts.first, intersperse(L.rest, pred, inserts.rest)))
    else:
        return Link(L.first, intersperse(L.rest, pred, inserts))

def intersperse2(L, pred, inserts): 
    """Returns a copy of linked list L in which the items whose values satisfy PRED (a one-argument, boolean function) are followed by successive values from linked list INSERTS, until INSERTS is exhausted. The function is non-destructive.""" 
    sentinel = Link(None) # 用于边缘情况
    # Code 
    return sentinel.rest

# 破坏性操作
def dintersperse(L, pred, inserts): 
    """Returns a copy of linked list L in which the items whose values satisfy PRED (a one-argument, boolean function) are followed by successive values from linked list INSERTS, until INSERTS is exhausted. The function is destructive and creates no new Link nodes."""

    result = L
    while L is not Link.empty and inserts is not Link.empty:
        if pred(L.first):
            LR = L.rest
            L.rest = inserts
            IR = inserts.rest
            inserts.rest = LR

            L = LR
            inserts = IR
        else:
            L = L.rest

    return result
```

## 二叉树 Binary Tree
```python
def isIn(T, target):
    """Return True iff T contains the label TARGET."""

def add(T, target): 
    """Destructively modify T to add the label TARGET, if it is not already
present. Return the resulting tree."""
```