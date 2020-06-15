import copy
from typing import List

'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

    Input: [1, 2, 3]
    Output: [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
'''


EXAMPLES = [
    (
        [1, 2, 3],
        [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ],
    ),
]


class Solution:
    def get_result(self, r: List[int], num: int) -> List[List[int]]:
        results = []

        i = len(r)
        while i >= 0:
            nums = copy.copy(r)
            nums.insert(i, num)
            results.append(nums)

            i -= 1

        return results

    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        for num in nums:
            if not results:
                results = [[num]]
            else:
                results = sum([self.get_result(r, num) for r in results], [])

        return results
