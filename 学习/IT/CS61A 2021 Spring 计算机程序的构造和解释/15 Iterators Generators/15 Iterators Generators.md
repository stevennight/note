# 15 Iterators Generators 迭代器与生成器

## Iterators
### Iterables
可迭代对象：list, tuple, dict, string
```python
for item in iterable_object
[item.lower for item in iterable_object]
# 字典
{item: prices[item] * 0.75 for item in prices}
```

### Iterators
```python
# list.__iter__()
iterator = iter(list)
# iterator.__next__()
next(iterator) # 遍历完抛出异常，try except
# 判断是否迭代器
type(iterator)
iterator.__iter__

# for语法是迭代器的语法糖
# for语法的性能更优
for <name> in <expression>:
    <suite>

iterator = iter(<expression>)

try:
    while True:
        <name> = next(iterator)
        <suite>
except StopIteration:
    pass



# 相关函数
reversed((1,2,3))

chocolate_bars = ["90%", "70%", "55%"]
worst_first = reversed(chocolate_bars
# 危险
chocolate_bars[0] = "Dark" # 迭代器受到影响
chocolate_bars.append("10%") # 迭代器没有受到影响
# print => 55% 70% Dark
for chocolate in worst_first:
    print(chocolate)

zip(["a","b","c"], ["e", "f", "g"]

eng_nums = ["one", "two", "three"]
esp_nums = ["uno", "dos", "tres"]
zip_iter = zip(eng_nums, esp_nums)
eng, esp = next(zip_iter)
print(eng, esp)
# for ...

#map(func, [1,2,3], ...) 可以相当于以下语法。
# [func(x) for x in iterable]

# filter(func, [1,2,3]) 可以相当于以下语法。
# [x for x in iterable if func(x)]

# iter(iterator) 返回 迭代器本身（指向同一个迭代器）
for item in iterator: # <= 迭代器本身用在for语法里面。
```

## Generators
```python
def evens:
    num = 0
    while num < 10:
        yield num
        num += 2
    return None # next()调用走到return之后，会抛出StopIteration异常

gen = evens() # 返回生成器
next(gen) # 开始执行函数，并且在yield语句上暂停。得到yield语句返回的值。

for num in evens():
    print(num)
```

为什么使用生成器？<br />
生成器是懒加载。需要时才生成下一项。
可以处理大量输入，如大的文件内容，在需要时才往下读取，而不需要一下子读取完整个文件。
或者计算过程复杂，在需要的时候才计算，避免一下子的大量计算。
```python
def find_matches(filename, match):
    for line in open(filename):
        if line.find(match) > -1:
            yield line
```
### yield from
```python
def a_then_b(a, b):
    # for item in a
    #     yield item
    yield from a
```

### 树的遍历生成器
p29