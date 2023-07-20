'''
使用类和实例：
类编写好后，根据类创建的实例。可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。
下面创建一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法：

class Car():
    def __init__(self, make, model, year):  #1
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):  #2
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)  #3
print(my_new_car.get_descriptive_name())

在#1处，定义方法__init__() 与前面的Dog类一样，第一个形参为self ；包含另外三个形参：make 、model 和year 。
方法__init__() 接受这些形参的值，并将它们存储在根据这个类创建的实例的属性中。创建新的Car实例时，需要指定其制造商、型号和生产年份。
在#2处，定义一个名为get_descriptive_name() 的方法，它使用属性year 、make 和model创建一个对汽车进行描述的字符串。
为在这个方法中访问属性的值，使用self.make 、self.model 和self.year 。
在#3处，根据Car类创建一个实例，并将其存储到变量my_new_car中。接下来，调用方法get_descriptive_name() ，指出是一辆什么样的汽车
运行结果：
2016 audi a4

给属性指定默认值：
下面给汽车添加一个随时间变化的属性，存储汽车的总里程。
类中的每个属性都必须有初始值，如设置默认值时，在方法__init__()内指定这种初始值是可行的，无需包含为它提供初始值的形参。
下面来添加一个名为odometer_reading 的属性，其初始值总是为0
再添加了一个名为read_odometer() 的方法，用于读取汽车的里程表：

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  #1

    def get_descriptive_name(self):
        (代码略)

    def read_odometer(self):  #2
        print("This car has " + str(self.odometer_reading) + " miles on it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

当Python调用方法__init__() 创建新实例时，像前一个示例一样以属性的方式存储制造商、型号和生产年份。
在#1处，Python将创建一个名为odometer_reading 的属性，并将其初始值设置为0。
在#2处，定义了一个名为read_odometer() 的方法，获悉汽车的里程。一开始汽车的里程为0。
运行结果如下：
2016 audi a4
This car has 0 miles on it.

修改属性的值：
可以以三种不同的方式修改属性的值：直接通过实例修改；通过方法设置；通过方法递增（增加特定的值）。

1.直接修改属性的值：
要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为23：
class Car():
    (略)
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23  #1
my_new_car.read_odometer()
在#1处，使用句点表示法直接访问并设置汽车的属性odometer_reading 。这行代码让Python在实例my_new_car
中找到属性odometer_reading ，并将该属性的值设置为23。

2.通过方法修改属性的值：
update_odometer() 的方法：
class Car():
    (略)
    def update_odometer(self,mileage):  #1
        self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)  #2
my_new_car.read_odometer()
在#1处添加方法update_odometer() 。在#2处，调用update_odometer() ，并向它提供了实参23（该实参对应于形参mileage）,它将里程表读数设置为23。

3.通过方法对属性的值进行递增：
update_odometer() 的方法：
class Car():
    (略)
    def update_odometer(self,mileage):
        (略)
    def increment_odometer(self, miles): #1
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.increment_odometer(100)#2

运行结果：
2016 audi a4
This car has 23 miles on it.
This car has 123 miles on it.

3.通过方法对属性的值进行递增：
    def increment_odometer(self, miles): #1
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.increment_odometer(100)#2
在#1处，新增的方法increment_odometer() 接受一个单位为英里的数字，并将其加入到self.odometer_reading 中。在#2处，调用increment_odometer()
并传入100 ，以增加新行驶行驶的100英里。

运行结果：
2016 audi a4
This car has 23 miles on it.
This car has 123 miles on it.

'''