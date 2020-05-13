from typing import List
import math
from utils import build_list_node
from utils.types import ListNode

'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe
its complexity.

Example:

    Input:
    [
        1->4->5,
        1->3->4,
        2->6,
    ]
    Output: 1->1->2->3->4->5->6
'''

'''
解题思路：

    1. 使用分治法将问题分解为两两合并，可以解决该题，效率可能不高。
'''

EXAMPLES = [
    (
        [
            build_list_node(1, 4, 5),
            build_list_node(1, 3, 4),
            build_list_node(2, 6),
        ],
        build_list_node(1, 1, 2, 3, 4, 5, 6),
    )
]


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = ListNode(0)
        temp = n

        node1 = l1
        node2 = l2
        while not (node1 is None and node2 is None):
            node1_val = node1.val if node1 else math.inf
            node2_val = node2.val if node2 else math.inf
            if node1_val < node2_val:
                v = node1_val
                node1 = node1.next
            else:
                v = node2_val
                node2 = node2.next

            temp.next = ListNode(v)
            temp = temp.next

        return n.next

    def merge_sort(self, lists: List[ListNode], low: int, high: int) -> ListNode:
        if high < low:
            return None
        elif low == high:
            return lists[low]
        else:
            mid = int((low + high) / 2)
            left = self.merge_sort(lists, low, mid)
            right = self.merge_sort(lists, mid + 1, high)

            return self.mergeTwoLists(left, right)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.merge_sort(lists, 0, len(lists) - 1)
