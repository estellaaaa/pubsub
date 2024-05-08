import socket

HOST = '127.0.0.1'
PORT = 11341

class Broker:
    def __init__(self):
        self.subs = {}
        #socket.create_server((HOST, PORT)).listen()

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