import threading
import queue
from Bruteforce.pwdConsumer import PasswordConsumer
from Bruteforce.pwdProducer import pwdProducer


queue=queue.Queue(maxsize=10)
condition=threading.Condition()

producer =pwdProducer(queue,condition)
consumer =PasswordConsumer(queue,condition)

producer.start()
consumer.start()