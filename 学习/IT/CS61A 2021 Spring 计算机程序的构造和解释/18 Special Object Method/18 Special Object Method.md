# 18 Special Object Method

## Objects
tuple: 单元素元组，必须末尾带,提示为tuple
```python
(1) # 单纯的1
(1,) # tuple
```
 
### object内置属性
```python
# 返回对象的属性
```
 
## String Representation字符串表示方法
```python
one_third = 1/3
float.__str__(one_third) # 通常 类型.__str__(对象) 0.3333333
one_half = Fraction(1, 2)
Fraction.__str__(one_half) # 1/2

# str(), f-string 隐式调用了__str__

repr(one_half) # ↓ python实际调用，语法糖
Fraction.__repr__(one_half) # Fraction(1,2) 返回构造函数调用语句字符串
eval(Fraction.__repr__(one_half)) # eval执行字符串内容，创建新的Fraction

class Lamb:
    # ...

    def __str__(self):
        return f"羊 ： {self.name}"

    def __repr__(self):
        retunr f"Lamb({repr(self.name)})"
```

## Attribute access
```python
class Bunny:
    species_name = "Bunny"

    def __init__(self, name):
        self.name = name

    # object.name 实际调用↓
    def __getattribute__(self, name):
        # ...
        super().__getattribue__(name)

bunny = Bunny("Bugs")
bunny.species_name
bunny.ear_type # 报错
getattr(bunny, "ear_type", False) # 返回默认值

# 判断属性是否存在
if hasattr(bunny, "ear_type"):
    # ...

# more
# __setattr__(obj, "name", value) x.n = v
# __delattr__(obj, "name") del x.n
# __eq__(obj, x) obj == x
# __ne__(obj, x) obj != x
# __ge__(obj, x) obj >= x
# __gt__(obj, x) obj > x
# __le__(obj, x) obj <= x
# __lt__(obj, x) obj < x
# more ...
```