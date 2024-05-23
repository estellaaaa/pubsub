import json
import socket
import sys
import threading


class Subscriber:
    def __init__(self, broker_addr, HOST, PORT):
        self.addr = (HOST, PORT)
        self.broker_addr = broker_addr
        
    def subscribe(self, topic, callback):
        with socket.create_connection(self.broker_addr) as connection:
            message = json.dumps(topic)
            connection.sendall(message.encode())
            threading.Thread(target=self.run).start()

    def run(self):
        with socket.create_server(self.addr) as server:
            print(f"SUBSCRIBER: Server listening on {self.addr[0]}:{self.addr[1]}")
            conn, addr = server.accept()
            print(f"SUBSCRIBER: Connected by {addr}")
            incoming_message = json.load(conn.recv(1024).decode())
            print('SUBSCRIBER:', incoming_message)
            # threading.Thread(target=self.run).start()


if __name__ == '__main__':
    broker_port = sys.argv[1]
    own_port = sys.argv[2]
    subscriber = Subscriber('127.0.0.1', broker_port, own_port)
