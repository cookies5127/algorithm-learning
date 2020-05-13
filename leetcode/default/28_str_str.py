'''
28. Implement strStr()

Implement strStr()

Return the index of the first occurrence of needle in baystack, or -1 if needle
is not part of haystack.

Example 1:

    Input: haystack = 'hello', needle = 'll'
    Output: 2

Example 2:

    Input: haystack = 'aaaaa', needle = 'bba'
    Output: -1

Carification:

What should we return when needle is an empty string? This is a great question
to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr and Java's indexOf().
'''

EXAMPLES = [
    (
        ('hello', 'll'), 2,
    ),
    (
        ('aaaaaa', 'bba'), -1,
    ),
]


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        r = -1

        h_length = len(haystack)
        length = len(needle)
        i = 0

        while i + length <= h_length:
            match_string = haystack[i:i+length]
            if match_string == needle:
                r = i
                break
            else:
                i += 1

        return r
