from queue import Queue
from threading import Thread
# _sentinel = object()
# def producer(out_q):
#     i = 0
#     while True:
#         i+=1
#         print("put data")
#         out_q.put("data")
#         if i==100:
#             out_q.put(_sentinel)
#         if out_q.qsize()>100:
#             break
# def consumer(in_q):
#     while True:
#         data = in_q.get()
#         print("get",data)
#         if data is _sentinel:
#             in_q.put(_sentinel)
#             break

# q = Queue()
# t1 = Thread(target=consumer,args=(q,))
# t2 = Thread(target=producer,args=(q,))
# t1.start()
# t2.start()

import heapq
import threading

# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._count =0
#         self._cv = threading.Condition()
#
#     def put(self,item,priority):
#         with self._cv:
#             heapq.heappush(self._queue,(-priority,
#                                         self._count,
#                                         item))
#     def get(self):
#         with self._cv:
#             with len(self._queue):
#                 self._cv.wait()
#             return heapq.heappop(self._queue)[-1]

# import time
# def producer(out_q):
#     runing = True
#     while runing:
#         data = "data"
#         time.sleep(1)
#         out_q.put(data)
#         print("put",data)
# def consumer(in_q):
#     while True:
#         data = in_q.get()
#
#         time.sleep(1)
#         print("get",data)
#         in_q.task_done()
#         #给对象发送信息 明确长度
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=producer, args=(q,))
# t1.start()
# t2.start()
# q.join()
# #队列为空 就执行其他操作 阻塞
# print("dddddd")
# from threading import Thread, Event
# data = 'data'
# import copy
# def producer(out_q):
#     running = True
#     while running:
#         evt = Event()
#
#         print("put",data)
#         out_q.put((copy.deepcopy(data),evt))
#         while not evt.is_set():
#             evt.wait(.1)#阻塞 等待
#         print('1111')
#
#
# def consumer(in_q):
#     while True:
#         data,evt = in_q.get()
#         import time
#         time.sleep(2)
#         print("get",data)
#         evt.set()#取消阻塞
#
# q = Queue()
# t1 = Thread(target=consumer,args=(q,))
# t2 = Thread(target=producer,args=(q,))
# t1.start()
# t2.start()
#向队列中添加数据项时并不会复制此数据项，
# 线程间通信实际上是在线程间传递对象引用


# q = Queue(10)
# def producer(q):
#
#     while True:
#         q.put("data", block=False)
# producer(q)

import queue

q = queue.Queue(1)
q.put(1)
q.put(1)#会阻塞
# data = q.get()#会阻塞

try :
    q.get(block=False)
except queue.Empty:
    print(111)

try:
    data = q.get(timeout=5.0)
except queue.Empty:
    ...

# q.qsize() ， q.full() ， q.empty() 不是线程安全