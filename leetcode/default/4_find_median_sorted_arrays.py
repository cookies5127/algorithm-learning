from typing import List

'''
4. Median of Two sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(long(m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is 2.5
'''


'''
解题思路：

    中位数是一组数据中，居于中间位置的数，能把数据分为上下两部分。如果该组数据为奇数个，按顺序
    排列以后，找出中间那个，如果为偶数个。就为最中间两个数的平均数。

    两个已经排序后的数组，假设长度为别为 m、n，将其按顺序合并以后。
    如果 m + n 为奇数，nums[(m + n + 1) / 2] 为其中位数；
    如果 m + n 为偶数，(nums[(m + n + 1) // 2] + nums[(m + n + 2) // 2]) / 2 为其中位数。

    主要考查对二分法查找，二分法基本思路是不断缩小范围，最终只剩下结果。由中位数的理论推导可知，
    假设该位置为k，则每个数组中最多 k // 2 个数字小于中位数，不断缩小比较数组的规模和 k 值，
    直到找到最终结果。
'''


EXAMPLES = [
    (
        ([1, 3, 6], [2, 4]),
        3,
    ),
    (
        ([3, 4], [1, 2]),
        2.5,
    ),
]


class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        i = j = 0

        array = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                array.append(nums1[i])
                i += 1
            else:
                array.append(nums2[j])
                j += 1
        if i >= m:
            array += nums2[j:]
        if j >= n:
            array += nums1[i:]

        return (array[(m + n + 1) // 2 - 1] + array[(m + n + 2) // 2 - 1]) / 2


class Solution:

    def findKth(self, nums1: List[int], nums2: List[int], k: int) -> float:
        m = len(nums1)
        n = len(nums2)

        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]

        if k == 1:
            return min(nums1[0], nums2[0])

        i = min(k // 2, m) - 1
        j = min(k // 2, n) - 1

        if nums1[i] > nums2[j]:
            return self.findKth(nums1, nums2[j+1:], k - j - 1)
        else:
            return self.findKth(nums1[i+1:], nums2, k - i - 1)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        l = (m + n + 1) // 2
        r = (m + n + 2) // 2

        left = self.findKth(nums1, nums2, l)
        right = self.findKth(nums1, nums2, r)

        return (left + right) / 2.0
