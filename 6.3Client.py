import sys
import socket

clientSocket = socket.socket()
host = '192.168.56.103'
port = 8888

print("Waiting for connection")
try:
    clientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

response = clientSocket.recv(1024)
print(response.decode())

while True:
    opt = input('Choose mathematical function, A -Logarithmic, B -Square Root, C -Exponential or Q to quit: ')

    if opt == 'A' or opt == 'B' or opt == 'C':
        value = input("Enter a value: ")
        opt = opt + ":" + value
        clientSocket.send(str.encode(opt))
        response = clientSocket.recv(1024)
        print(response.decode("utf-8"))

    elif opt == 'Q':
        print("Quiting app.")
        clientSocket.send(str.encode(option))
        sys.exit()
        
    else:
        print("Invalid input! Enter only A,B,C")
        print("Please try again.")
        opt = "0"
        clientSocket.send(str.encode(option))
        response = clientSocket.recv(1024)
        print('***********')

clientSocket.close()
