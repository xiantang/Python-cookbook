import time
from  functools import  wraps

def time_this(func):

    # @wraps(func)
    def wrapper(*args,**kwargs):
        """
        Wrapper
        :param args:
        :param kwargs:
        :return:
        """
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return result
    return wrapper

@time_this
def countdown(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n>0:
        n-=1

countdown(1111111)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)