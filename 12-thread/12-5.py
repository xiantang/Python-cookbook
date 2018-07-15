import  threading
from contextlib import contextmanager

_local = threading.local()

@contextmanager
def acquire(*locks):
    locks = sorted(locks,key= lambda x:id(x))
    acquired = getattr(_local,'acquired',[])
    if acquired and (max(id(locks) for lock in acquired))>= id(locks[0]):
        raise  RuntimeError('Lock Order Violation')
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
            yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks)]

x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock,y_lock):
            print('1')


def thread_2():
    while True:
        with acquire(x_lock, y_lock):
            print('2')
# t1 = threading.Thread(target=thread_1)
# t2 = threading.Thread(target=thread_2)
# t1.daemon =True
# t2.daemon =True
# t1.start()
# t2.start()

def philosopher(left,right):
    while True:
        while acquire(left,right):
            print(threading.current_thread(),'eating')
#死锁 就是无法同时获取资源
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n], chopsticks[(n + 1) % NSTICKS]))
    t.start()