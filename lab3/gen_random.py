import random

def gen_random(quantity,min,max):
    for i in range(quantity):
        yield random.randint(min,max)

