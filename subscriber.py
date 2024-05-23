import json
import socket
import sys
import threading


class Subscriber:
    def __init__(self, name, broker_addr):
        self.name = name
        self.broker_addr = broker_addr
        self.subscribed = False

    def subscribe(self, topic, port):
        self.subscribed = True
        with socket.create_connection(self.broker_addr, source_address=('127.0.0.1', port)) as connection:
            message = json.dumps(topic)
            connection.sendall(message.encode())
        threading.Thread(target=self.run, args=(topic, port)).start()

    def run(self, topic, port):
        with socket.create_server(('127.0.0.1', port)) as server:
            while self.subscribed:
                print(f"SUBSCRIBER: Server listening on 127.0.0.1:{port}")
                conn, addr = server.accept()
                print(f"SUBSCRIBER: Connected by {addr}")
                incoming_message = json.loads(conn.recv(1024).decode())
                if incoming_message == 'UNSUBSCRIBE_ALL':
                    self.subscribed = False
                print(f'HEY SUBSCRIBER {self.name}:', incoming_message)
                conn.close()
        #self.subscribe(topic, port)


if __name__ == '__main__':
    broker_port = sys.argv[1]
    own_port = sys.argv[2]
    subscriber = Subscriber('127.0.0.1', broker_port, own_port)
