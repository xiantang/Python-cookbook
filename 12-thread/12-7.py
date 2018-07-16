from queue import Queue
from socket import AF_INET,SOCK_STREAM,socket
from concurrent.futures import ThreadPoolExecutor

# def echo_client(sock,client_addr):
#     print("get connection from",client_addr)
#     while True:
#         msg = sock.recv(65536)
#         if not msg:
#             break
#         sock.sendall(msg)
#     print('Client closed connection')
#
# def echo_server(addr):
#     pool = ThreadPoolExecutor(128)
#     sock = socket(AF_INET,SOCK_STREAM)
#     sock.bind(addr)
#     sock.listen(5)
#     while True:
#         client_sock,client_addr = sock.accept()
#         pool.submit(echo_client,client_sock,client_addr)
#
# echo_server(("",15000))
from threading import Thread


def echo_client(q):
    sock,client_addr = q.get()
    print("get connection from",client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()
def echo_server(addr,nworkers):
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client,args=(q,))
        t.daemon = True
        t.start()
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock,client_addr = sock.accept()
        q.put((client_sock,client_addr))

# echo_server(("",15000),128)

import urllib.request

def fech_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data
pool = ThreadPoolExecutor(10)
a = pool.submit(fech_url,'http://www.python.org')
b = pool.submit(fech_url,'http://www.pypy.org')
# print(type(a))
# print(type(b))
x=a.result()
y=b.result()
print(len(x))
print(len(y))