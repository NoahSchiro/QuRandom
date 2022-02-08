from queue import Queue
from random import randrange as rand_int

from numpy import get_include

# This class seeks to make calls to ibm's quantum 
# computers to generate a bunch of truely random bits. 
# To save on calls made to the quantum computer (and 
# to avoid wait times), we can make one call that 
# generates more data than we need, stores this data 
# in a queue, and then pops the data from the queue as 
# we need it. This will also include functionality for 
# generating more than just random 1s and 0s. Certain 
# methods will convert this data to ints, floats, 
# strings, etc.

class QuRandom:

    my_q = Queue()

    def __init__(self):

        # If queue is empty, we need to populate it
        for i in range(20000):

            # For now, we are just going to use pseudo-random 
            # data. Eventually, we will hook up the IBM quantum systems
            self.my_q.put(rand_int(0,2))

    # Returns an integer such that i is in range [start, stop] 
    # and (i-start)%increment == 0
    def get_int(self, start=0, stop=100, increment=1):

        # Construct a 32 bit number

        # Convert to int

        # Convert from [0, 2^32-1] to [start, stop]
        pass

    def get_string(self):
        pass

if __name__ == "__main__":
    
    Q = QuRandom()

    Q.get_int()