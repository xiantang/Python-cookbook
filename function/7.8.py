# def spam(a,b,c,d):
#     print(a,b,c,d)
#
# from functools import partial
#
# s1 = partial(spam,1)
# s1(2,3,4)
#
# s2 = partial(spam,d=42)
# s2(1,2,3)
#
# s2(4,5,5)
#
# points = [(1, 2), (3, 4), (5, 6), (7, 8) ]
#
# import math
#
# def distance(p1,p2):
#     x1, y1=p1
#     x2, y2=p2
#     return math.hypot(x2-x1,y2-y1)
#
# pt = (4,3)
# points.sort(key=partial(distance,pt))
# print(points)

# def output_result(result,log=None):
#     if log is not None:
#         log.debug('Got: %r', result)
#
# def add(x,y):
#     return x+y
#
# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial
#
#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')
#
#     p = Pool()
#     p.apply_async(add,(3,4),callback=partial(
#         output_result,log=log
#     ))
#     p.close()
#     p.join()


###################################

from socketserver import StreamRequestHandler, TCPServer

# class EchoHandler(StreamRequestHandler):
#     def handle(self):
#         for line in  self.rfile:
#             self.wfile.write(b'GOT:'+line)
#
# serv = TCPServer(("",15000),EchoHandler)
# serv.serve_forever()

class EchoHandler(StreamRequestHandler):

    def __init__(self,*args,ack,**kwargs):
        self.ack = ack
        super().__init__(*args,**kwargs)

    def handle(self):
        for line in self.rfile:
            self.wfile.write(self.ack+line)