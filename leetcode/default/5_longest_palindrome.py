'''
5. Longest Palindromic SubString

Given a string s, find the longest palindromic substring in s. You may assume that
the maximum length of s is 1000.

Example 1:

    Input: 'babad'
    Output: 'bab'
    Note: 'aba' is also a vaild answer

Example 2:

    Input: 'cbbd'
    Ouput: 'bb'
'''

'''
解题思路：

    1. 字符串正序等于字符串逆序
    2. 最终结果如果为奇数，要考虑最中间的字符；为偶像，字符串分为等长的两个字符串，互为逆序。

'''

EXAMPLES = [
    (('babad',), 'bab'),
    (('cbbd',), 'bb'),
]


class Solution:
    '''
        以字符串长度开始迭代查询，属于暴力求解。
    '''
    def longestPalindrome(self, s: str) -> str:
        final_result = None

        string_length = len(s)
        length = string_length
        while final_result is None:
            start = 0
            while start + length <= string_length:
                str = s[start:start+length]
                if str == str[::-1]:
                    final_result = str
                    break
                else:
                    start += 1

            length -= 1

        return final_result
