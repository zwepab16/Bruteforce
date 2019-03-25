import threading
import queue
from Bruteforce.password import Password

class PasswordConsumer(threading.Thread):


    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue=queue
        self.condition=condition

    def run(self):
        password=None

        while(True):
            self.condition.acquire()
            try:

                self.condition.notify()
            except queue.Empty:
                self.condition.wait()
            self.condition.release()
############################
            your_list = '123456789'
            completeList=[]
            for current in range(3):
                a = [i for i in your_list],
                for y in range(current):
                    a = [x + i for i in your_list for x in a]
                    password.check(a)
############################

            if not password is None:
                print("Testing with '123' = " + password.check("123"))
