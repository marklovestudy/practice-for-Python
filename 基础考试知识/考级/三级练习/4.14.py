# f = open("41_4.csv","w")
# a = ["mark","dafei","weiwei"]
# for i in a:
#     f.write(",".join(i)+"\n")
# f.close()
# b = "look"
# print(b.center(90,"_"))
# f = open("41_4.csv","r")
# c = f.read().strip("\n").split(",")
# f.close()
# print(c)
c = [
    ["mark","38","173","67"],
    ["dafei","30","173","62"],
    ["weiwei","27","172","57"],
]
f = open("wenjian.csv", "w")
for i in c:
    f.write(",".join(i)+"\n")
f.close()
f = open("wenjian.csv", "r")
d = []
for i in f:
    d.append(i.strip("\n").split(","))
f.close()
print(d)
for i in d:
    line=""
    for j in i:
        line +='{:10}'.format(j)
    print(line)