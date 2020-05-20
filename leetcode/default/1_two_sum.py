from typing import List


'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Examples:

    Given nums = [2, 7, 11, 15], target = 9

    Becacuse nums[0] + nums[1] = 2 + 7 = 9
    return [0, 1].
'''

'''
总结：

    1. hash_map 寻找速度大于 array.index
    2. target - nums[i] = new_target，hash_map有两种方式
       a. 当前值是需要找到的 new_target, nums[i] in memeroy
       b. new_target 是否在以前迭代过的某个值，new_target in memeroy
'''


EXAMPLES = [
    (
        ([2, 7, 11, 15], 9),
        [0, 1]
    ),
]


class Solution:
    def twoSum_myself(self, nums: List[int], target: int) -> List[int]:
        r = []
        for i, v in enumerate(nums):
            next_value = target - v
            if next_value in nums[i+1:]:
                r = [i, nums[i+1:].index(next_value) + i + 1]
                break
        return r


class Solution1:
    '''
        用时最小
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memeroy = {}
        for i, v in enumerate(nums):
            if v in memeroy:
                return [memeroy[v], i]
            memeroy[target - v] = i


class Solution2:
    '''
        内存最小
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
