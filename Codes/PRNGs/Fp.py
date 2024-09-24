import time
import matplotlib.pyplot as plt

t = time.time()
m1 = 4294944443.0
q11 = 527612.0
q13 = 1370589.0

SEED = int((t - int(t)) * (2 ** 32 + 1))

s10, s11, s12 = SEED+0b1, SEED+0b11, SEED+0b111


num_random_numbers = 100000
random_numbers = []

for _ in range(num_random_numbers):
    p1 = q11 * s12 - q13 * s10
    k = p1 // m1
    p1 -= k * m1
    if p1 < 0.0:
        p1 += m1
    s10, s11, s12 = s11, s12, p1
    random_numbers.append(p1 / m1)

plt.hist(random_numbers, bins=1000, range=(0, 1))
plt.title('p=4294944443, r=3')
plt.show()