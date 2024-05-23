import socket

broker_host = '127.0.0.1'
broker_port = 11343

class Broker:
    def __init__(self):
        # self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server.bind((HOST, PORT))
        # self.server.listen(10)
        with socket.create_server((broker_host, broker_port)) as server:
            print(f"Server listening on {broker_host}:{broker_port}")
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
