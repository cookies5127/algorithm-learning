from typing import List

'''
1. Container With Most Water

Given a non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are draw such that the two endpoints of line
i is at (i,ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container the most water.

Note: You may not slant the container and n is at least 2.

Example:

    Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
'''

'''
解题思路：

    1. 尽量寻找较大值来计算
'''

EXAMPLES = [
    (([1, 8, 6, 2, 5, 4, 8, 3, 7],), 49),
]


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_value = 0

        while i < j:
            v = min(height[i], height[j])
            max_value = max(max_value, v * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_value
