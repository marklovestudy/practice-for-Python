try:
    a=eval(input('a?'))
    b=eval(input('b?'))
    s=a/b
    print('result:',s)
except Exception as error:
    print(error)