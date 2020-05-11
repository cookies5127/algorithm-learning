'''
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol          Value
I                1
V                5
X                10
L                50
C                100
D                500
M                1000

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is
written as XXVII, which XX + V + II.

Roman numberals are usually written
'''


EXAMPLES = [
    (('III',), 3),
    (('IV',), 4),
    (('IX',), 9),
    (('LVIII',), 58),
    (('MCMXCIV',), 1994),
]


class Solution:
    def get_count(self, f: str, str: str) -> int:
        i = 1
        while str.startswith(i * f):
            i += 1
        return i - 1

    def romanToInt(self, s: str) -> int:
        ROMAN_MAP = [
            (('M', 'D', 'C'), 100,),
            (('C', 'L', 'X'), 10,),
            (('X', 'V', 'I'), 1,),
        ]

        v = 0
        for (ten, five, one), f in ROMAN_MAP:
            if s.startswith(ten):
                count = self.get_count(ten, s)
                v += count * 10 * f
                s = s[count:]

            if s.startswith(one+ten):
                v += 9 * f
                s = s[2:]

            if s.startswith(five):
                v += 5 * f
                s = s[1:]

            if s.startswith(one+five):
                v += 4 * f
                s = s[2:]

            if s.startswith(one):
                count = self.get_count(one, s)
                v += count * f
                s = s[count:]

        return v
