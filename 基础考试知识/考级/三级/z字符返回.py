import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.1.7', 1234))
    while 1:
        data = bytes(input(), encoding='utf-8')
        s.sendall(data)
        data = s.recv(1024)
        print('Re: ', data.decode('utf-8'))

