from broker import Broker
from publisher import Publisher
from subscriber import Subscriber


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

# class topic meow meow meow
