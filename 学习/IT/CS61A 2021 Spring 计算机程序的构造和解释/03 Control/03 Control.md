# 03 Control 流程控制

## Enviorment 环境

### 例1
```python
def square(x): return x*x
def sum_square(x, y):
  return square(x)+square(y)
z = sum_square(3, 4)
```

<div style="border: 1px solid #eee; padding: 10px; margin: 10px 0;">
全局：<br>
square -> def square(x) 全局<br>
sum_square -> def sum_square(x,y) 全局

f1：<br>
x=3<br>
y=4<br>
return

f2：<br>
x=3<br>
return 9

f3：<br>
x=4<br>
return 16
</div>

### 例2
```python
def id(x):
  return x
print id(id)(id(13))
```
调用顺序：
   1. **id(id)**(id(13)) f1
   2. id(**id(13)**) f2
   3. **id(13)** f3

<div style="border: 1px solid #eee; padding: 10px; margin: 10px 0;">
全局：<br>
id -> def id(x) 全局

f1：<br>
x=id<br>
return id

f2：<br>
x=13<br>
return 13

f3：<br>
x=13<br>
return 13
</div>


### 例3
```python
def incr(n):
  def f(x):
    return n + x
  return f

print(incr(5)(6))
# 上面的写法与下面的写法相同
g = incr(5)
print(g(6))
```

<div style="border: 1px solid #eee; padding: 10px; margin: 10px 0;">
全局：<br>
incr -> def incr(n) 全局

f1：<br>
n=5<br>
f -> def f(x) f1<br>
return f

f2：<br>
x=6<br>
return n+x=5+6=11(n来源f1，因为f2环境的父级是定义func f的f1环境)
</div>

## Control 流程控制
```python
# 表达式形式
1/x if x != 0 else 1 # 1/2 输出0.5
5 and "hello" # 输出hello
5 or "hello" # 输出5

# 语句形式
''' 注意缩进、嵌套 '''
if x > 0:
  return 1
elif x == 0:
  return 0
else:
  return -1

# 迭代(递归)
def add_sq(accum, k, n):
  if k > n:
    return accum
  else:
    return add_sq(accum + k ** 2, k + 1, n)

# while
accum = 0
k = 1
n = 100
while k <= n:
  accum = accum + k ** 2
  k += 1
print(accum)
```