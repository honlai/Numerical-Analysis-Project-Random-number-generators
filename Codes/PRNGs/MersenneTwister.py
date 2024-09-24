#! coding: utf-8
import time

#use this module by "import MersenneTwister"

#This seems like a RNG
#Use time() to get a good seed"
def get_seed():
    t = time.time()
    t-=int(t)
    t*=(10**16)
    seed = int(t)
    return seed

#MersenneTwister
class MersenneTwister:
    #Initialize the generator from a seed
    def __init__(self, seed = 0,w= 32,n= 624,m= 397,r = 31,a= 0x9908B0DF,u = 11,s = 7,t = 15,l = 18,b = 0x9D2C5680,c= 0xEFC60000,initialization_multiplier= 0x6C078965):
        #Word size
        self.__w = w
        #State size
        self.__n = n
        #Shift size
        self.__m = m
        #Mask bits
        self.__r = r
        #Xor Mask
        self.__a = a
        #Tempering shift parameters
        self.__u = u
        self.__s = s
        self.__t = t
        self.__l = l
        #Tempering bitmask parameters
        self.__b = b
        self.__c = c
        self.__max_bits = (1 << self.__w) - 1 
        
        #f
        self.__initialization_multiplier = initialization_multiplier

        self.__lower_mask = (1 << self.__r) - 1                  
        self.__upper_mask = ( self.__max_bits | (~self.__lower_mask)) 

        self.__index = self.__n
        self.__MT = [0] * self.__n
        self.__MT[0] = seed & self.__max_bits

        #Initialization
        for i in range(1, self.__n):
            self.__MT[i]= (self.__initialization_multiplier * (self.__MT[i - 1] ^ (self.__MT[i - 1] >> (self.__w-2))) + i) & self.__max_bits
        return

    #Generate the next n values from the series X_i
    def __twister(self):
        for i in range(self.__n):
            #Get (X_i (upper)|X_i+1 (lower)) 
            #i.e. concatenating the upper w − r bits of X_i and the lower r bits of X_i+1
            x = (self.__MT[i] & self.__upper_mask) | (self.__MT[(i + 1) % self.__n] & self.__lower_mask)
            #Compute XA
            xA = (x >> 1)
            if (x & 1):
                xA ^= self.__a
            #Compute X_k+n (= X_k+m XOR XA)
            self.__MT[i] = self.__MT[(i + self.__m) % self.__n] ^ xA
        self.__index = 0
        return
    
    # Extract a tempered value based on MT[index]
    # Calling twist() every n numbers
    def __temper(self):
        if self.__index == self.__n:
            self.__twister()

        x = self.__MT[self.__index]
        y = x ^ (x >> self.__u) & self.__max_bits
        y = y ^ (y << self.__s) & self.__b
        y = y ^ (y << self.__t) & self.__c
        z = y ^ (y >> self.__l)

        self.__index = (self.__index + 1) % self.__n

        #return lowest w bits of z
        return z & ((self.__max_bits<<1)|1)

    #call function
    def __call__(self):
        return self.__temper()

class mt19937(MersenneTwister):
    def __init__(self, seed = 0,w= 32,n= 624,m= 397,r = 31,\
                 a= 0x9908B0DF,\
                 u = 11,s = 7,t = 15,l = 18,\
                 b = 0x9D2C5680,c= 0xEFC60000,\
                 initialization_multiplier= 0x6C078965):
        super().__init__(seed,w,n,m,r,a,u,s,t,l,b,c,initialization_multiplier)

class mt19937_64(MersenneTwister):
    def __init__(self, seed = 0,w=64,n = 312,m = 156,r = 31,\
                 a = 0xB5026F5AA96619E9 ,\
                 u = 29,s = 17,t = 37,l = 43,\
                 b = 0x71D67FFFEDA60000,c = 0xFFF7EEE000000000  ,\
                 initialization_multiplier = 0x851F42D4C957F2D):
        super().__init__(seed,w,n,m,r,a,u,s,t,l,b,c,initialization_multiplier)
    

#main function Example
if __name__ == "__main__":
    seed = get_seed()
    #mt = MersenneTwister(seed,w,n,m,r,a,u,s,t,l,b,c,initialization_multiplier)
    mt = mt19937(seed)
    #mt = mt19937_64(seed)
    tank = set()
    Nmax = 100
    for i in range(Nmax):
        rdn = mt()
        tank.add(rdn)
        print(rdn)
