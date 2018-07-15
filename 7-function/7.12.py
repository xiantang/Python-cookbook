def sample():
    n = 0
    def func():
        print('n=0',n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        #可以修改
        n = value