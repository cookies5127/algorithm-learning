from typing import List, Dict

'''
1471.
'''

'''
解题思路：

    1. 排序数组后求出中位数
    2. 根据中位数，由数组本来的值和 abs(v - median) 进行排序

TODO:

    1. 自己设计排序算法，包括值相等两个数本身不等的状况
'''

EXAMPLES = [
    (
        ([1, 2, 3, 4, 5], 2),
        [5, 1]
    ),
    (
        ([6, 7, 11, 7, 6, 8], 5),
        [11, 8, 6, 6, 7],
    ),
    (
        ([-7, 22, 17, 3], 2),
        [22, 17],
    )
]


class Solution:
    def get_median(self, arr: List[int]) -> int:
        new_arr = sorted(arr)
        length = len(new_arr)
        return new_arr[(length - 1) // 2]

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if arr:
            median = self.get_median(arr)

            r = sorted(arr, key=lambda x: (abs(x - median), x), reverse=True)
            return r[:k]
