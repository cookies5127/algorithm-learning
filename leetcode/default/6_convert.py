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
    2. 期待能够从字符所处位置来判断，该值属于哪行。
'''

EXAMPLES = [
    (
        ('PAYPALISHIRING', 3),
        'PAHNAPLSIIGYIR',
    ),
    (
        ('PAYPALISHIRING', 4),
        'PINALSIGYAHRPI',
    ),
    (
        ('PAYPALISHIRING', 1),
        'PAYPALISHIRING',
    ),
]


class Solution1:
    '''
        1. 值存在两种，在垂直的竖排中和在对角线上，除了第一排和最后一排，其它的都有存在对角线
    '''
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        r = ''
        string_length = len(s)
        for line in range(numRows):
            key = line

            step_one = 2 * (numRows - line - 1)
            step_two = 2 * line

            if key <= string_length - 1:
                r += s[key]

            while (step_one or step_two) and key < string_length:
                if step_one != 0:
                    key += step_one
                    if key <= string_length - 1:
                        r += s[key]

                if step_two != 0:
                    key += step_two
                    if key <= string_length - 1:
                        r += s[key]

        return r


class Solution:
    '''
        LeetCode 上的高级答案，确实高明。
        最根本的规律就是题目本身的意思，只要把它分到对应的行号内，就可以了。
        到最后一行的时候，往前面的行里分配数据即可。
    '''

    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        r = ['' for _ in numRows]

        i = 0
        flag = 1
        for v in s:
            r[i] += v
            i += flag
            if i == numRows - 1 or i == 0:
                flag = -flag
        return ''.join(r)
