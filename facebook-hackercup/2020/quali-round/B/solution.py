def solve(C):
    while len(C) > 1:
        x = None
        for i in range(len(C) - 2):
            if all(C[i : i + 3] != _ for _ in ['AAA', 'BBB']):
                x = 'B' if any(C[i : i + 3] == _ for _ in ['BBA', 'BAB', 'ABB']) else 'A'
                break
        if x is None:
            return 'N'
        else:
            C = C[:i] + x + C[i + 3:]

    return 'Y'

def print_ans(print_fun, A):
    for _ in A:
        print_fun(''.join(str(__) for __ in _) + '\n')


if __name__ == '__main__':
    T = 0
    n_lst = []
    C_lst = []

    T = int(input())
    for i in range(T):
        n_lst.append(int(input()))
        C_lst.append(input())

    with open('output.txt', 'w') as fin:
        for i in range(T):
            fin.write(f'Case #{i + 1}: {solve(C_lst[i])}\n')
