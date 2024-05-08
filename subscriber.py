import socket

class Subscriber:
    def __init__(self, broker_addr, HOST, PORT):
        self.server = socket.create_server((HOST, PORT))
        self.broker_addr = broker_addr

    def subscribe(self, topic, callback):
        with socket.create_connection(self.broker_addr) as connection:
            connection.sendall(topic.encode())

    def receive(self, message):
        print(self, message)