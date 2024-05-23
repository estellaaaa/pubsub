from broker import Broker
from publisher import Publisher
from subscriber import Subscriber
import subprocess


# subprocess.Popen(['python', 'broker.py'])
# broker = Broker()

print(f"meow")
sub1 = Subscriber(('127.0.0.1', 11343))
sub2 = Subscriber(('127.0.0.1', 11343))
sub3 = Subscriber(('127.0.0.1', 11343))

pub1 = Publisher(('127.0.0.1', 11343))
pub2 = Publisher(('127.0.0.1', 11343))

sub1.subscribe('electronics', port=13338)
sub1.subscribe('environment', port=13425)

sub2.subscribe('electronics', port=25843)
sub3.subscribe('sports', port=23623)


pub1.publish('a new iphone was announced!!', 'electronics')
pub1.publish('the EM 2024 is starting soon!', 'sports')
pub2.publish('wow leon musk got richer lol!', 'environment')
pub1.publish('aslkjdflkdsaf', 'asdf')


# class Message:
#     def __init__(self, topic):
#         self.topic = topic

# class topic meow meow meow
