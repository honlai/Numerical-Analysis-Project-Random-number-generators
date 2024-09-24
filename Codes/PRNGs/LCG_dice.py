import matplotlib.pyplot as plt
import time


def LCG(x0):
    a = 75
    c = 74
    m = 2**16+1
    while (True):
        x0 = (a*x0 + c) % m
        yield x0


# 初始化
t = time.time()
seed = int((t-int(t))*(2**16+1))
print(seed)
G = LCG(seed)
D = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 0: 0}


# 骰骰子
tm = 10000  # 要骰幾次
for i in range(tm):
    num = next(G) % 6
    D[num] += 1


# 畫圖
nums = [1, 2, 3, 4, 5, 6]
times = [D[1], D[2], D[3], D[4], D[5], D[0]]
fig, ax = plt.subplots()
ax.bar(nums, times)
ax.set_ylabel('count')
ax.set_title('my random number generator')

plt.show()
