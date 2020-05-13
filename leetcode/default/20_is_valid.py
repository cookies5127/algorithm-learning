'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is vaild.

An input string is vaild if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

    Input: '()'
    Output: true

Example 2:

    Input: '(){}[]'
    Output: true

Example 3:

    Input: '(]'
    Output: false

Example 4:

    Input: '([)]'
    Output: false

Example 5:

    Input: '{[]}'
    Output: true
'''

'''
解题思路：

    1. 尝试用动态规划来求解，字符串从左往右，先出现左半边时，期待可以出现对应的右半边。
    2. 如果先出现右半边，或者不是期待得到的右半边，括号不可用。
'''


EXAMPLES = (
    ('()', True),
    ('(){}[]', True),
    ('(]', False),
    ('([)]', False),
    ('{[]}', True),
)


class Solution:

    def isValid(self, s: str) -> bool:
        brakcet_map = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        v = True

        need_match_v = ''
        for i, str in enumerate(s):
            if str in brakcet_map:
                need_match_v = f'{brakcet_map[str]}{need_match_v}'
            elif need_match_v.startswith(str):
                need_match_v = need_match_v[1:]
            else:
                v = False
                break

        if need_match_v:
            v = False

        return v
