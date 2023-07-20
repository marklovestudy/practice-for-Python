# # 用户input输入1234，请对这个字符进行格式化，要求有千分位
# # 字符长度20，用=号填充，字符在右边
# n=eval(input('n?'))
# print('{:=>20,}'.format(n))
#print('{0:=^20} {1:} {0:}'.format('ok','age',23))
#print('{a:} {b:_>10,} {c:}'.format(a='ok',c='age',b=1234))
#左边控制传值:右边控制格式化:
# 1:填充符一个字符位，2：位置<^>左中右
#3：字符长度  4千分位 5精度 6进制x16进制o八进制,b二进制
# 用户输入一个字符fdsafdadfdfs，
# 请输出这个字符的长度，用十六进制输出
# 这个十六进制居中，用*填充，格式后的长度为20
# n=len(input('str?'))
# print('{:*^20x}'.format(n))
# print(123,end='__')
# print(456)
#
# str1=input('请输入一个字符：')
# n=len(str1)
# if n%2==1:
#     print('奇数输出中间字符：',str1[int((n-1)/2)])
# else:
#     print('偶数输出最后一个字符：',str1[-1])
list1=list(input("输入一个字符串")[::2])
print(list1)