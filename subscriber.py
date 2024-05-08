class Subscriber:
    def __init__(self, broker):
        self.broker = broker

    def subscribe(self, topic, callback):
        self.broker.register(callback, topic)

    def receive(self, message):
        print(self, message)