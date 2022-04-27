# 19 Recursive Object

## Tree
```python
class Tree:

    def __init__(self, label, branches = []):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ',' + repr(self, brances)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)
    
    def __str__(self):
        return '\n'.join(self.indented())

    def indested(self):
        lines = []
        for b in self.brances:
            for line in b.indented():
                lines.apped(' ' + line)
        return [str(self.label)] + lines
```

## Linked lists
List, 动态数组，插入操作，需要对后续元素一个一个往后移动，缓慢。

链表，每个对象存储值以及下一个元素的引用（地址）。插入只需要更改前一个元素的指向以及当前元素的指向。

链表 插入 空间换时间

```python
class Link:
    empty = ()

    def __init__(self, first,  rest=empty):
        # 测试rest假如为()空tuple, rest is Link_empty为True, 空turple id似乎一样。
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    # ...
```

### Create Linked Lists
#### Creating  a range
```python
def range_link(start, end):
    if start >= end:
        return List.empty
    return Link(start, range_link(start + 1, end))

def map_link(f, ll):
    if ll is Link.empty:
        return Link.empty
    return Link(f(ll.first), map_link(f, ll.rest))

def filter_link(f, ll):
    if ll is Link.empty:
        return Link.empty
    elif f(ll.first):
        return Link(ll.first, filter_link(f, ll.rest))
    return filter_link(f, ll.rest)
```

### Mutating Linked Lists
```python
# 直接修改链表的值
s = Link("A", Link("B"))
s.first = "Hi"
s.rest.first = "Hola"
```

### infinite list
```python
# 循环链表 不推荐
s = Link("A", Link("B", Link("C")))
t = s.rest
t.rest = s
```

### Adding to front of linked list 添加到链表头部
```python
def insert_front(linked_list, new_val):
    """
    >>> ll = Link(1, Link(3, Link(5)))
    >>> insert_front(ll, 0)
    Link(0, Link(1, Link(3, Link(5))))

    return Link(new_val, linked_list)
```

### Adding to an ordered linked list 添加到有序链表
P40

## Recursive Objects
Tree 和 Link 对象中包含对相同类型对象的引用。

处理递归对象，可以使用递归方法。