# class Spam:
#     def __init__(self,name):
#         self.name = name
# a = Spam('Guido')
# b = Spam('Diana')

# class NoInstance(type):
#     def __call__(self, *args, **kwargs):
#         raise  TypeError("Can't instantiate directly")
# class Spam(metaclass=NoInstance):
#     @staticmethod
#     def grok(x):
#         print("Spam.grok")
#
# Spam.grok(42)
# s = Spam()

# class Singleton(type):
#     def __init__(self,*args,**kwargs):
#         self.__instance = None
#         super().__init__(*args,**kwargs)
#
#     def __call__(self, *args, **kwargs):
#         if self.__instance is None:
#             self.__instance = super().__call__(*args,**kwargs)
#             return self.__instance
#         else:
#             return self.__instance
# class Spam(metaclass=Singleton):
#
#     def __init__(self):
#         print("Creating Spam")
#
# a = Spam()
# b = Spam()
# print(a is b)

import weakref

class Cached(type):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

class Spam(metaclass=Cached):
    def __init__(self, name):
        print("Creating Spam({!r})".format(name))
        self.name = name


spam = Cached("Spam",(),{"name" : "aaa"})()
# print(spam.name)
a = Spam('Guido')
b = Spam('Diana')
c = Spam('Guido')
print(a is c)