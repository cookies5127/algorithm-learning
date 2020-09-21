from typing import List

'''
45. Jump Game ||

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at the position.

Your goat is to reach the last index in the minimum number of jumps.

Example:

    Input: [2, 3, 1, 1, 4]
    Output: 2
    Explation: The minimum number of jumps to reach the last index is 2.
               Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

'''
解题思路：

    1. 在第一个数字的范围内，找到下一个可以让你跳的更远的数字。
    2. 当前位置加上当前的数字就是可以跳的最远距离，此时可以走的距离不代表当前所处位置。
    3. 0也为非负整数。
    4. 存在第一个数可以直接跳到最后的情况。

总结：

    1. 审题不够清晰，没有从题目中得出需要的信息。
    2. 对待测试要更慎重，多考虑多个可能情况。
'''

EXAMPLES = [
    ([2, 3, 1, 1, 4], 2),
    ([0], 0),
    ([1, 2], 1),
    ([1, 1, 1, 1], 3),
    ([3, 2, 1], 1),
    ([1, 2, 1, 1, 1], 3),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 2),
]


class Solution:

    def jump(self, nums: List[int]) -> int:
        nums_length = len(nums)

        times = 0
        if nums_length > 0:
            index = 0

            while index + 1 < nums_length:
                value = nums[index]
                if value + index + 1 >= nums_length:
                    index = nums_length - 1
                else:
                    t = 0
                    tmp_index = index + 1
                    for i, num in enumerate(nums[tmp_index:tmp_index+value]):
                        if num > 0 and num + i > t:
                            t = num + i
                            index = tmp_index + i

                    print('t: ', t, ' index: ', index)

                times += 1

        return times
