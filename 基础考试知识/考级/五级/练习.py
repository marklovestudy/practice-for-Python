import wordcloud
import jieba
str1='天天学习，好好学习，努力向上，成绩优异，三好学生'
str2=','.join(jieba.lcut(str1,cut_all=True))
wd=wordcloud.WordCloud(width=400,height=400,font_path='c:/Windows/Fonts/simfang.ttf')
wd.generate(str2)
wd.to_file('tp.png')
