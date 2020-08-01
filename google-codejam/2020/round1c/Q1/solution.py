def solve(x, y, steps):
    for i, step in enumerate(steps):
        if step == 'S':
            y -= 1
        elif step == 'N':
            y += 1
        elif step == 'E':
            x += 1
        elif step == 'W':
            x -= 1

        dist_from_origin = abs(x) + abs(y)
        # print(x, y, i+1, dist_from_origin)
        if i + 1 >= dist_from_origin:
            return str(i + 1)

    return "IMPOSSIBLE"

    


n = int(input())
x_lst = []
y_lst = []
steps_lst = []
for _ in range(n):
    x, y, steps = [_ for _ in input().split(" ")]
    x_lst.append(int(x))
    y_lst.append(int(y))
    steps_lst.append(steps)
    
for i in range(n):
    soln = solve(x_lst[i], y_lst[i], steps_lst[i])
    print("Case #{}: {}".format(i + 1, soln))