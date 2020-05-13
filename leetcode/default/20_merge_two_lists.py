import math
from utils import build_list_node
from utils.types import ListNode


'''
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be
made by splicing together the nodes of the first two lists.

Example:

    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
'''

'''
解题思路：

    1. 归并排序的链表实现
'''

EXAMPLES = [
    (
        (build_list_node(1, 2, 4), build_list_node(1, 3, 4)),
        build_list_node(1, 1, 2, 3, 4, 4),
    ),
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
