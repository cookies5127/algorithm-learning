from typing import List

'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., [0, 1, 2, 3, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2])

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Example 2:

    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    Output: -1
'''

EXAMPLES = [
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
]


class Solution:

    def half_find(self, nums: List[int], low: int, high: int, target: int) -> int:
        r = -1
        if low == high:
            if nums[low] == target:
                r = low
        elif high > low:
            mid = int((low + high) / 2)
            if nums[mid] > target:
                r = self.half_find(nums, low, mid, target)
            elif nums[mid] < target:
                r = self.half_find(nums, mid + 1, high, target)
            elif nums[mid] == target:
                r = mid
        return r

    def find_result(self, nums: List[int], low: int, high: int, target: int) -> int:
        if low > high:
            return -1
        elif low == high:
            return low if nums[low] == target else -1
        else:
            mid = int((low + high) / 2)

            if nums[low] > nums[mid]:
                r = self.find_result(nums, low, mid, target)
            else:
                r = self.half_find(nums, low, mid, target)

            if r == -1:
                if nums[mid + 1] > nums[high]:
                    r = self.find_result(nums, mid + 1, high, target)
                else:
                    r = self.half_find(nums, mid + 1, high, target)

            return r

    def search(self, nums: List[int], target: int) -> int:
        return self.find_result(nums, 0, len(nums) - 1, target)
