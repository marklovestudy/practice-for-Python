'''
1输入一个字符串。
2判断是不是以a开头，是不是以z结尾。
3如果是：输入是的。如果不是，输出不是

10-11、endswith()、startswith()           7分(0-10分为重要程度)
name = "markmarkmark"
v1 = name.endswith("ar",0,8)#7、endswith(self, suffix, start=None, end=None)是否以“ar”结束。
print(v1)       #输出：False
v2 = name.startswith("ma",0,8)#8、startswith(self, prefix, start=None, end=None)是否以“ma”开始
print(v2)       #输出：True
'''
while True:
    str1=input("请输入一个字符串")
    re=str1.startswith('a')
    if re:
        print('是以a开头')
    else:
        print('不是以a开头')
    re = str1.endswith('z')
    if re:
        print('是以z结尾')
    else:
        print('不是以z结尾')
