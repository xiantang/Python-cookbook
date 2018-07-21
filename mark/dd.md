### 给函数添加包装

```
import time
from  functools import wraps

def timethis(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,end-start)
        return  result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -=1
```

装饰器其实是很简单的
不过就是传入一个函数 然后返回一个函数
Python的语法糖可能看起来比较麻烦
我们可以这样写

```
func=timethis(countdown)
func(100000)
```
这样就很简洁明了了
首先返回一个处理后的func对象
然后调用他

### 在创建装饰器的时候保留函数的元数据

```
def time_this(func):
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
```
如果我们不去保留传入函数的元数据的话
```
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
wrapper

        Wrapper
        :param args:
        :param kwargs:
        :return:

{}
```
返回的会是上个函数的包装的信息
我靠 ！ 这就很难受了
我想看到里面的东西！
怎么办！
python引入了wraps这个装饰器
我们只要把需要包装的函数作为参数传入就行啦
`@wraps(func)`

```
def time_this(func):
    @wraps(func)
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
```
我们来看下输出把

```
countdown 0.2415015697479248
countdown

    Counts down
    :param n:
    :return:

{}
```

### 解除装饰器

```
@time_this
def countdown(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n>0:
        n-=1
        print(n)
orig_add=countdown.__wrapped__
orig_add(100)
```
如果有多个包装器，那么访问 `__wrapped__` 属性的行为是不可预知的，应该避免这样做。

### 给装饰器传入参数

```
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
```
