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
    3. 如果是在循环中取字符串的话，奇数和偶数需要分开来看，既可能存在奇数的情况，也可能存在偶数

'''

EXAMPLES = [
    (('babad',), 'bab'),
    (('cbbd',), 'bb'),
]


class Solution1:
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


class Solution:
    '''
        1. max_len 不断增加，每次截取的 s 片段也在不断增长。
        2. 如果 max_len 为奇数，sub1 长度为奇数；如果 max_len 为偶数，sub 长度为偶数。
    '''

    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1

        for i in range(len(s)):
            sub1 = s[i-max_len-1:i+1]
            sub2 = s[i-max_len:i+1]

            if i - max_len - 1 >= 0 and sub1 == sub1[::-1]:
                start = i - max_len - 1
                max_len += 2
            if i - max_len >= 0 and sub2 == sub2[::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start+max_len]
