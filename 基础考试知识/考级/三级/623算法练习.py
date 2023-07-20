#甲乙丙丁，干了一坏事，是谁做了坏事呢。
#只有一个人说了真话。
#甲：是乙干的。1       xiaotou==2   真1  假0
#乙：是丁干的。2       xiaotou==4   真1  假0
#丙：不是我干的。3     xiaotou!=3   真1  假0
#丁：不是我。4        xiaotou!=4   真1  假0

# for xiaotou in range(1,5):
#     if (xiaotou==2)+(xiaotou==4)+(xiaotou!=3)+(xiaotou!=4) == 1:
#         print(xiaotou)

#输入一个字符串   输入："fd6fds3fd1"   输出：631
# str1=input("请输入一个字符串：")
# num=0       #int
# for i in str1:
#     if '0'<i<'9':       #str    #  '0'<i and i<'9'等价于'0'<i<'9'
#         i=int(i)
#         num=num*10+i
# print(num)

#输入一个浮点字符串   输入："5.6431"   输出：有4位小数
str1=input("输入一个浮点字符串:")
count=False
n=0
for i in str1:
    if count==True:
        n+=1
    if i =='.':
        count=True

print("有%d位小数"%n)