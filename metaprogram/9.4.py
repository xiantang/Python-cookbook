from  functools import  wraps
import logging

def logged(level,name=None,message=None):
    def decorate(func):
        logname=name if name else func.__module__
        log=logging.getLogger(logname)
        logmsg=message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logmsg)
            return func(*args,**kwargs)
        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x,y):
    return  x+y


@logged(logging.CRITICAL,'example')
def spam():
    print("Spam!")


print(add(1,2))
spam()

def bbb(c):

    def log(func):

        def wrapper(*args):
            print(c)
            print(*args)#1 1 1
            print(args)#(1, 1, 1)
            import time
            start=time.time()
            func(*args)
            end=time.time()
            print(end-start)
        return wrapper
    return log

# @bbb(100)
def a(a,b,c):
    print(a)
    print(b)
    print(c)
    print("1")

# a(1,1,1)
bbb(1)(a)(1,1,1)