'''
概述：
    pyinstaller 是一个将 python 语言脚本（ py 文件）打包成可执行文件的第三方库，
    可用于 windows 、 Linux 、 Mac OS X 等操作系统。由于 pyinstaller 不支持
    原文件名中有英文句点存在，因此要避免。假设 dpython . py 文件在 D 盘的 codes
    目录中，则:\> pyinstaller d : \codes\dpython . py 执行完，原文件所在的
    目录将生成 dist 和 build 两个文件夹，其中 build 目录是存储临时文件的目录，可
    以删除。最终的打包程广在dist内部的目录中。目录中其他文件是可执行文件的动态链接库。


1pip install pyinstaller
可以通过﹣ F 参数对 python 源文件生成一个独立的可执行文件，代码如下：
\> pyinstaller -F d：\codes\dpython.py

1 pyinstaller相关参数
-F, –onefile | 打包一个单个文件，如果你的代码都写在一个.py文件的话，可以用这个，如果是多个.py文件就别用

-D, –onedir | 打包多个文件，在dist中生成很多依赖文件，适合以框架形式编写工具代码，我个人比较推荐这样，代码易于维护

-K, –tk | 在部署时包含 TCL/TK

-a, –ascii | 不包含编码.在支持Unicode的python版本上默认包含所有的编码.

-d, –debug | 产生debug版本的可执行文件

-w,–windowed,–noconsole | 使用Windows子系统执行.当程序启动的时候不会打开命令行(只对Windows有效)

-c,–nowindowed,–console | 使用控制台子系统执行(默认)(只对Windows有效)

| pyinstaller -c xxxx.py

| pyinstaller xxxx.py --console

-s,–strip | 可执行文件和共享库将run through strip.注意Cygwin的strip往往使普通的win32 Dll无法使用.

-X, –upx | 如果有UPX安装(执行Configure.py时检测),会压缩执行文件(Windows系统中的DLL也会)(参见note)

-o DIR, –out=DIR | 指定spec文件的生成目录,如果没有指定,而且当前目录是PyInstaller的根目录,会自动创建一个用于输出(spec和生成的可执行文件)的目录.如果没有指定,而当前目录不是PyInstaller的根目录,则会输出到当前的目录下.

-p DIR, –path=DIR | 设置导入路径(和使用PYTHONPATH效果相似).可以用路径分割符(Windows使用分号,Linux使用冒号)分割,指定多个目录.也可以使用多个-p参数来设置多个导入路径，让pyinstaller自己去找程序需要的资源

–icon=<FILE.ICO> | 将file.ico添加为可执行文件的资源(只对Windows系统有效)，改变程序的图标 pyinstaller -i ico路径 xxxxx.py

–icon=<FILE.EXE,N> | 将file.exe的第n个图标添加为可执行文件的资源(只对Windows系统有效)

-v FILE, –version=FILE | 将verfile作为可执行文件的版本资源(只对Windows系统有效)

-n NAME, –name=NAME | 可选的项目(产生的spec的)名字.如果省略,第一个脚本的主文件名将作为spec的名字

2 pyinstaller填坑总结
[在这里提醒大家，在代码里面尽量不要用import，能from…import…就尽量用这个，因为如果是import的话，在打包的时候，会将整个包都打包到exe里面，没有意义的增大了工具的大小！]

2.1、先下载pyinstaller，我比较懒，就直接用pip install pyinstaller，等待自动安装

2.2、在代码的路径下进行cmd，就直接跳转到该路径的cmd界面，切记路径中不要有中文

2.3、先用后台模式生成工具exe，命令为pyinstaller xxxx.py文件，主要目的是为了看报错信息，解决了报错后，再生成完整版的工具

tip：由于我的代码是存在依赖的，即多文件的，而非所有代码都在一个文件中的，所以我在这里没有使用-F，刚开始玩的时候不知道，老是用了-F生成了单文件的，没有生成依赖，老是不成功，各位朋友切记！

如果在日志中只有info信息的话，说明打包过程没有问题

2.4、找到生成的exe文件，运行exe（生成的exe文件都会在dist目录下）

运行时，我遇到了以下的报错信息，是在dist找到相关的图片资源，所以需要把所有关于工具所需的资源（包含图片以及依赖的.py文件都放进dist下的项目目录中）

2.5、再次运行exe，此时运行成功，说明工具打包成功

2.6、重新生成exe工具，去掉后台模式以及更换掉图标

给大家推荐一个图标获取地址，里面ico蛮多的：easyicon

下载了自己心仪的ico后，用-i+ico路径来替换默认ico，这次重新生成exe工具，命令为pyinstaller -i ico路径 -w xxxx.py
————————————————

'''
