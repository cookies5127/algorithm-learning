from typing import List

'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

    Input: nums = [5, 7, 7, 8, 8, 10], target = 8
    Output: [3, 4]

Example 2:

    Input: nums = [5, 7, 7, 8, 8, 10], target = 6
    Output: [-1, -1]
'''


EXAMPLES = [
    (([5, 7, 7, 8, 8, 10], 8), [3, 4]),
    (([5, 7, 7, 8, 8, 10], 6), [-1, -1]),
]


class Solution:
    def find_cross(self, nums: List[int], low: int, mid: int, high: int, target: int) -> List[int]:
        left = mid
        for i in range(mid, low - 1, -1):
            if nums[i] == target and i < left:
                left = i

            if nums[i] < target:
                break

        right = mid
        for j in range(mid + 1, high + 1):
            if nums[j] == target and j > right:
                right = j

            if nums[j] > target:
                break

        return [left, right]

    def find_result(self, nums: List[int], low: int, high: int, target: int) -> List[int]:
        if low > high:
            return [-1, -1]
        elif low == high:
            return [low, high] if nums[low] == target else [-1, -1]
        else:
            mid = int((low + high) / 2)

            if nums[mid] > target:
                r = self.find_result(nums, low, mid, target)
            elif nums[mid] < target:
                r = self.find_result(nums, mid + 1, high, target)
            elif nums[mid] == target:
                r = self.find_cross(nums, low, mid, high, target)

            return r

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.find_result(nums, 0, len(nums) - 1, target)
