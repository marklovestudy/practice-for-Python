'''
概念：
SQLite是内嵌在Python中的轻量级、基于磁盘文件的数据库管理系统，不需要安装和配置服务器，支持使用SQL语句来访问数据库。
SQLite是一个开源的关系型数据库，具有零配置、自我包含、便于传输等优点。当多个线程同时访问同一个数据库并试图写入数据时，每一时刻只有一个线程可以写入数据。
关系型数据库的数据存放于多个二维表中，在表中，行称为记录(record)，列称为字段(field)，一个数据库中可以包含多个表。
访问和操作SQLite数据时，首先导入sqlite3模块(内置)，然后创建一个与数据库关联的Connection对象。例如:
import sqlite3   #导入模块
conn=sqlite3.connection('d:/test.db')  #连接数据库

SQLite数据库连接对象及表的SQL操作：
SQLite是Python的内置库，用import sqlite3引用后，访问SQLite数据库的步骤如下：
1.用connect()创建数据库连接对象conn。
2.若要对数据库进行创建新表、对表插入数据、修改及删除数据等操作，使用conn.execute()方法，使用conn.commit()提交。
3.若要查询数据，先使用conn.cursor()方法创建游标对象cur，再通过cur.execute()查询，然后调用cur.fetchone()、cur.fetchmany()、cur.fetchall()方法返回查询值。
4.最后关闭cur和conn对象。
用connect()函数可建立数据库文件的连接对象，比如conn。若不存在数据库文件则新建数据库(例：d:/test.db)。

SQLite数据库连接对象及表的SQL操作：
import sqlite3   #导入模块
conn=sqlite3.connection('d:/test.db')  #连接数据库
由于SQLite3并不是可视化呈现的，因此可以使用第三方工具协助管理数据库。如：SQLlit Expert软件。

成功创建数据库后，应在其中合理创建表。

建立数据库连接对象后，用数据库连接对象的execute()方法可执行SQL语句,对数据库及表实现创建、插入、修改、删除和查询操作。SQL语句大小写不敏感，可分行，关键字之间可使用空格。

例：根据如下图所示的数据结构，在D盘根目录下建立一个空数据库test.db。并按如图所示的表结构，创建学生基本情况表base。
名       类型          长度          小数点         允许空值（Null）
学号      TEXT        10              0                   主键1
姓名      TEXT        10              0
性别      TEXT        1               0
专业      TEXT        6               0           1
生源      TEXT        6               0           1
身高      INTEGEF     0               0           1
电话      TEXT        11              0           1


'''
"""
例1：根据如下图所示的数据结构，在D盘根目录下建立一个空数据库test.db。并按如图所示的表结构，创建学生基本情况表base。
import sqlite3   #导入模块
conn=sqlite3.connect('d:/test.db')  #连接数据库
conn.execute('''CREATE TABLE base
(学号  TEXT(10)  PRIMARY KEY    NOT NULL,
 姓名  TEXT(10)  NOT NULL,
 性别  TEXT(1)   NOT NULL,
 专业  TEXT(6),
 生源  TEXT(6),
 身高  INTEGER,
 电话  TEXT(6));''')

"""
"""
SQLite3表支持以下4种类型：**********
整数型(INTEGER)：有符号整数，按实际存储大小，自动存储为1、2、3、4、6或8字节，通常不需要指定位数。
实数型(REAL)：浮点数，以8字节指数形式存储。可指总位数和小数位数.
文本型(TEXT)：字符串，以数据库编码方式存储(以UTF-8支持汉字)。
BLOB型：二进制对象数据，通常用来保存图片、视频、XML等数据。
创建表的SQL语句格式：
CREATE TABLE <表>(<字段元组>)
SQL语句大小写不敏感,但为与Python语言相区别，以大写表示。
设计表结构时，作为一种数据完整性约束，可指定某字段是否允许空，若不允许为空，可用NOT NULL关键字加以限制。
在大多数表中，往往会指定一个非空且唯一的字段作为关键主关键字(PRIMARY KEY，如学号)，便于快速检索，通常将表按主关键字建立索引。

创建表的SQL语句格式：**********
CREATE TABLE <表>(<字段元组>)
与数据库连接对象conn.execute()方法相关的常用SQL语句格式如下：
添加：
INSERT INTO <表>(<字段元组>)  VALUES (<数据元组>)
修改：
UPDATE <表> SET <字段>=<值>
删除：
DELETE  FROM <表>  WHERE <条件表达式>

例2：编写程序为例1创建的base表添加新生学号、姓名和性别三项非空数据。
import sqlite3   #导入模块
conn=sqlite3.connect('d:/test.db')  #连接数据库
while True:
    idd=input('请输入新生学号：(输入0退出程序)\n')
    if idd=="0":
        break
    name=input("请输入新生姓名：\n")
    gender=input("请输入新生性别：\n")
    #格式化构建SQL字符串
    SQL='''insert into base
(学号,姓名,性别)
values ('%s','%s','%s')'''%(idd,name,gender)
    #插入数据
    conn.execute(SQL)
    #提交事务
    conn.commit()
conn.close()

在格式化构建SQL字符串时应注意：values后面的数据元组应与前面的表达式字段元组顺序一致，且TEXT类型的数据要加单引号定界符。

例3：案例，小猫钓鱼
建立数据库表结构，添加一条记录
import sqlite3   #导入sqlite3模块
conn=sqlite3.connect('d:/fish.db')  #连接数据库
cur=conn.cursor() #通过建立数据库游标对象，准备读写操作
conn.execute('''create table fish1(date text,name text,nums int,price real,Explain text)''')
conn.execute("insert into fish1 values('2022-3-28','黑鱼',10,28.3,'张三')")
conn.commit()
conn.close()

例3：案例，小猫钓鱼
查询数据
import sqlite3   #导入sqlite3模块
conn=sqlite3.connect('d:/fish.db')  #连接数据库
cur=conn.cursor() #通过建立数据库游标对象，准备读写操作
cur.execute('select * from fish1')#对fish1表执行数据查找命令
for i in cur.fetchall():#以一条记录为元组单位返回结果给i
    print(i)
conn.close()
fetchone()从结果中取一条记录，并将游标指向下一条记录；
fetchmany()从结果中取多条记录；
fetchall()从结果中取出全部记录；
scroll()用于游标滚动；

例4：案例，小猫钓鱼
删除数据
import sqlite3   #导入sqlite3模块
conn=sqlite3.connect('d:/fish.db')  #连接数据库
cur=conn.cursor() #通过建立数据库游标对象，准备读写操作
conn.execute("insert into fish1 values('2022-3-29','鲤鱼',17,10.3,'李四')")
conn.execute("insert into fish1 values('2022-3-30','鲢鱼',9,9.3,'王五')")
conn.commit()#提交数据保存到磁盘
cur.execute('select * from fish1')
for i in cur.fetchall():
    print(i)
cur.execute("delete from fish1 where nums=10")
conn.commit()
cur.execute('select * from fish1')
for i in cur.fetchall():
    print(i)
conn.close()

"""
import sqlite3   #导入sqlite3模块
conn=sqlite3.connect('test.db')  #连接数据库
cur=conn.cursor() #通过建立数据库游标对象，准备读写操作
cur.execute('select * from base')#对fish1表执行数据查找命令
print(cur.fetchone())
conn.close()
