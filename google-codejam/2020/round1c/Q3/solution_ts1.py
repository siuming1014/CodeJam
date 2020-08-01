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
    # print(A_sorted_lst)
    cur_slices_map = dict()
    cur_num_slices = 0
    cur_num_of_cut = 0

    for _A_i, _count_i in A_sorted_lst:
        print(cur_slices_map)

        _ = False
        for _A_j in cur_slices_map:
            _gcd = gcd(_A_i, _A_j)
            if _gcd != 1:
                a = int(_A_i / _gcd)
                b = int(_A_j / _gcd)
                _count_j = cur_slices_map[_A_j]
                del cur_slices_map[_A_j]
                cur_slices_map[_gcd] = a * _count_i + b * _count_j
                cur_num_slices += cur_slices_map[_gcd] - _count_j
                _ = True
                break
        if not _:
            cur_slices_map[_A_i] = _count_i
            cur_num_slices += _count_i
        
        if cur_num_slices >= D:
            return cur_num_slices - min(cur_slices_map.items(), key=lambda item: item[0])[1]

    print(cur_slices_map, cur_num_slices)
    return -1

    


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
