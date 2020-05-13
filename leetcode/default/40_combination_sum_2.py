'''
40, Combination Sum II

Given a collection of candidate numers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to
target.

Each number in candidates may only be used once in the combination.

Note:

    * All numbers (including target) will be positive integers.
    * The solution set must not contain duplicate combinations.

Example 1:

    Input: canditates = [10, 1, 2, 7, 6, 1, 5], target = 8
    A solution set is:
    [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6],
    ]

Example 2:

    Input: candidates = [2, 5, 2, 1, 2], target = 5
    A solution set is:
    [
        [1, 2, 2],
        [5],
    ]
'''

EXAMPLES = [
    (
        ([10, 1, 2, 7, 6, 1, 5], 8),
        [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6],
        ],
    ),
    (
        ([2, 5, 2, 1, 2], 5),
        [
            [1, 2, 3],
            [5],
        ],
    ),
]


class Solution:
    def combination(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        for i, v in enumerate(candidates):
            if v <= target:
                new_target = target - v
                if new_target == 0:
                    result.append([v])
                else:
                    sub_results = self.combination(candidates[i+1:], new_target)
                    if sub_results:
                        result += [
                            [v] + r
                            for r in sub_results
                        ]
        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = self.combination(candidates, target)
        result = set(tuple(r) for r in result)
        return [list(r) for r in result]
