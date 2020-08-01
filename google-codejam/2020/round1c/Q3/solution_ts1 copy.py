from collections import Counter

def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

def solve(N, D, A_lst):
    A_count = Counter(A_lst)
    A_sorted_lst = sorted(A_count.items(), key=lambda item: item[1], reverse=True)

    if len(A_lst) >= 2:
        _A_0, _count_0 = A_sorted_lst[0]
        if _count_0 >= D:
            return 0
        _A_1, _count_1 = A_sorted_lst[1]
        if _count_0 + _count_1 >= D:
            if _A_0 > _A_1:
                return _count_0
            else:
                return D - _count_0
        return 2
    
    if len(A_lst) == 1:
        if A_lst[0] >= D:
            return 0
        if D == 2:
            return 1
        if D == 3:
            return 1


    


n = int(input())
N_lst = []
D_lst = []
A_lst_lst = []
for _ in range(n):
    N, D = [int(_) for _ in input().split(" ")]
    N_lst.append(N)
    D_lst.append(D)
    A_lst_lst.append([int(_) for _ in input().split(" ")])
    
for i in range(n):
    soln = solve(N_lst[i], D_lst[i], A_lst_lst[i])
    print("Case #{}: {}".format(i + 1, soln))
