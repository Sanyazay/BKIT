from contextlib import contextmanager
import time


@contextmanager
def cm_timer1():
    start=time.time()
    yield
    print(time.time()-start)
#with cm_timer1():
#    time.sleep(1)


class cm_timer2():
    
    def __init__(self):
        self.start=0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self,type, value, traceback):
        print(time.time()-self.start)

#with cm_timer2():
#    time.sleep(2)