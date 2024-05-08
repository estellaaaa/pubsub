class Broker:
    def __init__(self):
        self.subs = {}

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