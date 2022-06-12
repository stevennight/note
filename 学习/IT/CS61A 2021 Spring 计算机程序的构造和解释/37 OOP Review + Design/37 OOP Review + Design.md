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
# 类型分派：函数检查传参类型，选择合适的行为
def print_obj(obj):
    if hasattr(obj, "__iter__"):
        for item in obj:
            print(item)
    else:
        print(obj)

print_obj([1, 2, 3])
print_obj(123)

def display_first(data):
    if isinstance(data, Link):
        print(data.first)
    elif isinstance(data, Tree):
        print(data.label)
    else:
        raise Error("Unsupported data type!")
display_first(Link(1, Link(2, Link(3))))
display_first(Tree("A", [Tree("B", Tree("C"))]))
```

## Design Principles 设计原则

## Easy Construction
```python
class LinkedList:
    def __init__(self, values):
        self.head = link = Link(None) # self.head => 哨兵节点
        for value in values:
            link.rest = Link(value)
            link = link.rest

    def __iter__(self):
        link = self.head.rest
        while link is not Link.empty:
            yield link
            link = link.rest

lnk = LinkedList([1, 2, 3, 4])
for link in lnk:
    print(link.first)
```

## Set Boundaries
```python
class Insect:
    def __init__(self):
        self.__health = 100 # => 被python重写成 __classname__attrname，保护实例变量。
        self.__perished = False

    def reduct_health(self, amount):
        self.__health -= amount
        # 边界
        if self.__health <= 0:
            print("Ohno! I have perished")
            self.__perished = true

class Ant(Insect):
    pass

class BumbleBee(Insect):
    def avenge_bee_deaths(self, ant):
        # ant.__health -= 1000 # Error, AttributeError.
        ant.reduct_health(1000)
```

## Check Your Assumptions
```python
# before
class Person:
    def __init__(self, first_name, middle_name, last_name):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name[0]}."

# after
class Person:
    def __init__(self, family_name, given_name, family_first=True):
        self.family_name = family_name
        self.given_name = given_name
        self.family_first = family_first

    def __str__(self):
        if self.family_first:
            return f"{self.family_name}, {self.given_name}"
        else:
            return f"{self.given_name} {self.family_name}"
```