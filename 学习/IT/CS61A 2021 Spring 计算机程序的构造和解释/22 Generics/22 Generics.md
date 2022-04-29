# 22 Generics

## String Formatting
```python
print("%s, %syMc%sFace" % (greeting, noun,  noun))
print("{}, {}yMc{}Face".format(greeting, noun, noun))
print("{0}, {1}yMc{1}Face".format(greeting, noun))
print("{greeting}, {noun}yMc{noun}Face".format(greeting=greeting, noun=noun1))
print(f"{greeting}, {noun}yMc{noun}Face")
print(f"{greeting.lower()}, {noun[0:3]}yMc{noun[-1]}Face")
# 对象 调用 __str__ 方法
greeting = 36.999999
print(f"{greeting:.2f}, {noun[0:3]}yMc{noun[-1]}Face")
rf"{greeting} and \n {noun}" # 36.999999 amd {换行} boat
fr"{greeting} and \n {noun}" # {greeting} and \n {noun}
```

## Generics 泛型
```python
# items 可以是任何的可迭代类型/迭代器，tuple, list ... 泛型
def map(items, func):
    # ...
    for item in items:
        # ...

# item, initial_value 要可相加。
def sum(items, initial_value):
    sum = initial_value
    for item in items:
        sum += item
    return sum

class Rational:
    # ...

    # Rational + Retional 遇到这样的相加就会调用__add__方法。
    # 乘法、取模、减法、除法div floordiv等等都可。
    # += __iadd__
    # __getitem__ S[k], __setitem__ S[k] = v, __len__, __setattr__ x.n=v
    # __delattr__ del x.n, __sub__, __mul__, __eq__, __lt__ 
    def __add__(self, other):
        new_numer = self.numer * other.denom + other.numer * self.denom
        new_denom = self.denom * other.denom
        return Rational(new_numer, new_denom)
```
### Duck typing
根据函数的行为，可以使用任何类型的对象的能力，称为duck typing

## String Joining
```python
names = ["test", "test2"]
"".join(names)
",".join(names)
```