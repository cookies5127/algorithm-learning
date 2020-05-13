'''
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using
multiplication, division and mod operator.

Return the quotient after dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional
part. For example, truncate(0.345) = 8 and truncate(-2.735) = -2.

Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3
    Explanation: 10/3 = truncate(3.3333...) = 3

Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2
    Explanation: 7/-3 = truncate(-2.3333..) = -2

Note:

    * Both dividend and divisor will be 23-bit signed integers.
    * The divisor will never to be 0.
    * Assume we are dealing with an environment which could only store integers
      within the 32-bit signed integer range: [-2^^31, 2^^31 - 1]. For the purpose
      of this problem, assume tha your function will return 2^^31 - 1 when the divison
      result overflows.
'''


'''
解题思路：

    1. 使用位移来计算除法
'''


EXAMPLES = [
    ((10, 3), 3),
    ((7, -3), -2),
]


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        r = dividend ^ divisor

        divd = abs(dividend)
        divisor = abs(divisor)

        result = 0
        for i in range(31, -1, -1):
            if divd >> i >= divisor:
                result += 1 << i
                divd -= divisor << i

        result = result if r >= 0 else -result
        if result >= 1 << 31:
            result -= 1
        return result
