from typing import List

'''
78. Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: nums = [1, 2, 3]
    Output:
    [
        [3],
        [1],
        [2],
        [1, 2, 3],
        [1, 3],
        [2, 3],
        [1, 2],
        [],
    ]
'''

'''
总结

   1. 空集也属于子集
'''

EXAMPLES = [
    (
        [1, 2, 3],
        [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            [],
        ],
    ),
]


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)

        results: List[List[int]] = []

        for i, num in enumerate(nums):
            results.append([num])

            j = i + 1
            if nums_length - j > 0:
                results += [
                    sum([[num], r], [])
                    for r in self.subsets(nums[j:]) if r
                ]

        if [] not in results:
            results.append([])

        return results
