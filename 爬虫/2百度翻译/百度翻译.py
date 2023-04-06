import requests
import json
from tkinter import *
def findbd(words):
    #1创建访问对象及访问目的：1url,2关键字：kw,3UA伪装
    url='https://fanyi.baidu.com/sug'

    data={
        'kw':words
    }

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    #2发起请求POST
    response=requests.post(url=url,data=data,headers=headers)
    #3获取数据
    response=json.loads(response.text)
    # print(response,type(response))
    #4数据存储
    # filename=words+'.text'
    # with open(filename,'w',encoding='utf-8') as f:
    #     f.write(str(response))
    str1=''
    for i in response['data']:
        str1+=i['k']+':'+i['v']+'\n'
    return str1

def fy():
    what=e1.get()
    v=findbd(what)
    l1.config(text=v)
win=Tk()
win.title('百度翻译')
Label(win,text='查询内容').grid(row=0,column=0)
e1=Entry(win)
e1.grid(row=0,column=1)
Button(win,text='开始查询',command=fy).grid(row=0,column=2)
l1=Label(win,justify='left')
l1.grid(row=1,column=0,columnspan=3)
win.mainloop()
