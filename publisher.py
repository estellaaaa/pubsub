import socket

class Publisher:
    def __init__(self, broker):
        self.broker = broker

    def publish(self, message, topic):
        self.broker.delegate(message, topic)
        socket.create_connection(('127.0.0.1', 11341))