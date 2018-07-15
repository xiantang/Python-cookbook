import threading

# class SharedCounter:
#
#     def __init__(self,initial_value = 0):
#         self._value = initial_value
#         self._value_lock = threading.Lock()
#
#     def incr(self,delta):
#         with self._value_lock:
#             self._value += delta
#
#     def decr(self,delta):
#         with self._value_lock:
#             self._value -= delta

# class SharedCounter:
#     _lock = threading.RLock()
#     def __init__(self,initial_value = 0):
#         self._value = initial_value
#
#     def incr(self,delta=1):
#         with SharedCounter._lock:
#             self._value +=delta
#
#     def decr(self,delta=1):
#         with SharedCounter._lock:
#             self._value -=delta


from threading import Semaphore
import urllib.request


_fetch_url_sema = Semaphore(5)

def fetch_url(url):
    with _fetch_url_sema:
        return urllib.request.urlopen(url)

fetch_url("https://www.baidu.com")

