import socket, threading, os

def recive():
    while True:
        x = c.recv(100).decode('utf-8')
        print("-" + x, end='')
        if(x == 'Good Bye\n'):
            c.close()
            print('Connection closed successfully')
            os._exit(0)

def send():
    while True:
        x = input()
        x += '\n'
        c.send(x.encode('utf-8'))
        if (x == 'Good Bye\n'):
            c.close()
            print('Connection closed successfully')
            os._exit(0)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket successfully created')
except socket.error as err:
    print("socket creation failed with error %s" %(err))
    exit(0)

port = 7000

s.bind(('', port))
print("socket binded to %s" %(port))

s.listen(5)
print('socket is listening...')

while True:
    c, addr = s.accept()
    print('Got connection from', addr)

    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=recive)


    t1.start()
    t2.start()

    t1.join()
    t2.join()
    c.close()
