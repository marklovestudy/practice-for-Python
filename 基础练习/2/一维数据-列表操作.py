# list1=[]
# for i in range(4):
#     city=input("请输入城市名：")
#     list1.append(city)          #末尾添加一个元素。
# #把这四个文件名写入文件存储起来。
# f=open("citys.csv",'w',encoding='utf-8')        #以写入的方式打开一个文件
# str1=','.join(list1)
# f.write(str1)
# f.close()
# f=open("citys.csv",'r',encoding='utf-8')        #以读的方式打开一个文件
# str2=f.read()                                   #读取文件内容
# print(str2)                                     #打印读取的内容
# f.close()
def pp():
    name = input("欢迎光临，请输入你的名字：")
    print("{}您好，祝您购物愉快".format(name))
    return name
def shop():
    ls=[]
    for i in range(eval(input("你要购买几件商品输入1-10："))):
        ls.append(input("输入商品名："))
    return ls
def save(name,ls):
    f=open("information.txt",'a+',encoding='utf-8')
    f.write("{}购买了:{}\n".format(name,ls))
    f.close()
    print('购物完毕。')
if __name__ == '__main__':
    name=pp()        #显示欢迎界面
    ls=shop()       #返回购买的货物
    save(name,ls)   #把购物信息存储起来
    print('欢迎下次光临。')