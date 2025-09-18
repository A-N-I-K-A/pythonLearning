
from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1 )

t1=hello()
t2=hi()
t1.start()
t2.start()

t1.join()
t2.join()
print("Bye")
