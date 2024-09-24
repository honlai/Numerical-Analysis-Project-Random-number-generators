import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt


def test_dist_is_uniform_08(result, alpha=0.005, k=1000):
    '''
    input result = list(random number)
    return True if this result is uniform[0,8], return False if not
    '''
    result.sort()
    n = len(result)
    df = k
    p_hat = 1/k
    Y = {i+1: 0 for i in range(k)}
    i = 1
    for val in result:
        if val > 8:
            break
        while (True):
            if val > 8/k*i:
                i += 1
            else:
                break
        Y[i] += 1
    sum = 0
    for j in range(1, k+1):
        sum += ((Y[j]-n*p_hat)**2) / (n*p_hat)
    if sum > chi2.ppf(1-alpha, df):
        return False
    else:
        return True


def test_dist_is_uniform_ab(result, alpha=0.005, k=1000, a=0, b=8):
    '''
    input result = list(random number)
    return True if this result is uniform[a,b], return False if not
    '''
    result.sort()
    n = len(result)
    df = k
    p_hat = 1/k
    Y = {i+1: 0 for i in range(k)}
    i = 1
    for val in result:
        if val > b:
            break
        while (True):
            if val > a+(b-a)/k*i:
                i += 1
            else:
                break
        Y[i] += 1
    sum = 0
    for j in range(1, k+1):
        sum += ((Y[j]-n*p_hat)**2) / (n*p_hat)
    if sum > chi2.ppf(1-alpha, df):
        return False
    else:
        return True


if __name__ == '__main__':
    print(test_dist_is_uniform_08([0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 5]))
    print(test_dist_is_uniform_ab([0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 5], a=0, b=8))
    print(chi2.ppf(1-0.005, 1000))
