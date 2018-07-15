from socket import socket, AF_INET,SOCK_STREAM
import threading
class LazyConnection:
    def __init__(self, address,family=AF_INET,type=SOCK_STREAM):
        