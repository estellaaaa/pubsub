import time
from publisher import Publisher
from subscriber import Subscriber

PORT = 1212

print(f"meow")
sub1 = Subscriber("Maria", ("127.0.0.1", 11343))
sub2 = Subscriber("Garfield", ("127.0.0.1", 11343))
sub3 = Subscriber("Leo", ("127.0.0.1", 11343))

pub1 = Publisher("Spiegel", ("127.0.0.1", 11343))
pub2 = Publisher("BILD", ("127.0.0.1", 11343))

sub1.subscribe("electronics", port=PORT + 1)
sub1.subscribe("environment", port=PORT + 2)

sub2.subscribe("electronics", port=PORT + 3)
sub3.subscribe("sports", port=PORT + 4)


pub1.publish("a new iphone was announced!!", "electronics")
pub1.publish("the EM 2024 is starting soon!", "sports")
pub2.publish("wow leon musk got richer lol!", "environment")
pub1.publish("aslkjdflkdsaf", "asdf")
pub2.publish("new ipad coming, get your money ready", "electronics")

time.sleep(1)

pub1.publish("UNSUBSCRIBE_ALL", "electronics")
pub1.publish("UNSUBSCRIBE_ALL", "sports")
pub1.publish("UNSUBSCRIBE_ALL", "environment")
