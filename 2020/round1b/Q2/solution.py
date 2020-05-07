import random

class Solution:
    def __init__(self):
        self.T = None
        self.A = None
        self.B = None

    def solve_one_step(self):
        count = 0
        for i in range(-5, 5 + 1):
            for j in range(-5, 5 + 1):
                print(i, j)
                response = input()
                if response == "CENTER":
                    return True
                count += 1
                if count > 300:
                    return False

    def main(self):
        self.T, self.A, self.B = [int(_) for _ in str(input()).split(' ')]

        for case_idx in range(self.T):
            if not self.solve_one_step():
                break
            

solution = Solution()
solution.main()
