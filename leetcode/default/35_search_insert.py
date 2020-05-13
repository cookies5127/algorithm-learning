from typing import List

'''
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume to duplicates in array.

Example 1:

    Input: [1, 3, 5, 6], 5
    Ouput: 2

Example 2:

    Input: [1, 3, 5, 6], 2
    Output: 1

Example 3:

    Input: [1, 3, 5, 6], 7
    Output: 4

Example 4:

    Input: [1, 3, 5, 6], 0
    Output: 0
'''


EXAMPLES = [
    (([1, 3, 5, 6], 5), 2),
    (([1, 3, 5, 6], 2), 1),
    (([1, 3, 5, 6], 7), 4),
    (([1, 3, 5, 6], 0), 0),
]


class Solution:
    def find_result(self, nums: List[int], low: int, high: int, target: int) -> int:
        if high < low:
            return -1
        elif low == high:
            return low if nums[low] >= target else low + 1
        else:
            mid = int((low + high) / 2)
            if nums[mid] > target:
                r = self.find_result(nums, low, mid, target)
            elif nums[mid] < target:
                r = self.find_result(nums, mid + 1, high, target)
            else:
                r = mid

            return r

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.find_result(nums, 0, len(nums) - 1, target)
