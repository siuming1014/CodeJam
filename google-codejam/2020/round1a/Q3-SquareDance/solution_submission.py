import random


def solve(dims, ilevels):
    # print(dims)
    # print(ilevels)
    # print("dims, ilevels:", dims, ilevels)

    is_elim = [[False] * dims[1] for _ in range(dims[0])]
    no_neighbors = [[False] * dims[1] for _ in range(dims[0])]
    # remaining = {(i, j) for i in range(dims[0]) for j in range(dims[1])}
    interest_level = 0

    is_changed = True
    while is_changed:
        is_changed = False
        to_be_eliminated = []
        for i in range(dims[0]):
            for j in range(dims[1]):
                if is_elim[i][j]:
                    continue

                # print("i, j:", i, j)
                interest_level += ilevels[i][j]

                if no_neighbors[i][j]:
                    continue

                _neighbors = []

                # up
                a = [(_i, j, ilevels[_i][j]) for _i in range(0, i) if not is_elim[_i][j]]
                if len(a) > 0:
                    _neighbors.append(min(a, key=lambda _: i - _[0]))
                # down
                a = [(_i, j, ilevels[_i][j]) for _i in range(i + 1, dims[0]) if not is_elim[_i][j]]
                if len(a) > 0:
                    _neighbors.append(min(a, key=lambda _: _[0]))
                # left
                a = [(i, _j, ilevels[i][_j]) for _j in range(0, j) if not is_elim[i][_j]]
                if len(a) > 0:
                    _neighbors.append(min(a, key=lambda _: j - _[1]))
                # right
                a = [(i, _j, ilevels[i][_j]) for _j in range(j + 1, dims[1]) if not is_elim[i][_j]]
                if len(a) > 0:
                    _neighbors.append(min(a, key=lambda _: _[1]))

                if len(_neighbors):
                    _average = float(sum(_neighbor[2] for _neighbor in _neighbors)) / len(_neighbors)
                    if ilevels[i][j] < _average:
                        to_be_eliminated.append((i, j))
                        is_changed = True

                else:
                    no_neighbors[i][j] = True

        for _ in to_be_eliminated:
            # print(_)
            is_elim[_[0]][_[1]] = True
        
        # print("is_elim", is_elim)

    return interest_level


n = int(input())
dim_lst = []  # int[][2]
ilevel_lst = []  # int[][][]
for _ in range(n):
    dim_lst.append([int(_) for _ in input().split(" ")])
    ilevel_lst.append([])
    for _ in range(dim_lst[-1][0]):
        ilevel_lst[-1].append([int(_) for _ in input().split(" ")])
    
for i in range(n):
    y = solve(dim_lst[i], ilevel_lst[i])
    print("Case #{}: {}".format(i + 1, y))