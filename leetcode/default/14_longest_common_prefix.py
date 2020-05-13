from typing import List

'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string ''.

Example 1:

    Input: ['flower', 'flow', 'flight']
    Output: 'fl'

Exmaple 2:

    Input: ['dog', 'racecar', 'car']
    Output: ''
    Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
'''

'''
解题思路：

    1. 从数组中不断去寻找两个词最大相同前缀。
    2. 如果按顺序循环迭代数组，时间复杂度为 O(n)

待解决问题：

    1. 该算法的时间复杂度
'''


class Solution:
    def getPrefix(self, strs: List[str], low: int, high: int) -> str:
        if high < low:
            return ''
        elif low == high:
            return strs[low]
        else:
            mid = int((low + high) / 2)
            l_str = self.getPrefix(strs, low, mid)
            r_str = self.getPrefix(strs, mid + 1, high)

            r = ''
            if l_str and r_str:
                r = min(l_str, r_str)
                while not (l_str.startswith(r) and r_str.startswith(r)):
                    r = r[0:-1]
            return r

    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.getPrefix(strs, 0, len(strs) - 1)
