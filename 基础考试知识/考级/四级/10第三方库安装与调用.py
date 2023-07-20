'''
安装python第三方库的三种方法
    方法1：使用pip命令
    方法2：集成安装方法
    方法3：文件安装方法

一.pip命令安装方法(需要联网)：
    pip安装方法：使用python自带的pip安装工具进行第三方库安装，使用pip安装工具，需要
    打开操作提供提供的命令行，适合windows,Mac OS，和linux平台；
    pip -h查看这个命令的帮助信息
    python -m pip install --upgrade pip更新方法

常用的pip指令
    pip install <第三方库名> 安装指定的第三方库
    pip install --upgrade <第三方库名> 对已经安装的第三方库进行更新，使之到最新版本
    pip uninstall <第三方库名> 卸载指定的第三方库
    pip download <第三方库名> 下载但不安装指定的第三方库，作为后续的安装基础
    pip show <第三方库名> 列出指定第三方库的详细信息
    pip search <第三方库名> 根据关键词在名称和介绍中搜索第三方库
    pip list 列出当前系统已经安装的第三方库

二。第三方库的集成安装方法：
    Anaconda    www.anaconda.com
    -支持近800个第三方库    一次性装完
    -包含多个主流工具
    -适合数据计算领域开发

三。第三方库的文件安装方法：
    为什么有些第三方库用pip可以下载，但是无法安装？
    -这是因为某些第三方库提供的不是可执行文件，pip下载后，需要编译再安装
    -如果操作系统没有编译环境，只能下载但不能安装
    http://www.lfd.uci.edu/~gohlke/pythonlibs/          UCI页面
    -给出了一批在windows下经过编译在安装的第三方库的直接编译后的版本。
    例如安装jieba库

pip install arrow------时间 arrow 0.10.0
pip install bs4------BeautifulSoup4(4.6.0)      HTML解析器
pip install beautifulsoup4
pip install html5lib------html5解析器，BeautifulSoup要用到
pip install lxml------lxml4.1.0解析器，BeautifulSoup要用到
pip install cookies------cookies2.2.1
pip install Django------Django1.11.6网站
pip install flask------flask0.12.2网站
pip install jieba------jieba0.39中文分词，词频统计
pip install matplotlib------matplotlib2.1.0.2D绘图库
pip install numpy------numpy1.13.3开源的数值计算扩展。这种工具可用来存储和处理大型矩阵
pip install pdfkit------pdfkit0.6.1操作pdf
pip install pillow------pillow4.3.0由于PIL仅支持到python2.7，加上年久失修，于是一群志
愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新python 3.x，又加入了许多新特性，
因此，我们可以直接安装使用Pillow
pip install pymysql------pymysql0.7.10,
pip install pytesseract------pytesseract0.1.7,Tesseract-OCR(识别图像中的文字，还得
另外安装其它的。)
pip install pyquery------pyquery1.3.0数据库连接库，连接mysql的
pip install pymongo------pymongo3.5.1,数据库连接库，连接mongo的
pip install requests------requests2.18.4优雅，简单，人性化的HTTP库
pip install urllib3------urllib3 1.22
pip install wheel------wheel0.30.0
pip install wordcloud------wordcloud 1.3.1词云图
pip install xlrd------xlrd(1.1.0)读excel
pip install xlwt------xlwt(1.3.0)写excel
pip install setuptools------setuptools36.6.0
pip install pymouse------模拟鼠标操作
pip install PyAotuGUI------PyAotuGUI0.9.36,模拟鼠标键盘操作
pip install selenium------selenium3.3.1,selenium + python自动化测试环境搭建
pip install scrapy------这个安装比较麻烦，有很多依赖的库(主要是各种依赖装完了就好，Twisted、
vc++等)。最好弄个docker已经装好的镜像来做。
pip install cx_Oracle------cx_Oracle6.0.2 oracle数据库

本地安装whl文件：
    1、下载whl离线文件到本地，放到c盘根目录(任意位置均可，只是方便安装)
    https://pypi.org/
    https://www.lfd.uci.edu/~gohlk/pythonlibs/(推荐用这个地址下载whl文件，国内源，
    速度快。ctrl+f找到自己需要的文件)
    2、cmd到存放whl文件的目录
    3、pip安装whl离线文件
    pip install ****.whl
    (****.whl是我们下载的whl的文件名称)

本地安装exe文件：
.exe文件自定义安装
下载对应版本的exe安装文件，
如numpy-1.9.2-win32-superpack-python2.7exe和mlpy-3.5.0.win32-py2.7.exe
安装：打开exe文件，自动安装即可。
'''
