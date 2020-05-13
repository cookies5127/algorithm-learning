'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of
the longest valid (weel-formed) parentheses substring.

Example 1:

    Input: '(()'
    Output: 2
    Examplation: The longest valid parentheses substring is '()'

Example 2:

    Input: ')()())'
    Ouput: 4
    Explation: The longest vaild parentheses substring is '()()'
'''


EXAMPLES = [
    ('(()', 2),
    (')()())', 4),
]


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        str = []
        b = [0] * len(s)
        for i, val in enumerate(s):
            if val == '(':
                str.append(i)
            elif str:
                b[str.pop()] = 1
                b[i] = 1

        max_length = 0
        count = 0
        for v in b:
            if v:
                count += 1
            else:
                count = 0

            max_length = max(max_length, count)
        return max_length
