from os import system
while 1:
    it=input('请输入：1关机，0取消关机，q退出循环')
    if it == '1':
        system('shutdown -s -t 120')
        print('120秒后关机')
    if it =='0':
        system('shutdown -a')
        print('取消关机')
    if it == 'q':
        print('退出程序')
        break
