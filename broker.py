import socket
import threading

broker_host = '127.0.0.1'
broker_port = 11343

class Broker:
    def __init__(self):       
        self.subs = {}

    def run(self):
        with socket.create_server((broker_host, broker_port)) as server:
            while True:
                print(f"Server listening on {broker_host}:{broker_port}")
                conn, addr = server.accept()
                print(f"Connected by {addr}")
                threading.Thread(target=self.register2, args=(conn, addr)).start()
                print(self.subs)

    def register(self, callback, topic):
        try:
            topic = self.subs[topic]
            topic.append(callback)
        except KeyError:
            self.subs[topic] = [callback]

    def delegate(self, message, topic):
        try:
            callbacks = self.subs[topic]
        except KeyError:
            return
        for call in callbacks:
            call(message)

    def register2(self, conn, addr):
        topic = conn.recv(1024).decode()
        try:
            topic = self.subs[topic]
            topic.append(addr)
        except KeyError:
            self.subs[topic] = [addr]
        conn.close()

if __name__ == '__main__':
    broker = Broker()
    broker.run()

#broker = Broker()
