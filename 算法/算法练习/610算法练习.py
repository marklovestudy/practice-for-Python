#例6：10000以内
#有一盒乒乓球，9个9个的数最后余下7个，5个5个的数最后余下2个，4个4个的数最后余下1个。问这盒乒乓球到少有多少个？
#方法1：
# for i in range(7,10000):        #深挖
#     a_9 = i%9
#     a_5 = i%5
#     a_4 = i%4
#     if a_9 == 7 and a_5 == 2 and a_4 == 1:
#         print('这盒乒乓球最少有%s个'%i)

def maopaosort(l):
    sz=len(l)       #列表的长度，也就是有多少个元素
    #要多少轮，sz-1
    for i in range(sz-1):       #轮数
        for j in range(sz-1-i):       #每一轮的范围
            if l[j] > l[j+1]:           #前面的数大于后面的数，这时候就要交换位置
                l[j],l[j+1]=l[j+1],l[j]
import random as r
if __name__ == '__main__':
    # ls=[r.randint(0,100) for i in range(25)]
    # print('原列表：',ls)
    # maopaosort(ls)     #冒泡排序
    # print('排序后：',ls)
    # #请输入一个字符串，把字符串中的数字按大到小排列。如输入：'ads45632fds8..',输出：int类型：865432
    # str1=input("请输入一个字符串：")
    # #1提取数字加入列表
    # ls_str1=[]
    # for i in str1:
    #     if '0'<= i <= '9':
    #         ls_str1.append(i)
    # #2排序列表
    # maopaosort(ls_str1)
    # #3从大到小组合元素
    # str2=''.join(ls_str1[::-1])
    # print('输出int:',int(str2))
    #输入一个字符串，请统计这个字符串每个字符'a'---'z'出现的次数，不分大小写。其它统统为其它
    #如输入：'asdAA23**',输出：a=3,b=0,c=0,d=1,...s=1...z=0,其他=4
    #1创建一个列表，这个列表有27项。前26项为abcdef...z,27项为其他。全设置为0
    als=[0 for i in range(27)]
    #2统计每个字符属于列表的第几个索引，相应索引的值加1。
    str3=input('输入一个字符：').lower()       #"fdsa332"
    for i in str3:
        if 'a'<=i<='z':
            als[ord(i)-97]+=1
        else:
            als[26]+=1
    #3打印出这个列表的信息。
    for i in range(27):
        print("%s=%d"%(chr(97+i),als[i]),end=' ')