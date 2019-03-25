import sys
import threading
import queue


class pwdProducer(threading.Thread):

    def __init__(self,queue,condition):
        threading.Thread.__init__(self)
        self.queue=queue
        self.condition=condition



    def run(self):
        while(True):

            password=input("Next Password")

            self.condition.acquire()

            try:
                self.queue.put(password,block=False)
                self.condition.notify()

            except queue.Empty:
                self.condition.wait()
                self.condition.release()

