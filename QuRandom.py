from queue import Queue
from random import randrange as rand_int
from unicodedata import decimal
from bitarray import bitarray
from bitarray import util

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

    # Adds more random ints to our queue, needs to be private
    def __get_more_bits(self):

        print(f"Current queue size {self.my_q.qsize()}")
        print("Adding to the queue")
        for i in range(20000):
            self.my_q.put(rand_int(0,2))

        print(f"Current queue size {self.my_q.qsize()}")

    # Returns a random true or false
    def get_bool(self):
        if self.my_q.get() == 1:
            return True
        else:
            return False
    
    # Returns an integer such that i is in range [start, stop] 
    # and (i-start)%increment == 0
    def get_int(self, start=0, stop=100):
        
        # Pull 32 bits from the queue to create a random 32-bit number
        binary_num = bitarray()
        for i in range(32):
            binary_num.append(self.my_q.get())

        # Convert base 2 to base 10
        decimal_num = util.ba2int(binary_num)

        # Convert from [0, 2^32-1] to [start, stop] and round it off to the nearest int
        decimal_num = round(( (decimal_num) / (2**32-1) ) * (stop - start) + start)

        # If this call has reduced the size of our queue to more than half, add more elements
        if self.my_q.qsize() <= 10000:
            self.__get_more_bits()
        
        # Return our random integer
        return decimal_num
        
    # Returns a random string of a determined length. Can include all ascii characters or a restricted set
    def get_string(self):

        # If this call has reduced the size of our queue to more than half, add more elements
        if self.my_q.qsize() <= 10000:
            self.__get_more_bits()

if __name__ == "__main__":
    
    Q = QuRandom()

    true_counter = 0
    false_counter = 1

    for i in range(1000):
        if Q.get_bool():
            true_counter+=1
        else:
            false_counter+=1