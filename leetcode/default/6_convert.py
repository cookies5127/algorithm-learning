'''
6. ZigZag Conversion

The string 'PAYPALISHIRING' is written in a zigzg partter on a given number
of rows like this: (you may want to display this pattern in a fixed font for better
legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: 'PAHNAPLSIIGYIR'

Write the code that will take a string and make this conversion given a number of
rows:

    string convert(string s, int numRows)

Example 1:

    Input: s = 'PAYPALISHIRING', numRows = 3
    Output: 'PAHNAPLSIIGYIR'

Example 2:

    Input: s = 'PAYPALISHIRING', numRows = 4
    Output: 'PINALSIGYAHRPI'
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I

'''

'''
解题思路：

    1. Z字形排列以后，每行每个字符间隔多少个字符是可以预知的。根据行号和是不是对角线，可以知道
       下一个字符是谁。
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arrays = []

        string_length = len(s)
        if numRows == 1:
            return s
        for line in range(1, numRows + 1):
            key = line
            step_one = 2 * (numRows - line + 1) - 2
            step_two = 2 * line - 2

            try:
                arrays.append(s[key - 1])
            except IndexError as e:
                pass

            while (step_one or step_two) and key < string_length:
                if step_one != 0:
                    key += step_one
                    try:
                        arrays.append(s[key - 1])
                    except IndexError as e:
                        pass

                if step_two != 0:
                    key += step_two
                    try:
                        arrays.append(s[key - 1])
                    except IndexError as e:
                        pass

        return ''.join(arrays)
