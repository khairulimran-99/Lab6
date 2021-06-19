import math
import socket
import sys
import time
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 Not Found\n\n'


def process_start(s_sock):
    s_sock.send(str.encode("CONNECTED TO SERVER !!!\n"))
    while True:
        msg = s_sock.recv(2048).decode("utf-8").split(":")

        if msg[0] == "A":
            result = math.log(float(msg[1]))
        elif msg[0] == "B":
            result = math.sqrt(float(msg[1]))
        elif msg[0] == "C":
            result = math.exp(float(msg[1]))
        elif msg[0] not in 'ABC':
            result = math.exp(float(0))
        elif msg[0] == "Q":
            break

        s_sock.sendall(str.encode(str(result)))
    s_sock.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8888))
    print("Listening...")
    s.listen(3)

try:
    while True:
      try:
        s_sock,s_addr = s.accept()
        print ("\nConnection from : ", s_addr)
        p = Process(target = process_start,args = (s_sock,))
        p.start()

      except socket.error:
        print('got a socket error')

except Exception as e:
    print('an exception occured!')
    print(e)
