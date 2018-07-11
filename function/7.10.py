def apply_async(func,args,*,callback):
    print(args)
    print(*args) #解包
    result = func(*args)

    callback(result)
#
def add(x,y):
    return x+y
#
# def print_result(result):
#     print('Got:',result)
#
# apply_async(add,(2,3),callback=print_result)

class ResultHandlter:
    def __init__(self):
        self.sequence = 0

    def handlter(self, result):
        self.sequence += 1
        print(
            '[{}] Get: {}'.format(self.sequence,
                                  result)
        )
# r = ResultHandlter()
# apply_async(add,(2,3),callback=r.handlter)
# apply_async(add, ('hello', 'world'), callback=r.handlter)

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence +=1
        print('[{}] Got: {}'.format(sequence,result))
    return handler
#
# handler = make_handler()
# apply_async(add,
#             (2,3),
#             callback=handler)
# apply_async(add,('hello','world'),callback=handler)
# apply_async(add,(1,2),callback=handler)

def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got {}'.format(sequence,
                                   result))

handler =make_handler()
next(handler)
apply_async(add,(2,3),callback=handler.send)
apply_async(add,('hello','world'),callback=handler.send)