from typing import List

'''
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore
the length is 4.
'''


EXAMPLES = [
    ([10, 9, 2, 5, 3, 7, 101, 10], 4),
]


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1] * size
        for i in range(1, size):
            for j in range(i, size):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j])
