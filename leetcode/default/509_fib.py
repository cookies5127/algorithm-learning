'''
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) from a sequence, called the Fibonacci
sequence, such that each number is the sum of the two preceding ones, starting from
0 and 1. Tha is,

F(0) = 0, F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1

Given N, calculate F(N)

Example 1:

Input: 2
Output: 1
ExPlanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: 3
Output: 2
ExPlanation: F(3) = F(2) + F(1) = 1 + 1 = 2

Exmalpe 3:

Input: 4
Output: 3
ExPlanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:

0 <= N <= 30.
'''


'''
总结：

    1. 递归来解
    2. 为了能运行的更快，需要从2-N cache 以前算过的内容。
'''


EXAMPLES = [
    (2, 1),
    (3, 2),
    (4, 3),
]


class Solution:
    def get_value(self, N: int, memorize: dict) -> int:
        r = 0
        if N in memorize:
            r = memorize[N]
        else:
            r = self.get_value(N - 1, memorize) + self.get_value(N - 2, memorize)
            memorize[N] = r
        return r

    def fib(self, N: int) -> int:
        memorize = {0: 0, 1: 1}
        return self.get_value(N, memorize)
