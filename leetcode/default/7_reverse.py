'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:

Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [-2^^31, 2^^31-1]. For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.
'''

'''
解题思路：

    1. -13 % 10 = 7

'''


EXAMPLES = [
    ((123,), 321),
    ((-123,), -321),
    ((120,), 21),
]


class Solution:
    def reverse(self, x: int) -> int:
        r = 0

        value = x
        while value:
            temp = value % 10
            if x < 0 and temp > 0:
                temp -= 10
            r = r * 10 + temp
            value = int(value / 10)

        if r > 2147483648 or r < -2147483648:
            r = 0

        return r
