import math
import random
import inspect

fact = math.factorial

pascal_mem = dict()

def pascal(n_r):
    n, r = n_r
    if (n, r) not in pascal_mem:
        pascal_mem[(n, r)] = int(fact(n - 1)) / int(fact(r - 1)) / int(fact(n - r))
    return pascal_mem[(n, r)]


def solve(N):
    steps = []
    visited = set(steps)
    sum_ = 0
    is_stop = False
    def dfs(_n, _r):
        nonlocal steps
        nonlocal visited
        nonlocal sum_
        nonlocal is_stop

        # print('start', (_n, _r), steps, sum_, visited, is_stop)

        if is_stop:
            return

        if len(steps) > 500:
            return

        visited.add((_n, _r))

        _ = sum_ + pascal((_n, _r))
        if _ == N:
            steps.append((_n, _r))
            is_stop = True
        elif _ < N:
            next_steps = [(_n + 1, _r + 1), (_n + 1, _r)] if _r < round((_n + 1) / 2) else [(_n + 1, _r), (_n + 1, _r + 1)]
            next_steps += [(_n, _r + 1), (_n, _r - 1)] if _r - 1 < round(_n / 2) else [(_n, _r - 1), (_n, _r + 1)]
            next_steps += [(_n - 1, _r), (_n - 1, _r - 1)] if _r - 1 < round((_n - 1) / 2) else [(_n - 1, _r - 1), (_n - 1, _r)]
            next_steps = [
                (_n2, _r2) for _n2, _r2 in next_steps
                if (_n2, _r2) not in visited and _n2 > 1 and _r2 >= 1 and _r2 <= _n2
            ]

            if len(next_steps):
                steps.append((_n, _r))
                # print('before next', sum_, pascal((_n, _r)))
                sum_ += pascal((_n, _r))
                for _n2, _r2 in next_steps:
                    dfs(_n2, _r2)
                if not is_stop:
                    steps.pop(-1)
                    sum_ -= pascal((_n, _r))

        # print('end', (_n, _r), steps, sum_, visited, is_stop)
        return

    dfs(1, 1)
    return steps


N = int(input())
n_lst = []
for _ in range(N):
    n_lst.append(int(input()))
    
for i in range(N):
    result = solve(n_lst[i])
    print("Case #{}:".format(i + 1))
    for _ in result:
        print(_[0], _[1])
#     # print(len(result), sum(pascal(_) for _ in result))


# WA = False
# while (not WA):
#     n = random.randint(1, 1000000000)
#     result = solve(n)
#     print('n:', n)
#     if (len(result) != len(set(result)) or n != sum(pascal(_) for _ in result)):
#         print('len(result):', len(result))
#         print('len(set(result):', len(set(result)))
#         print('sum(pascal(_) for _ in result):', sum(pascal(_) for _ in result))
#         WA = True


# for n in random.shuffle(list(range(1, 1000000001))):
#     result = solve(n)
#     print('n:', n)
#     if (len(result) != len(set(result)) or n != sum(pascal(_) for _ in result)):
#         print('len(result):', len(result))
#         print('len(set(result):', len(set(result)))
#         print('sum(pascal(_) for _ in result):', sum(pascal(_) for _ in result))
#         break
