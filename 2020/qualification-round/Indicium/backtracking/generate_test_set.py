test_cases = []

n = 5
for _n in range(2, n + 1):
    k = range(_n, _n**2 + 1)
    for _k in k:
        test_cases.append((_n, _k))

print(len(test_cases))
for test_case in test_cases:
    print(test_case[0], " ", test_case[1])