'''
继承：
编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可使用继承 。
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类 ，而新类称为子类 。
子类继承其父类的所有属性和方法，同时还可以定义自己的属性和方法。

子类的方法init ()：
创建子类的实例时，首先给父类的所有属性赋值。
例如，下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此可以在前面创建的Car类的基础上创建新类ElectricCar ，
这样就只需为电动汽车特有的属性和行为编写代码。

下面来创建一个简单的ElectricCar类版本，它具备Car 类的所有功能：

子类的方法init ()：
创建子类的实例时，首先给父类的所有属性赋值。
例如，下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此可以在前面创建的Car类的基础上创建新类ElectricCar ，
这样就只需为电动汽车特有的属性和行为编写代码。

下面来创建一个简单的ElectricCar类版本，它具备Car 类的所有功能：

class Car():#1
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):#2
    def __init__(self,make,model,year):#3
        super().__init__(make,model,year)#4

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

class ElectricCar(Car):#2
    def __init__(self,make,model,year):#3
        super().__init__(make,model,year)#4

my_tesla = ElectricCar('tesla', 'model s', 2016)#5
print(my_tesla.get_descriptive_name())
首先是Car 类的代码（#1）。创建子类时，父类必须包含在当前文件中，且位于子类前面。在#2处，定义子类ElectricCar ，
必须在括号内指定父类的名称。方法__init__() 接受创建Car 实例所需的信息（#3）。
在#4处的super() 是一个特殊函数，帮助Python将父类和子类关联起来。这行代码让Python调用ElectricCar
的父类方法__init__() ，让ElectricCar 实例包含父类的所有属性。父类也称为超类 （superclass），名称super因此而得名。
在#5处，创建ElectricCar类的一个实例，并将其存储在变量my_tesla 中。提供了实参'tesla' 、'model s' 和2016 。
运行结果：2016 Tesla Model S

给子类定义属性和方法：
class Car():#1
    (略)

class ElectricCar(Car):#2
    def __init__(self,make,model,year):#3
        super().__init__(make,model,year)#4
        self.battery_size=70  #1
    def describe_battery(self):  #2
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
在#1处，添加新属性self.battery_size ，并设置其初始值（如70 ）。根据ElectricCar 类创建的所有
实例都将包含这个属性，但所有Car 实例都不包含它。在#2处，添加了一个名为describe_battery() 的方法，它打印有关电瓶的信息。

运行结果：
2016 Tesla Model S
This car has a 70-kWh battery.
'''

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def move(self):
        print('%s is moving now'%self.name)

    def ag(self):
        print("%s's age is : %s"%(self.name,self.age))

class Mindog(Dog):
    def __init__(self,tk,name,age):
        super().__init__(name,age)          #继存超类
        self.tk = tk

    def ttk(self):
        print("%s's track is %s,it's age :%s"%(self.name,self.tk,self.age))

a = Mindog(12,'heihei',7)
a.ttk()
a.move()