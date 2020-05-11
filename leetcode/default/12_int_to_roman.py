'''
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol      Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written
as XXVII, which XX + V + II.

Roman numberals are usually written largest to smallest from left to right. However,
the numberal for four is not III. Instead, the number four is writter as IV. Because
the one is before the five we subtract it makeing four. The same principle applies
to the number nine, which is written as IX. There are six instances where subtraction
is used:

    * I can be placed before V (5) and X (10) to make 4 and 9.
    * X can be placed before L (50) and C (100) to make 40 and 90.
    * C can be placed before D (500) and M (1000) to make 400 and 900.

Given an Integer, convert it to a roman numeral. Input is guaranteed to be within
the range from 1 to 3999.

Example 1:

    Input: 3
    Output: 'III'

Example 2:

    Input: 4
    Output: 'IV'

Example 3:

    Input: 9
    Output: 'IX'

Example 4:

    Input: 58
    Output: 'LVIII'
    Explanation: L = 50, V = 5, III = 3

Example 5:

    Input: 1994
    Output: 'MCMXCIV'
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

'''
解题思维：

    1. 9 和 4 是一个比较敏感的位置，在处理过程中，碰到以后处理。
    2.
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        ROMAN_MAP = [
            (('M', 'D', 'C'), 100,),
            (('C', 'L', 'X'), 10,),
            (('X', 'V', 'I'), 1,),
        ]

        r = ''
        for (ten, five, one), f in ROMAN_MAP:
            if num >= f:
                v = num // f
                num -= v * f
                if v >= 10:
                    temp = v // 10
                    r += temp * ten
                    v -= temp * 10
                if v == 9:
                    r += one + ten
                    v -= 9
                if v >= 5:
                    r += five
                    v -= 5
                if v >= 4:
                    r += one + five
                    v -= 4
                if v >= 1:
                    r += v * one
        return r
