# 08 More on Functions

## Exceptions
```python
if N < 0:
    # raise 语句
    raise ValueError("...")
    # assert False 抛出assertion异常，约定俗成，通常不应该抛出该异常。

# 可预知的异常 以及 异常处理(不终止程序)
try:
    input = open(myfile).read()
except FileNotFoundError:
    print("文件不能打开", myfile)
    input = ""
```

P.S. 写一个方法，第一步是什么？ - 说明文档，最好能放几个例子（或者python的测试断言）

```python
# 可用stirl 斯特林公式（？）非常简单
def remove_digit(n, digit):
    """ 说明
    """
    if n == 0:
        return 0

    if n % 10 == digit
        return remove_digit(n // 10, digit)

    return digit + remove_digit(n // 10, digit) * 10

# 执行程序时 立即 运行测试
if __name__ == "main":
    import doctest
    doctest.testmod()
```
