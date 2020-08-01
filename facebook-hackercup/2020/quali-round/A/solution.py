def solve(n, I, O):
    i_arr = list(map(lambda x: x == 'Y', list(I)))
    o_arr = list(map(lambda x: x == 'Y', list(O)))

    P = [[None] * n for _ in range(n)]

    for i in range(n):
        P[i][i] = 1
        if i > 0:
            P[i][i - 1] = i_arr[i] * o_arr[i - 1]
        if i < n - 1:
            P[i][i + 1] = i_arr[i] * o_arr[i + 1]

    for j in range(n):
        for i in range(j + 2, n):
            P[i][j] = i_arr[i] * o_arr[i - 1] * P[i - 1][j]

    for j in range(n):
        for i in range(j - 2, -1, -1):
            P[i][j] = i_arr[i] * o_arr[i + 1] * P[i + 1][j]
    
    PT = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            PT[i][j] = 'Y' if P[j][i] else 'N'

    return PT


def print_ans(print_fun, A):
    for _ in A:
        print_fun(''.join(str(__) for __ in _) + '\n')


if __name__ == '__main__':
    n_lst = []
    I_lst = []
    O_lst = []

    T = int(input())
    for i in range(T):
        n_lst.append(int(input()))
        I_lst.append(input())
        O_lst.append(input())
            
    with open('output.txt', 'w') as fin:
        for i in range(T):
            n = n_lst[i]
            I = I_lst[i]
            O = O_lst[i]
            fin.write(f'Case #{i + 1}:\n')
            print_ans(fin.write, solve(n, I, O))
