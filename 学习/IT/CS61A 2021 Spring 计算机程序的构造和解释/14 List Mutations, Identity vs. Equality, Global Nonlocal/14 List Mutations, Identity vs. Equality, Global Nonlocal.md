# 14 List Mutations, Identity vs. Equality, Global Nonlocal

## List
### List creation
```python
a = []
b = [1, 2, 3]
c = b + [20, 30]
d = c[:]
e = list(c) # c 可以是任何可迭代对象，转成list。

# 以上操作是非破坏性的 non-destructive

# 注意：
a = []
b = [1, 2, 3]
c = b
b = b + [20, 30] # 非破坏性，c => [1,2,3] b => [1,2,3,20,30]
b += [20, 30] # 直接修改指向的列表，破坏性，c => [1,2,3,20,30] b => [1,2,3,20,30]
```
### List mutation
```python
L[2] = 6
L[1:3] = [9,8]
L[2:4] = []
L[1:1] = [2,3,4,5]
L[len(L):] = [10, 11]
L[0:0] = range(-3, 0)

# 以上操作是破坏性的 destructive
```

语法糖：可以用其他语法转换的结构

### List Method
```python
l.append(4)
l.append([5,6])
l.extend([5,6]) # 相当于 l += [5,6]，注意不等于 l = l + [5,6] <=新的list
l.pop()
l.pop(2)
l.remove()

# 以上操作是破坏性的
```

## Equality and Identity
相等、同一

相等： exp0 == exp1，值相等<br />
同一： exp00 is exp1，是否同一对象
```python
# is使用场景。通常使用==
if next_cup is None:
type(list1) is type(list2)

# 陷阱 =>
a = "orange"
b = "orange"
c = "o" + "range"
d = 2
e = 2
f = 10000000000000
g = 10000000000000
id(a)
id(b)
id(c)
id(d)
id(e)
a is b # True, python优化，同样的值指向了相同的对象。
d is e # 包括字符串和数字
f is g # False。不要用is，可能与期望值不一样
```

## Scope 作用域
```python
current = 0

#def count():
#    current = current + 1 # Error, python见到current = 之后会在本地框架中定义一个current变量，然后没有赋值。在没有赋值之前就做了current + 1的使用，发生异常。
#    print("Count:", current)

#def count():
#    # 不应该这样使用
#    global current
#    current = current + 1
#    # ...

def count(current):
    current = current + 1
    # ...
    return current

current = count(current)

# ↑ 高阶函数中修改父级框架的变量同理。
# 要那样做，先使用nonlocal <var>声明。
```

尽量不使用global, nonlocal