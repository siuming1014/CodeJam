import math
import random

fact = math.factorial

nCr_mem = dict()

def nCr(n, r):
    if (n, r) in nCr_mem:
        return nCr_mem[(n, r)]
    return int(fact(n) / fact(r) / fact(n - r))


def solve(N):
    steps = [(1, 1)]
    nCr_mem = dict()
    sum_ = 1
    level = 1
    while sum_ < N:
        level += 1
        nCr_mem
        sum_ += nCr(level, round(level / 2))
        steps.append((level, round(level / 2)))

    # print(steps)
    # print(sum_)
    # return steps

    if sum_ != N:
        while sum_ > N:
            i = random.choice(range(len(steps)))
            # print(steps[i])
            _n, _r = steps[i]
            if i == 0:
                continue
            if _r <= 1:
                continue
            is_skip = False
            _n_1, _r_1 = steps[i - 1]
            if i != len(steps):
                _n_2, _r_2 = steps[i + 1]
                if _r == _r_1 - 1 and _r == _r_2:
                    _r_3 = _r - 1
                elif _r == _r_1 and _r == _r_2 + 1:
                    _r_3 = _r + 1
                else:
                    is_skip = True
            else:
                _r_3 = _r + 1 if _r == _r_1 else _r - 1
                
            if not is_skip:
                diff = nCr(_n, _r_3) - nCr(_n, _r)
                if sum_ + diff >= N:
                    steps[i] = (_n, _r - 1)
                    sum_ += diff
                    if sum_ == N:
                        return steps

    return steps


n = int(input())
N_lst = []
for _ in range(n):
    N_lst.append(int(input()))
    
for i in range(n):
    result = solve(N_lst[i])
    print("Case #{}:".format(i + 1))
    for _ in result:
        print(_[0], _[1])