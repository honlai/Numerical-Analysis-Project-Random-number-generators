import matplotlib.pyplot as plt
import time


def RNG1(times):
    t = time.time()
    m1 = 4294944443.0
    q11 = 527612.0
    q13 = 1370589.0
    SEED = int((t - int(t)) * (m1))
    s10, s11, s12 = SEED, SEED, SEED
    random_numbers = []

    for _ in range(times):
        p1 = q11 * s12 - q13 * s10
        k = p1 // m1
        p1 -= k * m1
        if p1 < 0.0:
            p1 += m1
        s10, s11, s12 = s11, s12, p1
        random_numbers.append(p1 / m1)
    return random_numbers

# Q2


def RNG2(times):
    t = time.time()
    m1 = 4294949027.0
    a12 = 1154721.0
    a14 = 1739991.0
    a15n = 1108499.0
    SEED = int((t - int(t)) * (m1))
    s10, s11, s12, s13, s14 = SEED+12345, SEED+1234, SEED+123, SEED+12, SEED+1
    random_numbers = []
    for _ in range(times):
        p1 = a12 * s13 - a15n * s10
        if (p1 > 0.0):
            p1 -= a14 * m1
        p1 += a14 * s11
        k = int(p1 / m1)
        p1 -= k * m1
        if (p1 < 0.0):
            p1 += m1
        s10 = s11
        s11 = s12
        s12 = s13
        s13 = s14
        s14 = p1
        random_numbers.append(p1/m1)
    return random_numbers

# decimal to binary


def dec_to_bin(x, k=10):
    L = []
    for i in range(k):
        n = -1-i
        if x > 2**n:
            L.append(1)
            x -= 2**n
        else:
            L.append(0)
    return L

# binary to decimal


def bin_to_dec(L):
    return sum([x*2**(-1-i) for i, x in enumerate(L)])

# combine


def combine(a, b):
    LA = dec_to_bin(a)
    LB = dec_to_bin(b)
    L = []
    for i in range(len(LA)):
        L.append(LA[i])
        L.append(LB[i])
    return bin_to_dec(L)

# main function


def RNG(times):
    L1 = RNG1(times)
    L2 = RNG2(times)
    L = [combine(a, b) for a, b in zip(L1, L2)]
    return L

if __name__=="__main__":    
    L = RNG(100000)
    plt.hist(L, bins=1000, range=(0, 1))
    plt.show()
