import json
import socket
import sys
import threading


class Subscriber:
    def __init__(self, broker_addr):
        self.broker_addr = broker_addr
        
    def subscribe(self, topic, port):
        with socket.create_connection(self.broker_addr, source_address=('127.0.0.1', port)) as connection:
            message = json.dumps(topic)
            connection.sendall(message.encode())
        threading.Thread(target=self.run, args=(port,)).start()

    def run(self, port):
        with socket.create_server(('127.0.0.1', port)) as server:
            print(f"SUBSCRIBER: Server listening on 127.0.0.1:{port}")
            conn, addr = server.accept()
            print(f"SUBSCRIBER: Connected by {addr}")
            incoming_message = json.loads(conn.recv(1024).decode())
            print('SUBSCRIBER:', incoming_message)
            #threading.Thread(target=self.run).start()


if __name__ == '__main__':
    broker_port = sys.argv[1]
    own_port = sys.argv[2]
    subscriber = Subscriber('127.0.0.1', broker_port, own_port)
