import json
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
                incoming_message = json.loads(conn.recv(1024).decode())
                if type(incoming_message) == str:
                    print('subscribing')
                    threading.Thread(target=self.register2, args=(incoming_message, conn, addr)).start()
                else:
                    print('publishing')
                    threading.Thread(target=self.delegate, args=(incoming_message, conn, addr)).start()
                print(self.subs)

    def register(self, callback, topic):
        try:
            topic = self.subs[topic]    
            topic.append(callback)
        except KeyError:
            self.subs[topic] = [callback]

    def delegate(self, incoming_message, conn, addr):
        conn.close()
        try:
            message, topic = incoming_message
            callbacks = self.subs[topic]
        except KeyError:
            return
        for addr in callbacks:
            with socket.create_connection(addr) as connection:
                message = json.dumps(message)
                connection.sendall(message.encode())

    def register2(self, incoming_message, conn, addr):
        topic = incoming_message
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
