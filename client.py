import socket, threading, os

def recive():
    while True:
        x = s.recv(100).decode('utf-8')
        print("-" + x, end='')
        if (x == 'Good Bye\n'):
            s.close()
            print('Connection closed successfully')
            os._exit(0)

def send():
    while True:
        x = input()
        x += '\n'
        s.send(x.encode('utf-8'))
        if (x == 'Good Bye\n'):
            s.close()
            print('Connection closed successfully')
            os._exit(0)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 7000
    s.connect(('localhost', port))
    print('Connected to server')

except ConnectionRefusedError:
    print("Can't Connect to Server")
    exit(0)

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recive)

t1.start()
t2.start()

t1.join()
t2.join()

