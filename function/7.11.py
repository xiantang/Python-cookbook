def apply_async(func,args,*,callback):
    # print(args)
    # print(*args) #解包
    result = func(*args)

    callback(result)
from queue import Queue
from functools import wraps
class Async:
    def __init__(self,func, args):
        self.func = func
        self.args = args

def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        #去遍历 生成器
        while True:
            result = result_queue.get()
            try:
                # print(result)
                #send 传递yield表达式的值

                a = f.send(result)

                apply_async(
                    a.func,
                    a.args,
                    callback=result_queue.put
                )
            except StopIteration:
                break
    return wrapper

def add(x,y):
    return x+y
@inlined_async
def test():
    r = yield Async(add,(2,3))
    print(r)
    r = yield Async(add,('hello','world'))
    print(r)
    for n in range(10000):
        r = yield Async(add,(n,n))
        print(r)
    print('Goodbye')
if __name__ == '__main__':
    # import multiprocessing
    #
    # pool = multiprocessing.Pool()
    # apply_async = pool.apply_async
    test()