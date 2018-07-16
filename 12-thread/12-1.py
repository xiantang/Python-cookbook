import time
def countdown(n):
    while n>0:
        print('T-minus',n)
        n -= 1
        time.sleep(5)
from  threading import Thread
# t = Thread(target=countdown,args=(10,),daemon=True)
# t.start()
# t.join()#加入到当前线程

# if t.is_alive():
#     print("Still running")
# else:
#     print("completed")

class CountdownTask:
    def __init__(self):
        self._running  =  True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n>0:
            print("T-minus",n)
            n-=1
            time.sleep(5)

# c = CountdownTask()
# t = Thread(target=c.run,args=(10,))
# t.start()
# time.sleep(10)
# c.terminate()
# t.join()

class IOTask:
    def __init__(self):
        self.running = True

    def terminate(self):
        self.running = False

    def run(self):
        while self.running:
            try:
                time.sleep(1)
                print("aaaaaa")
            except Exception as e:
                print(e)
# io = IOTask()
# t = Thread(target=io.run, args=())
# t.start()
#
# io.terminate()
# t.join()

class CountDownThread(Thread):
    def __init__(self,n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n>0:
            print('T-minus',self.n)
            self.n -=1
            time.sleep(5)
c = CountDownThread(5)
c.start()