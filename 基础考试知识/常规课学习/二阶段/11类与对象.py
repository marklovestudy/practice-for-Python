'''
面向对象编程的概念：
在面向对象编程中，编写表示现实世界中的事物和情景的类，并基于类创建对象。
编写类时，定义一类对象都有的通用行为。基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。
根据类来创建对象被称为实例化，可以使用类的实例。

创建和使用类：
下面创建一个表示小狗的简单类Dog，它表示的不是特定小狗，而是任何小狗。它们都有名字和年龄；
大多数小狗还会蹲下和打滚。由于大多数小狗都具备上述两项信息（名字和年龄）和两种行为（蹲下和打滚），
Dog类将包含这些。创建这个类后，使用它来创建表示特定小狗的实例。

创建Dog类：
根据Dog类创建的每个实例都将存储名字和年龄。赋予了每条小狗蹲下（sit() ）和打滚（roll_over() ）的能力：

class Dog(): #1
    def __init__(self, name, age): #2
        self.name = name #3
        self.age = age

    def sit(self): #4
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

在#1处，定义了一个名为Dog的类，类名的首字母必须大写，后面跟圆括号。
类中的函数称为方法。#2处的方法__init__() 是一个特殊的方法。开头和末尾各有两个下划线，
这种约定避免Python默认方法与普通方法发生名称冲突。
将方法__init__() 定义成包含三个形参：self 、name 和age ，self 必不可少，
还必须位于其他形参的前面。Python调用这个__init__() 方法来创建Dog实例时，将自动传入实参self 。
每个与类相关联的方法调用都自动传递实参self ，因此不需要传递它。每当根据Dog 类创建实例时，
都只需给后两个形参（name 和age ）提供值。

在#3处定义两个变量都有前缀self 。以self为前缀的变量可供类中所有方法使用，
还可以通过类的任何实例来访问这些变量。self.name  = name 获取存储在形参name 中的值，
并将其存储到变量name 中，然后该变量被关联到当前创建的实例。self.age= age的作用与此类似。
像这样可通过实例访问的变量称为属性 。
Dog类还定义了另外两个方法：sit() 和roll_over() （在#4处）。

根据类创建实例：
创建一个表示特定小狗的实例：
class Dog(): #1
    (代码略)

my_dog = Dog('willie', 6) #5
print("My dog's name is " + my_dog.name.title() + ".")  #6
print("My dog is " + str(my_dog.age) + " years old.")  #7

在#5处，创建一条名字为'willie' 、年龄为6 的小狗。遇到这行代码时，Python使用实参'willie'
和6调用Dog 类中的方法__init__() 。方法__init__() 创建一个表示特定小狗的示例，并使用提供
的值来设置属性name 和age 。方法__init__() 并未显式地包含return语句，但Python自动返回一个
表示这条小狗的实例，将这个实例存储在变量my_dog中。这里的命名约定很有用：通常约定首字母大写的名称
（如Dog）指的是类，小写的名称（如my_dog）指的是根据类创建的实例。

访问属性：
在#6处，访问my_dog 的属性name的值：
my_dog.name
要访问实例的属性，可使用句点表示法，这种语法演示了Python如何获悉属性的值。在这里，
Python先找到实例my_dog ，再查找与这个实例相关联的属性name 。在Dog 类中引用这个属性时，
使用的是self.name 。在#7处，使用同样的方法来获取属性age 的值。
在前面的第1条print 语句中，my_dog.name.title() 将my_dog 的属性name 的
值'willie' 改为首字母大写的；在第2条print 语句中，str(my_dog.age) 将my_dog的属性age 的值6转换为字符串。运行结果如下：
My dog's name is Willie.
My dog is 6 years old.

调用方法：
根据Dog类创建实例后，就可以使用句点表示法来调用Dog 类中定义的任何方法。下面来让小狗蹲下和打滚：
class Dog(): #1
    (代码略)
my_dog = Dog('willie', 6) #5
my_dog.sit()
my_dog.roll_over()
要调用方法，可指定实例的名称（这里是my_dog ）和要调用的方法，并用句点分隔。
遇到代码my_dog.sit()时，Python在类Dog 中查找方法sit() 并运行其代码。
Python以同样的方式解读代码my_dog.roll_over() 。

创建多个实例：
创建一个表示特定小狗的实例：
class Dog(): #1
    (代码略)
my_dog = Dog('willie', 6) #5
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")  #6
print("My dog is " + str(my_dog.age) + " years old.")  #7
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

创建多个实例：
在这个实例中，创建了两条小狗，它们分别名为Willie和Lucy。每条小狗都是一个独立的实例，有自己的一组属性，能够执行相同的操作：

运行结果如下：
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.

'''


class Dog():  # 第一步写下类名
    def __init__(self, name, age, tall):  # 创建属性,参数不能直接在类内部传递
        self.name = name
        self.age = age
        self.tall = tall

    def pp(self):  # 创建第一个方法：显示方法
        print(self.name)
        print(self.age)
        print(self.tall)
        # print(name,age,tall)           #不能传递

    def zwjs(self):  # 创建第二个方法：自我介绍
        print('大家好，我的名字叫%s，我今年%s岁了，身高%s公分' % (self.name, self.age, self.tall))

    def dg(self):  # 创建第三个方法：打滚
        print('大家好，我的名字叫%s，我来给你们打个滚' % self.name)


import sys
import pygame

screen = pygame.display.set_mode((800, 600))  # 设置屏幕大小
pygame.display.set_caption('000')  # 设置标题
screen.fill('yellow')
while True:
    for event in pygame.event.get():  # 获取事件
        if event.type == pygame.QUIT:  # 如果点X退出
            sys.exit()
    pygame.draw.line(screen, 'black', (0, 0), (800, 600), 10)  # 画直线，画在哪，颜色，始末坐标，粗细
    pygame.display.update()  # 更新显示