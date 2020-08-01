import math
import time

fact = math.factorial

def comb(n, r):
    return fact(n) / fact(r) / fact(n - r)


start = time.time()
print(comb(20, 10))
print(time.time() - start)