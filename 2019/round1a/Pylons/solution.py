import random


def solve(r, c):
    def forbidded(i, j):
        _r_i, _c_i = int(i / c), i % c
        _r_j, _c_j = int(j / c), j % c
        return (_r_i == _r_j) or (_c_i == _c_j) or (_r_i - _c_i == _r_j - _c_j) or (_r_i + _c_i == _r_j + _c_j)

    trial_count = 100000
    coordinates = [(_r + 1, _c + 1) for _r in range(r) for _c in range(c)]
    while (trial_count > 0):
        remaining = {i for i in range(len(coordinates))}
        travelled = []
        def move(_remaining):
            next_ = random.choice(_remaining)
            remaining.remove(next_)
            travelled.append(coordinates[next_])
            return next_
        cur = move(tuple(remaining))
        while (len(remaining) > 0):
            _remaining = [i for i in remaining if not forbidded(cur, i)]
            if len(_remaining) == 0:
                trial_count -= 1
                break
            cur = move(_remaining)
        if (len(remaining) == 0):
            return True, travelled

    return False, None


n = int(input())
r_lst = []
c_lst = []
for _ in range(n):
    r, c = [int(_) for _ in input().split(" ")]
    r_lst.append(r)
    c_lst.append(c)
    
for i in range(n):
    is_possible, result = solve(r_lst[i], c_lst[i])
    print("Case #{}: {}".format(i + 1, "POSSIBLE" if is_possible else "IMPOSSIBLE"))
    if is_possible:
        for r, c in result:
            print(r, c)