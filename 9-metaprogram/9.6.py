from  functools import wraps,partial
import logging

def logged(func=None,level=logging.DEBUG,name=None,message=None):
    if func is None:
        return partial(logged,level=level,name=name,message=message)
    logname = name if name else  func.__module__
    log = logging.getLogger(logname)
    logmag = message if message else func.__name__

    @wraps(func)
    def wrapper(*args,**kwargs):
        log.log(level,logmag)
        return func(*args,**kwargs)
    return  wrapper
#
# @logged()
# def add(x,y):
#     return x+y

# @logged(level=logging.CRITICAL,name='example')
def spam():
    print("Spam!")

spam = logged(level=logging.CRITICAL,name='example')(spam)
spam()



