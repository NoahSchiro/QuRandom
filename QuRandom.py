from queue import Queue                     # Used to store our random numbers
from random import randrange as rand_int
from unicodedata import decimal             # Substitute for truely random numbers
from bitarray import bitarray               # Used for handling bitstrings
from bitarray import util                   # Used for handling bitstrings
from math import log2, ceil                 # For get_int()
import time                                 # For measuring q computer response time

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
        print("Adding to the queue...")
        before = time.time()
        for i in range(20000):
            self.my_q.put(rand_int(0,2))

        duration = time.time() - before
        print(f"Got 20,000 bits in {duration} seconds")
        print(f"Current queue size: {self.my_q.qsize()}")

    # Returns a random true or false
    def get_bool(self):
        
        if self.my_q.get() == 1:

            # If this call has reduced the size of our queue to more than half, add more elements
            if self.my_q.qsize() <= 10000:
                self.__get_more_bits()

            return True
        else:

            # If this call has reduced the size of our queue to more than half, add more elements
            if self.my_q.qsize() <= 10000:
                self.__get_more_bits()

            return False      
    
    # Returns an integer such that i is in range [start, stop] 
    # and (i-start)%increment == 0
    def get_int(self, start=0, stop=100):

        # Figure out the smallest power of two greater than the range
        power = ceil(log2(stop-start))

        # Pull 2**power bits from the queue to create a random n-bit number
        binary_num = bitarray()
        for i in range(power):
            binary_num.append(self.my_q.get())

        # Convert base 2 to base 10
        decimal_num = util.ba2int(binary_num)

        # Convert from [0, 2^32-1] to [start, stop] and round it off to the nearest int
        decimal_num = round(( (decimal_num) / (2**power-1) ) * (stop - start) + start)

        # If this call has reduced the size of our queue to more than half, add more elements
        if self.my_q.qsize() <= 10000:
            self.__get_more_bits()
        
        # Return our random integer
        return decimal_num
        
    # Returns a random string of a determined length.
    def get_string(self, length=10):

        # Ascii codes
        ascii_dict = {
            util.ba2int(bitarray('0100001')) : "!",
            util.ba2int(bitarray('0100010')) : "\"",
            util.ba2int(bitarray('0100011')) : "#",
            util.ba2int(bitarray('0100100')) : "$",
            util.ba2int(bitarray('0100101')) : "%",
            util.ba2int(bitarray('0100110')) : "&",
            util.ba2int(bitarray('0100111')) : "'",
            util.ba2int(bitarray('0101000')) : "(",
            util.ba2int(bitarray('0101001')) : ")",
            util.ba2int(bitarray('0101010')) : "*",
            util.ba2int(bitarray('0101011')) : "+",
            util.ba2int(bitarray('0101100')) : "'",
            util.ba2int(bitarray('0101101')) : "-",
            util.ba2int(bitarray('0101110')) : ".",
            util.ba2int(bitarray('0101111')) : "/",
            util.ba2int(bitarray('0110000')) : "0",
            util.ba2int(bitarray('0110001')) : "1",
            util.ba2int(bitarray('0110010')) : "2",
            util.ba2int(bitarray('0110011')) : "3",
            util.ba2int(bitarray('0110100')) : "4",
            util.ba2int(bitarray('0110101')) : "5",
            util.ba2int(bitarray('0110110')) : "6",
            util.ba2int(bitarray('0110111')) : "7",
            util.ba2int(bitarray('0111000')) : "8",
            util.ba2int(bitarray('0111001')) : "9",
            util.ba2int(bitarray('0111010')) : ":",
            util.ba2int(bitarray('0111011')) : ";",
            util.ba2int(bitarray('0111100')) : "<",
            util.ba2int(bitarray('0111101')) : "=",
            util.ba2int(bitarray('0111110')) : ">",
            util.ba2int(bitarray('0111111')) : "?",
            util.ba2int(bitarray('1000000')) : "@",
            util.ba2int(bitarray('1000001')) : "A",
            util.ba2int(bitarray('1000010')) : "B",
            util.ba2int(bitarray('1000011')) : "C",
            util.ba2int(bitarray('1000100')) : "D",
            util.ba2int(bitarray('1000101')) : "E",
            util.ba2int(bitarray('1000110')) : "F",
            util.ba2int(bitarray('1000111')) : "G",
            util.ba2int(bitarray('1001000')) : "H",
            util.ba2int(bitarray('1001001')) : "I",
            util.ba2int(bitarray('1001010')) : "J",
            util.ba2int(bitarray('1001011')) : "K",
            util.ba2int(bitarray('1001100')) : "L",
            util.ba2int(bitarray('1001101')) : "M",
            util.ba2int(bitarray('1001110')) : "N",
            util.ba2int(bitarray('1001111')) : "O",
            util.ba2int(bitarray('1010000')) : "P",
            util.ba2int(bitarray('1010001')) : "Q",
            util.ba2int(bitarray('1010010')) : "R",
            util.ba2int(bitarray('1010011')) : "S",
            util.ba2int(bitarray('1010100')) : "T",
            util.ba2int(bitarray('1010101')) : "U",
            util.ba2int(bitarray('1010110')) : "V",
            util.ba2int(bitarray('1010111')) : "W",
            util.ba2int(bitarray('1011000')) : "X",
            util.ba2int(bitarray('1011001')) : "Y",
            util.ba2int(bitarray('1011010')) : "Z",
            util.ba2int(bitarray('1011011')) : "[",
            util.ba2int(bitarray('1011100')) : "\\",
            util.ba2int(bitarray('1011101')) : "]",
            util.ba2int(bitarray('1011110')) : "^",
            util.ba2int(bitarray('1011111')) : "_",
            util.ba2int(bitarray('1100000')) : "`",
            util.ba2int(bitarray('1100001')) : "a",
            util.ba2int(bitarray('1100010')) : "b",
            util.ba2int(bitarray('1100011')) : "c",
            util.ba2int(bitarray('1100100')) : "d",
            util.ba2int(bitarray('1100101')) : "e",
            util.ba2int(bitarray('1100110')) : "f",
            util.ba2int(bitarray('1100111')) : "g",
            util.ba2int(bitarray('1101000')) : "h",
            util.ba2int(bitarray('1101001')) : "i",
            util.ba2int(bitarray('1101010')) : "j",
            util.ba2int(bitarray('1101011')) : "k",
            util.ba2int(bitarray('1101100')) : "l",
            util.ba2int(bitarray('1101101')) : "m",
            util.ba2int(bitarray('1101110')) : "n",
            util.ba2int(bitarray('1101111')) : "o",
            util.ba2int(bitarray('1110000')) : "p",
            util.ba2int(bitarray('1110001')) : "q",
            util.ba2int(bitarray('1110010')) : "r",
            util.ba2int(bitarray('1110011')) : "s",
            util.ba2int(bitarray('1110100')) : "t",
            util.ba2int(bitarray('1110101')) : "u",
            util.ba2int(bitarray('1110110')) : "v",
            util.ba2int(bitarray('1110111')) : "w",
            util.ba2int(bitarray('1111000')) : "x",
            util.ba2int(bitarray('1111001')) : "y",
            util.ba2int(bitarray('1111010')) : "z",
            util.ba2int(bitarray('1111011')) : "{",
            util.ba2int(bitarray('1111100')) : "|",
            util.ba2int(bitarray('1111101')) : "}",
            util.ba2int(bitarray('1111110')) : "~",
            util.ba2int(bitarray('1111111')) : " ",
        }

        response = ""

        # For each character that we need
        for i in range(length):

            # We need 7 bits for an ascii character
            binary_num = bitarray()
            for j in range(7):
                
                # If our MSB is 0, then the next digit MUST be a 1
                if binary_num == bitarray('0'):
                    binary_num.append(1)
                binary_num.append(self.my_q.get())

            # Add the generated character to the string
            response += ascii_dict[util.ba2int(binary_num)]
        
        # If this call has reduced the size of our queue to more than half, add more elements
        if self.my_q.qsize() <= 10000:
            self.__get_more_bits()
        
        return response

if __name__ == "__main__":
    
    Q = QuRandom()

    print(Q.get_int())