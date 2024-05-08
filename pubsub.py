class Publisher:
    def __init__(self, broker):
        self.broker = broker

    def publish(self, message, topic):
        self.broker.delegate(message, topic)


class Subscriber:
    def __init__(self, broker):
        self.broker = broker

    def subscribe(self, topic, callback):
        self.broker.register(callback, topic)

    def receive(self, message):
        print(self, message)


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



broker = Broker()

sub1 = Subscriber(broker)
sub2 = Subscriber(broker)
sub3 = Subscriber(broker)

pub1 = Publisher(broker)
pub2 = Publisher(broker)

sub1.subscribe('electronics', callback=lambda x: print('sub1', x))
sub1.subscribe('environment', callback=lambda x: print('sub1', x))

sub2.subscribe('electronics', callback=lambda x: print('sub2', x))
sub3.subscribe('sports', callback=lambda x: print('sub3', x))

pub1.publish('a new iphone was announced!!', 'electronics')
pub1.publish('aslkjdflkdsaf', 'asdf')
# class Message:
#     def __init__(self, topic):
#         self.topic = topic

# class topic meow
