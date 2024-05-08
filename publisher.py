class Publisher:
    def __init__(self, broker):
        self.broker = broker

    def publish(self, message, topic):
        self.broker.delegate(message, topic)