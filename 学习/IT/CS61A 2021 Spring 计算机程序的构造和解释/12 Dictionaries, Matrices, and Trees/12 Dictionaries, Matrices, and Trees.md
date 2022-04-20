# 12 Dictionaries, Matrices, and Trees 字典 矩阵 树

小项目：
[https://](https://cats.cs61a.org/)https://cats.cs61a.org/

## Dictionaries
```python
states = {
    "CA": "California",
    "DE": "Delaware",
    "NY": "New York",
    "TX"："Texas",
    "WY": "Wyoming"
}
len(states)
"CA" in states
states["CA"]
states.get("CA", "😄")
states["LA"] = "Los Axxx"
states["LA"] += "(test)"
# key可以是任何的不变类型，包括tuple p.s. String是不可变的
# Value可以是任何值。
# '1' 和 1 是不同类型，在字典里面可以共同存在，和javascript/php 不同。
# 遍历：插入顺序（python 3）   python 2 => 随机
for name in states:
    print(states[name])
```

## Matrices
```python
# 行主序。 列主序同理。一元list二元tuple也可行，但是修改时要替换整个tuple。
def matrix(rows, cols):
    return [ [0 for col in range(cols)] for row in range(rows) ]
def value(matrix, row, col):
    return matrix[row][col]
def set_value(matrix, row, col, val):
    matrix[row][col] = val
```

## Tree
node, child, root, sub tree 子树, leaves, inner node, label(node上的值)

binary tree 二叉树

```python
# list of list
def tree(label, children = []):
    return [label] + children
def label(tree):
    return tree[0]
def children(tree):
    return tree[1:]
def is_leaf(tree):
    return len(children(tree)) == 0
# list of tuple
# dict

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        # count_leave = 0
        # for sub in children(t):
        #     count_leave += count_leaves(sub)
        # return count_leave
        return sum([count_leaves(sub) for sub in children(t)])
```