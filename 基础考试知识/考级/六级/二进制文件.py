# f=open('ball.png','rb')  #来源文件
# v=f.read()
# fo=open('pic1.png','wb')     #目标文件
# fo.write(v)
# fo.close()
# f.close()
# with open('vi.csv','r',encoding='utf-8') as f:
#     print(f.read())
# str1='李先生, 语文组, 33, 否\n王先生, 数学组, 28, 是'
# fo =open('sut.csv','w',encoding='utf-8')
# fo.write(str1)
# fo.close()
# list1=[
#     [123654,'张三',65,45,76,78,65,34,32],
#     [123424,'李四',85,45,96,48,68,74,72],
#     [165454,'王五',95,75,96,58,85,64,42],
# ]
# fo=open('students.csv','w',encoding='utf-8')
# for i in list1:
#     for j in i:
#         fo.write(str(j)+',')
#     fo.write('\n')
# fo.close()
# f=open('students.csv','r',encoding='utf-8')
# ls1=f.read().strip().split('\n')
# ls=[]
# for i in ls1:
#     ls2=i.strip(',').split(',')
#     for j in range(9):
#         if j==1:
#             pass
#         else:
#             ls2[j]=eval(ls2[j])
#     ls.append(ls2)
# print(ls)
# fo=open('s1.txt','w',encoding='utf-8')
# import random as r
# for i in range(10000):
#     fo.write(str(r.randint(100000,999999))+','+chr(r.randint(20000,40000))+chr(r.randint(20000,40000))+',')
#     for j in range(7):
#         fo.write(str(r.randint(0,100))+',')
#     fo.write('\n')
# fo.close()
# f=open('s1.txt','r',encoding='utf-8')
# print(f.readlines())            #read(),     readline()     readlines()
f=open('s1.txt','r',encoding='utf-8')
ls=f.readlines()
d={}
for i in ls:
    ls1=i.strip().strip(',').split(',')
    k=ls1[1]
    v=eval('+'.join(ls1[2:]))
    d[k]=v
    # for j in ls[2:]:
    #     d[k]=d.get(k,0)+eval(j)
lt=list(d.items())
lt.sort(key=lambda x:x[1],reverse=True)
fo=open('studens_up.txt','w',encoding='utf-8')
for i in range(5000):
    fo.write('{}:{}'.format(lt[i][0],lt[i][1]))
fo.close()