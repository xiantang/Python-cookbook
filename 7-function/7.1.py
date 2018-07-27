def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    print(*args)
    print(x,args,y,kwargs)

b(1,2,3,4,y=1,a=3)