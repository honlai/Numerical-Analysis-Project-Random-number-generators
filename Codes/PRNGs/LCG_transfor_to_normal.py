import seaborn as sns
import matplotlib.pyplot as plt
import time
from test_dist_uniform import test_dist_is_uniform_08
from test_dist_uniform import test_dist_is_uniform_ab
import math


def exp_theta(x, theta=5):
    return math.exp(-x/theta)/theta


def inverse_exp_theta(y, theta=5):
    return (-1)*theta*math.log(1-y)


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
    seed = 12345
    G = LCG(seed)

    result = []
    # 骰骰子
    for i in range(tm):
        n = next(G)
        n = (n // 2**32)/2**32
        result.append(inverse_exp_theta(n, theta=5))
    return result


prob_a1 = 1-math.exp(-10/1000)
print(prob_a1)
L = RNG(100000)
X = [x/5000 for x in range(0, 10000*5, 1)]
Y = [exp_theta(x, theta=5)*prob_a1*100000 for x in X]
plt.plot(X, Y)
plt.hist(L, bins=1000, range=(0, 10))
# plt.legend()
plt.show()
