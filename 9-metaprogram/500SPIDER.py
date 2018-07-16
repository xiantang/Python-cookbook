import socket
# url="xkcd.com"
# request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
# encoded = request.encode('ascii')
# sock = socket.socket()
# while True:
#     try:
#         sock.send(encoded)
#         break  # Done.
#     except OSError as e:
#         pass


from  selectors import DefaultSelector,EVENT_WRITE,EVENT_READ

selector = DefaultSelector()
#
# sock = socket.socket()
# sock.setblocking(False)
# try:
#     sock.connect(("xkcd.com",80))
# except BlockingIOError:
#     pass
#
#
# def connected():
#     selector.unregister(sock.fileno())
#     print('connected!')
#
# selector.register(sock.fileno(),EVENT_WRITE,connected)
#
# def loop():
#     while True:
#         events = selector.select()
#         for event_key, event_mask in events:
#             callback = event_key.data
#             callback()
# loop()
import asyncio
urls_todo=set(['/'])
seen_url=set(['/'])

class Fetcher:

    def __init__(self,url):
        self.response=b''
        self.url= url
        self.sock=None

    @asyncio.coroutine
    def fetch(self):
        response = yield from self.session.get(url)

    def connected(self,key,mask):
        print("connected!")
        selector.unregister(key.fd)
        request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(self.url)
        self.sock.send(request.encode('ascii'))

        selector.register(key.fd,EVENT_READ,self.read_response)

    def parse_links(self):
        print(self.response)

    def read_response(self,key,mask):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response+=chunk
        else:
            selector.unregister(key.fd)
            links = self.parse_links()

            for link in links.difference(seen_url):
                urls_todo.add(link)
                Fetcher(link).fetch()

            seen_url.update(links)
            urls_todo.remove(self.url)
            if not  urls_todo:
                stopped =True

stopped = False

def loop():
    while not stopped:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

fetcher = Fetcher('/353/')
fetcher.fetch()

while True:
    events = selector.select()
    for event_key, event_mask in events:
        callback = event_key.data
        callback(event_key,event_mask)
