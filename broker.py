import socket

HOST = '127.0.0.1'
PORT = 11341

class Broker:
    def __init__(self):
        # self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server.bind((HOST, PORT))
        # self.server.listen(10)
        with socket.create_server((HOST, PORT)) as server:
            print(f"Server listening on {HOST}:{PORT}")
            self.conn, self.addr = server.accept()
            print(f"Connected by {self.addr}")
        self.subs = {}

    def register(self, callback, topic):
        try:
            topic = self.subs[topic]
            topic.append(callback)
        except KeyError:
            self.subs[topic] = [callback]

    def delegate(self, message, topic):
        try:
            callbacks = self.subs[topic]
        except KeyError:
            return
        for call in callbacks:
            call(message)

#broker = Broker()
