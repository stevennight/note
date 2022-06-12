# 37 OOP Review + Design

Object-Oriented Programming 面向对象编程
- Encapsulation 封装 把相关数据与行为Behavior绑在一起
- Composition 组合 对象可以包含其他对象
- Inheritance 继承 对象的固有行为来自祖先类ancestor classes
- Polymorphism 多态 一个函数可以在不同对象上运行

```python
# Polymorphism:
class Place:
    def add_insect(self, insect):
        insect.add_to(self)

class Insect:
    def add_to(self, place):
        self.place = place
    
class Bee(Insect):
    pass

class ThrowerAnt(Insect):
    pass

place = Place()
place.add_insect(Bee())
place.add_insect(ThrowerAnt())


# Polymorphism(Duck Typing):
# 一个通用的函数在（拥有特定方式行为的）任何对象上运行。
def print_list(iterable):
    item_num = 1
    for value in iterable:
        print(f"{item_num}. {value}")
        item_num += 1

class ShoppingList:
    def __init__(self, store, items):
        self.store = store
        self.items = items
    def __iter__(self):
        for item in self.item:
            yield item

shopping_list = ShoppingList("ZeroGrocery", ["Apples", "Tortillas"])
print_list(["A", "B", "C"])
print_list(shopping_list)


# Polymorphism(Type Coercion):
# 强制类型转换：函数将传参转成必要的类型。
def int_smash(num1, num2):
    """
    >>> int_smash(51.56, 34.72)
    5134
    """
    int1 = int(num1)
    int2 = int(num2)
    num_digits = count_digits(int2)
    while int1 > 0:
        int2 += ((int % 10) * pow(10, num_digits))
        num_digits += 1
        int1 = int1 // 10
    return int2
def int_smash(num1, num2):
    return int(num1) * 10 ** len((str(int(num2)))) + int(num2)

# Polymorphism(Type Dispatching):
# 类型分派：函数
```