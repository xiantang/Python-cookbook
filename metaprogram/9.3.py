def time_this(func):

    # @wraps(func)
    def wrapper(*args,**kwargs):
        """
        Wrapper
        :param args:
        :param kwargs:
        :return:
        """
        import time
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
# orig_add=countdown.__wrapped__
# orig_add(100)


from  functools import wraps
