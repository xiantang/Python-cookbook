from  inspect import signature
from  functools import wraps


def typeasserat(*ty_args, **ty_kwargs):

    def decorate(func):
        if not __debug__:
            return func
        sig = signature(func)
        print(sig)
        #获取参数
        bound_type = sig.bind_partial(*ty_args,**ty_kwargs).arguments
        print(bound_type)

        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_values = sig.bind(*args,**kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_type:
                    if not isinstance(value,bound_type[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(
                                name,bound_type[name]
                            )
                        )
            return func(*args,**kwargs)
        return wrapper
    return decorate

@typeasserat(int,z=int)
def spam(x,y,z=42):
    print(x,y,z)


spam(1,2,3)
# spam(1, 'hello', 'world')
from  inspect import  signature
def spam(x,y,z=42):
    pass
sig = signature(spam)
print(sig)
print(sig.parameters)
print(sig.parameters['z'].name)
print(sig.parameters['z'].default)
print(sig.bind_partial(int,z=int).arguments)
#指定参数类型