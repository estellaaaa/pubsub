import json
import socket
import sys

class Subscriber:
    def __init__(self, broker_addr, HOST, PORT):
        self.server = socket.create_server((HOST, PORT))
        self.broker_addr = broker_addr

    def subscribe(self, topic, callback):
        with socket.create_connection(self.broker_addr) as connection:
            message = json.dumps(topic)
            connection.sendall(message.encode())

    def receive(self, message):
        print(self, message)

if __name__ == '__main__':
    broker_port = sys.argv[1]
    own_port = sys.argv[2]
    subscriber = Subscriber('127.0.0.1', broker_port, own_port)
