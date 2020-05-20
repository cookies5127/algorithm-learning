'''
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:

    Input: 121
    Output: true

Example 2:

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it
    becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

'''

'''


class Solution1:
    '''
        纯粹为了过的一种解法
    '''

    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_palindrome = x_str[::-1]

        return x_str == x_palindrome


class Solution:
    def isPalindrome(self, x: int) -> bool:
        flag = -1 if x < 0 else 1
        res = flag * int(str(abs(x))[::-1])
        return res if (-2 ** 31) <= res <= (2 ** 31 - 1) else 0
