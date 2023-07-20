
# 1、append()原来列表的最后添加元素
# li = [1,3,4,5]
# v = li.append(6)  #把6添加到列表li的最后一项*
# print(li)       #[1,3,4,5,6]
#
# 2、clear()清空列表
# li = [1,3,4,5]
# v = li.clear()
# print(li)           #[]
#
# 3、copy()浅拷贝
# li = [1,3,4,5]
# v = li.copy()
# print(v)
#
# 4、count()计算元素的数量
# li = [1,3,4,5]
# v = li.count(3)
# print(v)   #输出：1
#
# 5、extend()在列表后添加可迭代对象
# li = [1,3,4,5]
# v = li.extend([66,"mark"])#extend里面加可迭代对象，用的是for循环添加
# print(li)       #[1,3,4,5,66,"mark"]
# 注：
# for i in [66,"mark"]
#     li.append(i)
# #[1, 3, 4, 5, 66, 'mark']
#
# 6、index()根据值找到值的位置index()，从左开始找，找到一个就不向后面找了。
# li = [1,3,4,5,3]
# v = li.index(3)
# print(v)   #输出 1
#
# 7、 insert(2,66)在指定位置插入值。
# li = [1,3,4,5,3]
# v = li.insert(2,66)
# print(li)
#
# 8、pop()默认删除最后一个元素的值，并获取删除的值，如果指定索引，将删除索引的值，并获得这个值。
# li = [1,3,4,5,3]
# v = li.pop()
# print(li)
# print(v)
#
# 9、remove()删除指定值，左边优先
# li = [1,3,4,5,3]
# v = li.remove(3)  #不获得值
# print(li)    #[1, 4, 5, 3]
# print(v)
#
# 10、reverse()将当前列表翻转
# li = [1,3,4,5,3]
# v = li.reverse()
# print(li)
# print(v)
#
# 11、sort()排序，从小到大reverse = False    从大到小排reverse = True
# li = [1,3,4,5,3]
# v = li.sort(reverse=False)
# print(li)   #[1, 3, 3, 4, 5]
# print(v)

# import random as r
# scores=[r.randint(0,120) for i in range(50)]
# print(scores)
# min_score=min(scores)
# max_score=max(scores)
# sum_score=sum(scores)
# length=len(scores)
# av=sum_score/length
# print("最低分：{}最高分：{}平均分：{}".format(min_score,max_score,av))

# citys=['020广州','021上海','022天津','023重庆','024沈阳市','025南京']
# while True:
#     find=input("你要找的城市：000-999？")     #find='022'
#     for i in citys:
#         if find in i:               #'022' in '022天津'
#             print(i[3:])

# 假设10位评委的打分是99,80,86,89,94,92,75,87,86,95，
# 现需要运用Python语言进行编程实现：去掉一个最高分，去掉一个最低分，
# 计算平均分，并打印出来。打印格式为：去掉一个最高分：XX分，
# 去掉一个最低分：XX分，最后得分为：XX分
# 5获取序列属性：长度len(s),最小值min(s),最大值max(s),和sum(s)
# max_score=88
# print("最高分：",max_score)         #1
# print(f"最高分{max_score}")        #2  引用变量
# print("最高分：%s"%max_score)       #3占位符
# print("最高分：".format(max_score))     #4字符串格式化
scores=[99,80,86,89,94,92,75,87,86,95]
max_score=max(scores)
min_score=min(scores)
scores.remove(min_score)              #删除最小值
scores.remove(max_score)           #删除最大值
av=sum(scores)/len(scores)         #算平均分
print("max={},min={},av={}".format(max_score,min_score,av))

