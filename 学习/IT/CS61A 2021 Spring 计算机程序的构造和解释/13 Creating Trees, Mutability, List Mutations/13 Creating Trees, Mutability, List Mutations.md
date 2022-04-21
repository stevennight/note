# 13 Creating Trees, Mutability, List Mutations

## Tree
抽象层

数据抽象：tree(), children(), label(), is_leaf()

用户程序：count_leaves(t) double(t)
```python
def double(t):
    """Returns a tree identical to T, but with all labels doubled."""
    if is_leaf(t):
        return tree(label(t) * 2)
    else:
        # doubled_children = []
        # for c in children(t):
        #     doubled_children.append(double(c))
        # return tree(label(t) * 2, doubled_children)
        return tree(label(t) * 2, 
            [double(c) for c in children(t)]
        )
```

## Mutation
### Non-destructive vs. Destructive 非破坏性 vs 破坏性操作
非破坏性：做的对象操作不会改变对象 => double(t)[未改变输入对象t]

破坏性：做的操作能够改变对象

### Immutability vs. Mutability 不可变 vs. 可变
不可变：一旦创建不可修改。int float string tuple
```python
a_str = "Hello"
id(a_str)
a_str += " world"
id(a_str) # 返回的ID不一样，创建了新的对象。number类型也是一样。

x = 5
y = x # 这里会进行引用传递，y指向x指向的对象5. id(x) = id(y)
y = 6 # 这里将y的指向变更为对象6，但是不会影响x的指向。 id(x) != id(y)

x = [1, 2]
y = x # 这里会进行引用传递，y指向x指向的对象列表 id(x) = id(y)
y[0] = 2 # 这里改变的是y指向列表的[0]这个位置的指向，并非改变y的指向。id(y) = id(x)仍成立。y[0] x[0]仍然是同一块空间。所以这里的y[0]赋值也影响到了x[0]，因为都是同一个列表同一块空间。
y = [2, 3] # 这里直接改变了y的指向，所以不会影响x的指向/内容。id(x) != id(y)
```

可变：可以改变值 dictionaries, lists

dictionaries, lists 在函数传递中，引用传值。
在函数内部对他们的变更可能会改变到外部环境的dict, list。如 l[0] 这样的赋值。

### 不可变里的可变元素
```python
t = (1, [2, 3])
```

上面的构造函数tree()，在不打破抽象界限的情况下，属于不可变。
### 可变树
```python
# 改变tree的结构 => list之后可以用以下function实现
def set_label(tree, label):
    tree[0] = label

def set_children(tree, children):
    tree[1] = children
```


### 破坏性的tree doubling
略。 用上面的set_label。

## List
```python
#copy a list slice
listA = [1, 2]
listB = listA # 同一指向，没有copy
listC = listA[:]
listD = list(listA)

# list 的改变方式
# 注：改同一个list对象， id(l)不变
L[2] = 1 # 索引形式修改
L[1:3] = [] # 切片形式修改
L += [2,3] # +运算形式修改

l.append(4) # 一个
l.extend([3, 4]) # 多个
l.pop() # pop
l.remove(4) # 移除等于指定值的第一个元素
```