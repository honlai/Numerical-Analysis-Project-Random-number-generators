import time
import matplotlib.pyplot as plt
# parameter from MRGK32a 
norm = 2.328306549295728e-10
m1 = 4294967087.0
m2 = 4294944443.0
a12 = 1403580.0
a13n = 810728.0
a21 = 527612.0
a23n = 1370589.0
# Get current time to use as seed
y = int(time.time())
SEED = y
s10 = SEED
s11 = SEED
s12 = SEED
s20 = SEED
s21 = SEED
s22 = SEED
results = []
for i in range(10000000):
    # Component 1
    p1 = a12 * s11 - a13n * s10
    k = p1 // m1
    p1 -= k * m1
    if p1 < 0.0:
        p1 += m1
    s10 = s11
    s11 = s12
    s12 = p1

    # Component 2
    p2 = a21 * s22 - a23n * s20
    k = p2 // m2
    p2 -= k * m2
    if p2 < 0.0:
        p2 += m2
    s20 = s21
    s21 = s22
    s22 = p2
    # Combination
    if p1 <= p2:
        print(f"{(p1 - p2 + m1) * norm} ", end='')
        results.append((p1 - p2 + m1) * norm)
    else:
        print(f"{(p1 - p2) * norm} ", end='')
        results.append((p1 - p2) * norm)
plt.hist(results, bins=500000, edgecolor='blue')
plt.title('Random Number Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

