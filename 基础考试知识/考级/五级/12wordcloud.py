'''
概述：
词云：将词语通过图形可视化的方式直观和艺术的展示出来。wordcloud是优秀的词云展示的第三方库，
它能够将一段文本变成一个词云。
基本使用：
    wordcloud 库把词云当作一个 WordCloud 对象，
    1.wordcloud. WordCloud ()代表一个文本对应的词云
    2可以根据文本中词语出现的频率等参数绘制词云
    3．词云的绘制形状、尺寸和颜色都可以设定

wordcloud 库常规方法：
wordcloud 对具体词云的绘制的思路是
用 wordcloud 中的 WordCloud 来声明一个词云。以 WorldCloud 对象为基础。例如：
# >>> w = wordcloud . WordCloud ()
# >>> w . generate ( txt )＃向 WordCoud 对象 w 中加载文本 txt
# >>> w . to_file(filename)＃将词云输出为图像文件，png 或． jpg 格式

wordcloud库常规方法：
1，width ，指定词云对象生成图片的宽度，默认400像素
2，height ，指定词云对象生成图片的高度，默认200像素
3，min_font_size ，指定词云中字体的最小字号，默认4号
4,max_font_size ，指定词云中字体的最大字号，根据高度自动调节
5,font_step ，指定词云中字体字号的步进间隔，默认为1
6,font_path ，指定字体文件的路径，默认 None
7,max_words ，指定词云显示的最大单词数量，默认200
8,stop_words，指定词云的排除词列表，即不显示的单词列表
9,mask，指定词云形状，默认为长方形，需要引用imread()函数
10,backaround_color 指定词云图片的背景颜色，默认为黑色

import wordcloud
text = open('ABC.txt','r',encoding='utf-8').read()
w = wordcloud.WordCloud()
w.generate(text)
w.to_file('q.png')

from wordcloud import WordCloud
import matplotlib.pyplot as plt
f = open('ABC.txt','r').read()
wordcloud = WordCloud(background_color='white',width=1000,height=860,margin=2).generate(f)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
path_txt = 'ABC.txt'
f = open(path_txt,'r',encoding='utf-8').read()
cut_text = ' '.join(jieba.cut(f))
#需要设置路径，不然会出现口字乱码，文字的路径是电脑的字体一般路径，可以换成别的
wordcloud = WordCloud(font_path = 'c:/Windows/Fonts/simfang.ttf',
                      background_color='white',width=1000,height=860,margin=2).generate(cut_text)
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
'''
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
f = open('ABC.txt','r',encoding='utf-8').read()
w = WordCloud(font_path = 'c:/Windows/Fonts/simfang.ttf',background_color='white',width=1000,height=860,margin=2)
txt = jieba.lcut(f,cut_all=True)
print(txt)
cut_text = ' '.join(txt)
print(cut_text)
plt.imshow(w.generate(cut_text))
plt.axis('off')
plt.show()