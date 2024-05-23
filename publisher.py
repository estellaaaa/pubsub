import json
import socket


class Publisher:
    def __init__(self, name, broker_addr):
        self.name = name
        self.broker_addr = broker_addr

    def publish(self, post, topic):
        print(f'PUBLISHER {self.name}:', post, topic)
        with socket.create_connection(self.broker_addr) as connection:
            message = json.dumps([post, topic])
            connection.sendall(message.encode())
