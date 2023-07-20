# import random as r
# with open('57.csv','w',encoding='utf-8') as f:
#     for i in range(1,4):
#         for j in range(1,6):
#             f.write('{},{},{}\n'.format(i,j,r.randint(60,100)))
import csv
with open('57.csv','r',encoding='utf-8') as f:
    print(list(csv.reader(f)))
