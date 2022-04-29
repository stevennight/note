# 23 Fun with Iterables

iterable,
iterator（有__next__，不一定要继承iterator class。鸭子类型(duck typing)，像（有需要的东西，比如__next__，即可。）,
generator,
for loop

__iter__ return iterator, or generator. not iterable(without __next__)

__iter__ or __getitem__ （旧版本支持，for loop找不到__iter__，还回去找__getitem__）

reversed(), zip(), map(), filter() return iterator.

> Exercise: Write zip using map();

list(), tuple(), set(), sorted() return iterable

max(), min(), sum(), all(), any() process iterables

## 概念图
![](https://file.nyatori.com/images/a71301c3c00c217426b62994f3a65de7.png)