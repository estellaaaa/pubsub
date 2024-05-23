import json
import socket

class Publisher:
    def __init__(self, broker_addr):
        self.broker_addr = broker_addr

    def publish(self, post, topic):
        with socket.create_connection(self.broker_addr) as connection:
            message = json.dumps([post, topic])
            connection.sendall(message.encode())
        
