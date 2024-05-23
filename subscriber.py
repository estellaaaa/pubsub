import json
import socket
import threading


class Subscriber:
    def __init__(self, name, broker_addr):
        self.name = name
        self.broker_addr = broker_addr
        self.subscribed = False

    def subscribe(self, topic, port):
        self.subscribed = True
        with socket.create_connection(self.broker_addr, source_address=("127.0.0.1", port)) as connection:
            message = json.dumps(topic)
            connection.sendall(message.encode())
        threading.Thread(target=self.run, args=(port,)).start()

    def run(self, port):
        with socket.create_server(("127.0.0.1", port)) as server:
            while self.subscribed:
                print(f"SUBSCRIBER: Server listening on 127.0.0.1:{port}")
                conn, addr = server.accept()
                print(f"SUBSCRIBER: Connected by {addr}")
                incoming_message = json.loads(conn.recv(1024).decode())
                if "UNSUBSCRIBE_ALL" in incoming_message:
                    self.subscribed = False
                print(f"HEY SUBSCRIBER {self.name}:", incoming_message)
                conn.close()
