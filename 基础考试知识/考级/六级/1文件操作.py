'''
概念：
按数据的组织形式可以把文件分为文本文件和二进制文件两大类。
    1文本文件存储的是常规字符串，由若干文本行组成，通常每行以换行符” \n ”结尾。常规字符串
    是指记事本之类的文本编辑器能正常显示、编辑并且人类能够直接阅读和理解的字符串，如英文字
    母、汉字、数字字符串。在 win 平台中扩展名为 txt 、 log 、 ini 都是文本文件，可以使
    用字处理软件如记事本等进行编辑。实际上文本文件在磁盘上也是以二进制形式存储的。只是在读
    取和查看时使用正确的编码方式进行解码，还原为字符串信息，所以可以直接阅读和理解。
    2二进制文件常见的如图形图像文件、音视频文件、可执行文件、资源文件、各种数据库文件、各
    类 office 文档等都属于二进制文件。二进制文件把信息以字节串进行存储，无法用记事本或其
    他普通字处理软件直接进行编辑，通常也无法直接阅读和理解，需要使用正确的软件进行解码或反
    序列化之后オ能正确地读取、显示、修改或执行。无法使用记事本查看，显示乱码。

操作：
    open ()方法：
    open ()方法用指定模式打开一个文件，并返回文件对象。
    使用 open ()方法一定要保证关闭文件对象，即调用 close ()方法， open ()函数常用形式
    是接收两个参数：文件名（ file ）和模式（ mode )。
    open ( file , mode = 'r')
    完整的语法格式为：
    open ( file , mode = 'r', buffering =1, encoding = None , errors = None ,
    newline = None , closefd = True , opener = None )
    file :必需，文件路径（相对或者绝对路径）。
    mode :可选，文件打开模式
    buffering :设置缓冲
    encoding ：一般使用utf8
    errors :报错级别
    newline :区分换行符
    closefd ：传入的 file 参数类型
    opener :设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
    默认为文本模式，如果要以二进制模式打开，加上 b

    mode 参数有：
    模式描述
    t   文本模式（默认)。
    w   写模式，新建一个文件，如果该文件已存在则会报错。
    b   二进制模式。
    +   打开一个文件进行更新（可读可写）。
    r   以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    rb  以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
    r+  打开一个文件用于读写。文件指针将会放在文件的开头。
    rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
    w   打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb  以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存衣
    创建新文件。一般用于非文本文件如图片等。
    w+  打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    wb+ 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创
    建新文件。一般用于非文本文件如图片等。
    a   打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，
    新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    ab  以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
    也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+  打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ab+ 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

操作： file 对象常用的函数:
    file.close ()，关闭文件。关闭后文件不能再进行读写操作。
    file.read ([size])，从文件读取指定的字符数，如size=10,读取前10个字符。如果未给定或为负则读取所有。
    file.readline ([size])，读取整行，包括" \n "字符。当有参数时，如size=3,表示读取此行的前3个字符。
    file.readlines([sizeint])，读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字符的行，
    实际读取值可能比sizeint较大，因为需要填充缓冲区。
    file.seek(offset[,whence])，移动文件读取指针到指定位置
    file.tell()，返回文件当前位置。
    file.write(str)，将字符串写入文件，返回的是写入的字符长度。
    file.writelines(sequence)，向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。
    v=f.writelines(['hao\n','ren\n','wo\n'])

操作： with 关键字：
    关键字 with 可以自动管理资源，不论因为什么原因，哪怕是代码引发了异常跳出 with 块，总能保证文件被正确关闭，
    可以在代码块执行完毕后自动还原进入该代码块时的上下文。用于文件内容读写时， with 语句的用法如下：
    with open(file,mode,encoding) as fp :
    ＃读写内容
例：
with open("test.txt","wt") as outfile:
    outfile.write ("该文本会写入到文件中＼n看到我了吧")
with open(" test.txt","rt") as in_file :
    text = in_file.read()
print(text)

实例1：
with open('IP.txt','r',encoding='utf-8') as f:
    list1 = f.readlines()
print(list1)
for i in range(0,len(list1)):
    list1[i] = list1[i].strip()
print(list1)
for i in range(len(list1)-1,-1,-1):
    print(list1[i])
f.close()

例2：
import csv
with open('sport.csv','r',encoding='utf-8') as f:
    rows = list(csv.reader(f))
    print(rows)
    s = 0
    c = 0
    for row in rows[1:]:
        s += eval(row[0])
        c = c + 1
print(round(s/c,3))     #第二个参数是保留几位小数的意思

例：20以内的加法
with open('ad20.csv','w',encoding='utf-8') as f:
    for i in range(11):
        for j in range(i,11):
            f.write('%s + %s = %s,'%(i,j,i+j))
        f.write('\n')

例3：
import csv
with open('subways.csv','r',encoding='utf-8') as f:
    rows = list(csv.reader(f))      #读出来的每行为这个列表的一个元素，并且每行都是一个列表元表，这个列表元表的元表是这行的每列信息。
    print(rows)
    s = 0
    for row in rows[1:]:
        if int(row[1]) >= 120:
            print(row[0])
'''
import csv
f=open('subways.csv','r+',encoding='utf-8')
f.seek(3)
v=f.writelines(['hao\n','ren\n','wo\n'])
rows = f.readlines()

print(rows,type(rows),v)
print(v)

