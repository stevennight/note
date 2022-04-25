# 16 Objects Classes

## Motivation 动机
### Building a chocolate shop
商品：名称、价格、说明、库存
顾客：姓名、地址
订单：商品及数量、支付信息（信用卡）

函数：
```python
# 库存跟踪
add_product(name, price, nutrition)
get_label(product)
get_nutrition_info(product)
increase_inventory(product, amount)
reduce_inventory(product, amount)

# 顾客跟踪
signup_customer(name, address)
get_greeting(customer)
get_formatted_address(customer)

# 购买跟踪
order(customer, product, quantity, cc_info)
track(order_number)
refund(order_number, reason)

# 先弄清楚想做什么
# 再用函数、object 等来实现
```

## Objects
数据以及行为的集合
```python
# 库存跟踪
Product(name, price, nutrition)
Product.get_label()
Product.get_nutrition_info()
Product.increase_inventory(amount)
Product.reduce_inventory(amount)
Product.get_inventory_report()

# 顾客跟踪
Customer(name, address)
Customer.get_greeting()
Customer.get_formatted_address()
Customer.buy(product, quantity, cc_info)

# 购买跟踪
Order(customer, product, quantity, cc_info)
Order.ship()
Order.refund(reason)
```

### 概念
class是数据类型的模板；<br />
class的实例叫做object<br />
每个object有数据属性，叫做instance variables描述其状态<br />
每个obejct有函数属性，叫method(改变状态、instance variables)

## Classes
class可以设置初始实例变量、定义方法。
```python
class Product:

    # class variables 类变量
    # object中没有定义，就会在class中寻找。
    # 假如直接修改 如 Product._sales_tax = 0.1，会影响所有的object._sales_tax的值
    # 因为object中找不到对象属性，就找Product._sales_tax。
    _sales_tax = 0.07

    # 构造函数调用__init__
    def __init__(self, name, price, nutrition_info):
        # python 对象变量/对象属性 都是 公共的。
        self._name = name
        # ...
        self._inventory = 0
    
    # python的method中，第一个参数是对象本身。
    def increase_inventory(slef, amount):
        self._inventory += amount
    
    def reduce_inventory(self, amount):
        if self._inventory < amount:
            print("OH NO! WE OUT")
            # 动态变量 未初始化、未定义
            self._needs_restocking = True
            return
        self._inventory -= amount

    def get_nutrition_label(self):
        return "|".join(self._nutrition_info)

    def get_inventory_report(self):
        return f"We have {self._inventory} bars" # 字符串格式化

# 在全局框架的pina_bar变量中指向的位置。
pina_bar = Product("test", 7.99, ["1 g sugar"]) # 参数传递到__init__
# 只是一个函数
Product.increase_inventory(pina_bar, 2)
# 绑定到对象的方法
pina_bar.increase_inventory(2)
```
