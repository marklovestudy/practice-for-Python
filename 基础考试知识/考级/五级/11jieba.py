'''
概述：
    jieba 库是一款优秀的 Python 第三方中文分词库， jieba 支持三
    种分词模式：精确模式、全模式和搜索引擎模式。
    精确模式：试图将语句最精确的切分，不存在冗余数据，适合
    做文本分析
    全模式：将语句中所有可能是词的词语都切分出来，速度很快，
    但是存在冗余数据
    搜索引擎模式：在精确模式的基础上，对长词再次进行切分

>>> import jieba
>>> s = '好好学习，天天向上。'
>>> '/'.join(jieba.lcut(s))
#精简模式，返回一个列表类型的结果
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\ADMINI~1\AppData\Local\Temp\jieba.cache
Loading model cost 1.110 seconds.
Prefix dict has been built successfully.
'好好学习/，/天天向上/。'
>>> '/'.join(jieba.lcut(s,cut_all=True))
#全模式，使用‘cut_all=True’指定
'好好/好好学/好好学习/好学/学习/，/天天/天天向上/向上/。'
'/'.join(jieba.lcut_for_search(s))
#搜索引擎模式
'好好/好学/学习/好好学/好好学习/，/天天/向上/天天向上/。'

用法：
    jieba.cut 方法接受三个输入参数：需要分词的字符串； cut_all 参数用来控
    制是否采用全模式。
    jieba.cut_for_search 方法适合用于搜索引擎构建倒排索引的分词
    待分词的字符串可以是 unicode 或 UTF-8字符串、GBK 字符串。
    注意：不建议直接输入GBK字符串，可能无法预料地错误解码成UTF-8
    jieba.cut 以及 jieba.cut_for_search返回的结构都是一个可迭代的
    generator，可以使用for循环来获得分词后得到的每一个词语(unicode)
    jieba.lcut以及jieba.lcut_for_search直接返回list

jieba 库的基本使用：
jieba 库常用函数：
jieba 库分词的三种模式：
    1、精准模式：把文本精准地分开，不存在冗余
    2、全模式：把文中所有可能的词语都扫描出来，存在冗余
    3、搜索引擎模式：在精准模式的基础上，再次对长词进行切分

1,jieba.cut(s)       精确模式，返回一个可迭代的数据类型
2,jieba.cut(s,cut_all=True)     全模式，输出文本s中所有可能单词
3，jieba.cut_for_search(s)        搜索引擎模式，适合搜索引擎建立索引的分词结果
4，jieba.lcut(s)                  精确模式，返回一个列表类型，建议使用
5,jieba.lcut(s,cut_all=True)     全模式，返回一个列表类型，建议使用
6,jieba.lcut_for_search(s)       搜索引擎模式，返回一个列表，建议使用
7,jieba.add_word(w)              向分词词典中增加新词w

例：
>>> jieba.lcut('中国是一个伟大的国家')
['中国', '是', '一个', '伟大', '的', '国家']
>>> jieba.lcut('中国是一个伟大的国家',cut_all = True)
['中国', '国是', '一个', '伟大', '的', '国家']
>>> jieba.lcut_for_search('中国是一个伟大的国家')
['中国', '是', '一个', '伟大', '的', '国家']

 ssn=jieba.lcut('会议费开支范围包括会议住宿费、伙食费、会议室租金、交通费、文件印刷费、医药费等。前款所称交通费是指用于会议代表接送站，以及会议统一组织的代表考察、调研等发生的交通支出。会议代表参加会议发生的城市间交通费，按照差旅费管理办法的规定回单位报销。')
>>> ssn
['会议费', '开支', '范围', '包括', '会议', '住宿费', '、', '伙食费', '、', '会议室', '租金', '、', '交通费', '、', '文件', '印刷', '费', '、', '医药费', '等', '。', '前款', '所', '称', '交通费', '是', '指', '用于', '会议', '代表', '接送', '站', '，', '以及', '会议', '统一', '组织', '的', '代表', '考察', '、', '调研', '等', '发生', '的', '交通', '支出', '。', '会议', '代表', '参加', '会议', '发生', '的', '城市', '间', '交通费', '，', '按照', '差旅费', '管理', '办法', '的', '规定', '回', '单位', '报销', '。']
>>> ssn1 = set(ssn)
>>> for i in ssn1:
	s=ssn.count(i)
	print(i,'......',s)


参加 ...... 1
规定 ...... 1
开支 ...... 1
的 ...... 4
单位 ...... 1
等 ...... 2
、 ...... 6
会议费 ...... 1
城市 ...... 1
是 ...... 1
。 ...... 3
称 ...... 1
组织 ...... 1
发生 ...... 2
办法 ...... 1
回 ...... 1
会议 ...... 5
间 ...... 1
住宿费 ...... 1
租金 ...... 1
报销 ...... 1
以及 ...... 1
接送 ...... 1
管理 ...... 1
费 ...... 1
包括 ...... 1
范围 ...... 1
指 ...... 1
医药费 ...... 1
考察 ...... 1
用于 ...... 1
交通 ...... 1
前款 ...... 1
站 ...... 1
交通费 ...... 3
代表 ...... 3
文件 ...... 1
印刷 ...... 1
差旅费 ...... 1
所 ...... 1
按照 ...... 1
调研 ...... 1
会议室 ...... 1
支出 ...... 1
， ...... 2
伙食费 ...... 1
统一 ...... 1
'''
import jieba
print(jieba.lcut('中国是一个伟大的国家'))