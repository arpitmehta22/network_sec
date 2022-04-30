from statsmodels.sandbox.stats.runs import runstest_1samp
import math
from scipy.stats import chisquare
from scipy.stats import kstest
from scipy.stats import  wilcoxon


# prints a list li
def printAll(li):
    for i in li[:-1]:
        print(i, end=", ")
    print(li[-1])


# gcd((p1 - 3) / 2, (p2 - 3) / 2) -  Blum Blum Shub
def prime(p):
    for i in range(2, int(1e9)):
        if i * i > p:
            break
        if p % i == 0:
            return False
    return True


def selectpq(l=800, list_r=2000):
    gcd, p = int(1e8), (-1, -1)
    for p1 in range(l, list_r + 1):
        if not prime(p1) or not prime(2 * p1 + 1):
            continue
        for p2 in range(p1 + 1, list_r + 1):
            if not prime(p2) or not prime(2 * p2 + 1) or (p1 * p2) % 4 != 3:
                continue
            if math.gcd((p1 - 3) // 2, (p2 - 3) // 2) < gcd:
                gcd = math.gcd((p1 - 3) // 2, (p2 - 3) // 2)
                p = (p1, p2)
    return p




# Returns frequency numbers without the key as a list
def freq_counter(li):
    map_f = {}
    for i in li:
        if i not in map_f:
            map_f[i] = 1
        else:
            map_f[i] += 1
    list_r = []
    for k, v in map_f.items():
        list_r.append(v)
    return list_r


# Blum Blum Shub implementation
def BlumBlumShub_function(num, p, q, seed):
    ret = []
    ret.append(seed)
    M = p * q
    for i in range(num - 1):
        ret.append((ret[-1] * ret[-1]) % M)
    return ret


# Lagged Fibonacci Generator implementation
def gen_LFG(i, j, n, lfg):
    lfg_li = []
    lfg_mod = 1145
    for i1 in range(n):
        lfg_li.append((lfg[i - 1] + lfg[j - 1]) % lfg_mod)
        lfg = lfg[1:]
        lfg.append(lfg_li[-1])
    return lfg_li

def main():

    # Select p, q, seed and number of elements to generate
    p, q = selectpq()
    seed = 18
    n = 1000


    # Calculate Blum Blum Shub and print the list as the answer
    li_bl = BlumBlumShub_function(n, p, q, seed)
    freq_bl = freq_counter(li_bl)
    printAll(li_bl)
    print("Runs test - p value for Blum Blum Shub : ", runstest_1samp(li_bl)[1])
    print("Chisquare test - p value for Blum Blum Shub : ", chisquare(freq_bl))


    # LFG
    i, j, lfg = 3, 7, [5, 63, 72, 31, 421, 141, 54, 323, 26, 412, 14, 241]
    li_lfg = gen_LFG(i, j, n, lfg)
    printAll(li_bl)
    freq_lfg = freq_counter(li_lfg)
    print(" 1. Runs test -  p value for LFG are as follows :  : ", runstest_1samp(li_lfg)[1])
    print("2. Chisquare test - p value for LFG are as follows : ", chisquare(freq_lfg))


if __name__ == "__main__":
    main()