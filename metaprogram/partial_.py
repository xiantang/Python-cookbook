from functools import partial

def add(a,b):
    return a+b

plus = partial(add,100)

print(add(4,3))
print(plus(9))

def add2(a,b,c=2):
    return  a+b+c

plus3=partial(add,101)
print(plus3(1))