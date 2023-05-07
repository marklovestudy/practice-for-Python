# #例3：查找100以内能被2整除的数
# def find_two(n):
#     ls=[]       #列表用来存放目标数据
#     for i in range(1,n+1):
#         if i%2 == 0 :        #判断是否被2整除
#             ls.append(i)    #添加目标数据到ls列表中
#     return ls          #返回列表
#
# def main():
#     print('请查找100以内的被2整除的数')
#     ret=find_two(100)   #用来查找100以内被2整除的数
#     print(f'您查找的结果是:{ret}')
#
# if __name__ == '__main__':
#     main()

#例3：查找100以内能被2和3整除的数
# def find_two(n):
#     ls=[]       #列表用来存放目标数据
#     for i in range(1,n+1):
#         if i%2 ==0 and i%3==0 :        #判断是否被2整除
#             ls.append(i)    #添加目标数据到ls列表中
#     return ls          #返回列表
#
# def main():
#     print('请查找100以内的被2和3整除的数')
#     ret=find_two(100)   #用来查找100以内被2整除的数
#     print(f'您查找的结果是:{ret}')
#
# if __name__ == '__main__':
#     main()

#例4：用枚举算法找出所有满足各位数字之和等于7的三位数
def find_goal(nums):
    ls=[]
    for i in nums:
        if i//100+i%100//10+i%10==7:
            ls.append(i)
    return ls

def main():
    print('用枚举算法找出所有满足各位数字之和等于7的三位数')
    nums=range(106,701)    #最小数为106,最大数为701
    ret=find_goal(nums)
    print(f'目标数据为{ret}')

if __name__ == '__main__':
    main()