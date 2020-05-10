'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the Longest substring without repeating
characters.

Example 1:

    Input: 'abcabcbb'
    OUtput: 3
    Explanation: The answer is 'abc', with the length of 3.

Example 2:

    Input: 'bbbb'
    Output: 1
    Explanation: The answer is 'b', with the length of 1.

Example 3:

    Input: 'pwwkew'
    Output: 3
    Explanation: The answer is 'wke', with the length of 3.
                 Note that the answer must be a substring.
'''

'''
总结：

    1. 分治法用于缩小问题规模，然后将结果组合起来得到最终结果，部分问题求解就是所需的算法。
    2. 解题需要确定好问题边界条件，何时改变需要改变的值。
'''


EXAMPLES = [
    (('abcabcbb',), 3),
    (('bbbbb',), 1),
    (('pwwkew',), 3),
    (('loddktdji',), 5),
]


class Solution1:
    '''
        分治法求解，问题比较多。
        1. 分治法只是减少问题的规模，所以最终是解决出问题，不过是减少了问题规模。
        2. 由于部分边界条件，导致不能在正确的范围内寻找正确答案。
    '''

    def find_mid_max_length(self, s: str, left: int, mid: int, right: int):
        max_left = mid
        max_right = mid

        string = ''

        i = mid
        j = mid + 1
        while i >= left or j <= right:
            if i >= left:
                if s[i] not in string:
                    string += s[i]
                    max_left = i
                    i -= 1
                else:
                    i = left - 1

            if j <= right:
                if s[j] not in string:
                    string += s[j]
                    max_right = j
                    j += 1
                else:
                    j = right + 1

        string = s[max_left:max_right + 1]
        return max_left, max_right, len(string)

    def find_max_length(self, s: str, left: int, right: int):
        if left == right:
            return left, right, 1
        else:
            mid = int((left + right) / 2)

            l_left, l_right, l_length = self.find_max_length(s, left, mid)
            r_left, r_right, r_length = self.find_max_length(s, mid + 1, right)
            c_left, c_right, c_length = self.find_mid_max_length(s, left, mid, right)

            if l_length >= r_length and l_length >= c_length:
                return l_left, l_right, l_length
            elif r_length >= l_length and r_length >= c_length:
                return r_left, r_right, r_length
            else:
                return c_left, c_right, c_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        str_length = len(s)
        if str_length > 0:
            left, right, length = self.find_max_length(s, 0, str_length - 1)
            print(left, right, s[left:right+1])
            return length
        else:
            return 0


class Solution:

    def lengthOfLongestSubstring_myself(self, s: str) -> int:
        max_value = 0
        ans = ''

        j = 0
        length = len(s)
        while j < length:
            v = s[j]
            if v in ans:
                max_value = max(len(ans), max_value)
                k = ans.index(v)
                ans = ans[k+1:]
            else:
                ans += v
                j += 1

        max_value = max(len(ans), max_value)
        return max_value
