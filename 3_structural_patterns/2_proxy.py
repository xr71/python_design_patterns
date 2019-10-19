import pytest
import time
import random

# Proxies are useful when object creation can become very expensive
# so delay the object creation until absolutely necessary

class Producer:

    def produce(self):
        print("Producer is expensive and busy right now")

    def meet(self):
        print("Producer has time to meet you now")

class Proxy:

    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        print("Checking if producer is available")

        if self.occupied == 'No':
            self.producer = Producer()
            time.sleep(1)

            self.producer.meet()
        else: 
            time.sleep(random.random()*2)
            print("Producer is busy!")

prox = Proxy()
prox.produce()


prox.occupied = 'Yes'
prox.produce()
