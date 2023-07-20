'''
1请输入一个整数，（input()）
2请编写一道程序，计算这个数转成二进数后，包含多少个1。
'''

# 方法1
num=eval(input('请输入一个整数。'))
num_bin=bin(num)[2:]
count=0
for i in num_bin:
    if i == '1':
       count+=1
print('{}转成二进制数是{}共有{}个1'.format(num,num_bin,count))
#方法2   字符串方法
# num=eval(input('请输入一个整数。'))
# num_bin=bin(num)[2:]
# count=num_bin.count('1')
# print('{}转成二进制数是{}共有{}个1'.format(num,num_bin,count))

#方法3    取余法
# num=eval(input('请输入一个整数。'))
# text_num=num
# count=0
# while text_num:
#     if text_num%2==1:
#         count+=1
#     text_num=text_num//2    #int(num/2)
# print('{}转成二进制数后共有{}个1'.format(num,count))

#方法4   位移法
# num=eval(input('请输入一个整数。'))
# text_num=num
# count=0
# while text_num:
#     if text_num%2==1:
#         count+=1
#     text_num >>=1
# print('{}转成二进制数后共有{}个1'.format(num,count))

#方法5    位与   位或    位异或
# num=eval(input('请输入一个整数。'))
# text_num=num
# count=0
# while text_num:
#     if text_num&1==1:
#         count+=1
#     text_num >>=1
# print('{}转成二进制数后共有{}个1'.format(num,count))


