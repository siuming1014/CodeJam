import random

def dfs(x, y, _x, _y, i, steps):
    pass


def solve(x, y):
    if (x % 2 == y % 2):
        return "IMPOSSIBLE"

    


n = int(input())
xy_lst = []  # int[][2]
for _ in range(n):
    xy_lst.append([int(_) for _ in input().split(" ")])
    
for i in range(n):
    soln = solve(*xy_lst[i])
    print("Case #{}: {}".format(i + 1, soln))