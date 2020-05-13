from typing import List

'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute hwo much water it is able to trap after raining.

Example:

    Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Output: 6
'''

EXAMPLE = [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
]


class Solution:
    def get_trap(self, height: List[int], start: int, end: int) -> int:
        start_value = height[start]
        end_value = height[end]

        trap = 0

        h = min(start_value, end_value)
        for i in range(start + 1, end):
            trap += h - height[i]

        return trap

    def trap(self, heights: List[int]) -> int:
        trap = 0

        start_index = None
        for i, v in enumerate(heights):
            if start_index is None:
                if v > 0:
                    start_index = i
            else:
                if v >= heights[start_index]:
                    trap += self.get_trap(heights, start_index, i)
                    start_index = i

        if start_index is not None and start_index != len(heights) - 1:
            trap += self.trap(heights[start_index:][::-1])

        return trap
