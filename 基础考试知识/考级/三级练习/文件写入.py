# f=open("date.csv","w")
# a = ["dafei","weiwei","mark"]
# f.write(",".join(a)+"\n")
# f = open("date.csv","r")
# c = f.read().strip("\n").split(",")
# f.close()
# print(c)
#
# f = open("1.csv","w")
# a = "a good day"
# b = "what will you doing ?"
# c = "I'd like to read a book about life."
# f.write(" ".join(a)+"\n")
# f.write(" ".join(b)+"\n")
# f.write(" ".join(c)+"\n")
# f = open("1.csv","r")
# c = f.read().strip("\n").split(",")
# print(c)
# for i in c:
#     print(i)
# c = [
#     ["dafei","54","55","64","68"],
#     ["weiwei","53","59","60","68"],
#     ["mark","73","79","70","78"],
# ]
# f=open('date.csv','w',encoding='utf-8')
# for i in c:
#     for j in i:
#         f.write(j+',')
#     f.write('\n')
# f.close()

import random as r
f=open(r'C:\Users\Administrator\Desktop\720.doc','w',encoding='utf-8')
for i in range(1,5):
    f.write("第{}组练习\n".format(i))
    for j in range(5):
        f.write("{}+{}+{}=             {}+{}+{}=\n".format(r.randint(1,4),r.randint(1,3),r.randint(1,3),r.randint(1,4),r.randint(1,3),r.randint(1,3)))
    f.write("\n\n\n\n\n")
f.close()
