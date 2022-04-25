# 17 Inheritance Composition 继承与组合

## Movitation
### Building Animal Conserving
```python
Panda()
Lion()
Rabbit()
# ...
Food()

class Food:
    def __init__(self, name, type, calories):
        # ...

bamboo = Food("bamboo", "veggie", 10)

# Elephant, Rabbit ... 等等，属性、方法类似。
# 需要重用代码。
class Elephant:
    species_name = "xxx"

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten = 0
        self.happiness = 0

    def play(self, hour):
        self.happiness += (hour * 4)
    def eat(self, food):
        self.calories_eaten += food.calories
        # ...
    def interact_with(self):
        # ...
```

## Inheritance
### Base classes/Superclass and subclasses
多个类有相似的属性，可以定义一个基类base class，然后子类继承自基类。

上面的例子，Animal作为基类，Rabiit, Panda, Elephant... 继承Animal。

减少代码。

```python
class Animal:
    species_name = "Animal"
    play_multiplier = 2 # 不同的地方提取出来作为一个属性。
    # ...

    def __init(self, name, age=0):
        # ...

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        # ...
    
    def eat(self, food);
        # ...

    # ...

# 继承Animal类
class Elephant(Animal):
    sepcies_name = 'xxx'
    play_multiplier = 4

class Rabbit(Animal):
    sepcies_name = 'xxx'
    play_multiplier = 8
    # 基类中没有的属性
    num_in_litter = 12

class Panda(Animal):
    # override 重写方法
    def interact_with(self, other):
        self.happiness -= 1

class Lion(Animal):
    # 重写__init__
    def __init__(name, age):
        super().__init__(name, age)
        if age < 1:
            self.calories_needed = 1000
            # ...
    
    def eat(self, food):
        if food.type == "meat":
            # 调用父类的方法
            super().eat(food)
```

继承：优点：可以对一批子类执行相同（共有）的方法。

## Layer of inheritance
object <- Animal <- Rabbit, Panda ...

List, Dict 等都基于object类。

```python
# object <- Animal <- Herbivore <- Rabbit, Panda
#                  <- Carnivore <- Vulture, Lion
```

## Multiple inheritance 多重继承
不建议

## Identity 同一性
```python
mafasa = Lion("Mufasa", 15)
nala = Lion("Nala", 16)

mufasa is mufasa
mufasa is nala
mufasa is not Nala
nala is not None
```

## Composition 组合
一个对象由其他对象组成

```python
class Animal:

    def mate_with(self, other):
        if other is not self and other.species_name == slef.species_name:
            self.mate = other
            other.mate = self
```

## Inheritance vs. Composition
继承：is-a关系。兔子是一种特殊的动物。Rabbit继承了Animal。
组合：has-a关系。保护区里有很多动物。Conservatory有实例变量【Animal实例列表】。