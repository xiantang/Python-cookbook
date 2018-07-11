from  functools import wraps

class A:
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print("Decorator 1")
            return func(*args,**kwargs)
        return wrapper
    @classmethod
    def decorator2(cls,func):
        wraps(func)
        def wrapper(*args,**kwargs):
            print("Decorator 2")
            return func(*args,**kwargs)
        return wrapper

a= A()
@a.decorator1
def spam():
    pass

@A.decorator2
def grok():
    pass

class Person:

    first_name = property()

    @first_name.getter
    def fist_name(self):
        return  self._first_name

    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Expected a string")
        self._first_name=value

class B(A):
    @A.decorator2
    def bar(self):
        pass
b=B()
b.bar()