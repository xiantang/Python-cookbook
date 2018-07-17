from collections import defaultdict

class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self,task):
        self._subscribers.add(task)

    def detach(self,task):
        self._subscribers.remove(task)

    def send(self,msg):
        for subcriber in self._subscribers:
            subcriber.send(msg)

_exchanges = defaultdict(Exchange)

def get_exchange(name):
    return _exchanges[name]

class Task:
    def send(self,msg):
        print(msg)

# task_a = Task()
# task_b = Task()
#
# exc = get_exchange('name')
# exc.attach(task=task_a)
# exc.attach(task=task_b)
# # exc.attach(task=task_b)
# # exc.send('msg1')
# # exc.send('msg2')
# exc.detach(task_a)
# exc.detach(task_b)
# exc.send('msg1')

class DisplayMessages:
    def __init__(self):
        self.count = 0

    def send(self,msg):
        self.count += 1
        print('msg[{}]:{!r}'.format(self.count,msg))
exc = get_exchange('name')
d = DisplayMessages()
exc.attach(d)