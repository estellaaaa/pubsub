import socket

class Publisher:
    def __init__(self, broker_addr):
        self.broker_addr = broker_addr

    def publish(self, message, topic):
        with socket.create_connection(self.broker_addr) as connection:
            post = (message, topic)
            connection.sendall(post.encode())
        
