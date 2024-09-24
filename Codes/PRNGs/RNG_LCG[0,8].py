import matplotlib.pyplot as plt
import time
from test_dist_uniform import test_dist_is_uniform_08
from test_dist_uniform import test_dist_is_uniform_ab


def LCG(x0):
    a = 6364136223846793005
    c = 1
    m = 2**64
    while (True):
        x0 = (a*x0 + c) % m
        yield x0


def RNG(tm):
    # tm 為骰骰子次數
    # return type: list[int]
    # 初始化
    t = time.time()
    seed = int((t-int(t))*(2**64))
    G = LCG(seed)

    result = []
    # 骰骰子
    for i in range(tm):
        n = next(G)
        n = n / 2**64 * 8
        result.append(n)
    return result


L = RNG(100000)
print(test_dist_is_uniform_08(L, alpha=0.005, k=4))
print(test_dist_is_uniform_ab(L, a=1, b=6))
# plt.hist(L, bins=1000, range=(0, 8))
# plt.show()
