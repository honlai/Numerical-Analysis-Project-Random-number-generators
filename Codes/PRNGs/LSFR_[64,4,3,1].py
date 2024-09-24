start_state = 1 << 2 | 1
lfsr = start_state
period = 0

for i in range(20):
    #taps: 4 3; feedback polynomial: x^4 + x + 1
    # 1 2 3 4
    #     * * 
    # bit = (lfsr ^ (lfsr >> 1) ) & 1
    # lfsr = (lfsr >> 1) | (bit << 3)
    # period += 1
    # print(f"({bin(lfsr)}) {lfsr}")
    # if (lfsr == start_state):
    #     print(period)
    #     break


    # feedback polynomial: x^64 + x^4 + x^3 + x + 1 also 1 + x^60 + x^61 + x^63 + x^64
    
    bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 3) ^ (lfsr >> 4) ) & 1
    lfsr = (lfsr >> 1) | (bit << 63)
    period += 1
    print(f"({bin(lfsr)}) {lfsr}")
    if (lfsr == start_state):
        print(period)
        break