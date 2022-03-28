# 03 Control 流程控制

## Enviorment 环境

### 例1
```python
def square(x): return x*x
def sum_square(x, y):
  return square(x)+square(y)
z = sum_square(3, 4)
```

### 例2
```python
def id(x):
  return x
print id(id)(id(13))
```

调用顺序：
   1. **id(id)**(id(13))
   2. id(**id(13)**)
   3. **id(13)**
   
环境图表：

// todo::看看要怎么画图表


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