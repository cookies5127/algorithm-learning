from typing import List

'''
39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target
number (target), find all unique combinations in candidates where the candidate
numbers sums to target.

The same repeated number may be choosen from canidates limited number of times.

Note:

    * All numbers (including target) will be positive integers.
    * The solution set must not contain duplicate combinations.

Example 1:

    Input: candidates = [2, 3, 6, 7], target = 7,
    A solution set is:
    [
        [7],
        [2, 2, 3],
    ]

Example 2:

    Input: canidates = [2, 3, 5], target = 8,
    A Solution set is:
    [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5],
    ]
'''


EXAMPLES = [
    (
        ([2, 3, 6, 7], 7),
        [
            [7],
            [2, 2, 3],
        ],
    ),
    (
        ([2, 3, 5], 8),
        [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5],
        ],
    ),
]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        for i, v in enumerate(candidates):
            count = int(target / v)
            for c in range(count, 0, -1):
                new_target = target - c * v
                if new_target == 0:
                    result.append(
                        count * [v]
                    )
                else:
                    sub_results = self.combinationSum(candidates[i+1:], new_target)
                    if len(sub_results):
                        for sub_result in sub_results:
                            result.append(
                                c * [v] + sub_result
                            )

        return result
