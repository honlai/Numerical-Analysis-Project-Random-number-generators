import matplotlib.pyplot as plt
import time


def LCG(x0):
    a = 75
    c = 74
    m = 2**16+1
    while (True):
        x0 = (a*x0 + c) % m
        yield x0


def Dice(tm):
    # tm 為骰骰子次數
    # return type: list[int]
    # 初始化
    t = time.time()
    seed = int((t-int(t))*(2**16+1))
    G = LCG(seed)
    result = []
    # 骰骰子
    for i in range(tm):
        num = (next(G) % 6) + 1
        result.append(num)
    return result


print(Dice(8))
