from utils import build_list_node
from utils.types import ListNode

'''
24. Swap Noeds in Pairs

Given a linked list, swap every two adjacent nodes and return ints head.

You may not modify the values in the list's node, only ondes itself may be changed.

Example:

    Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

'''
解题思路：

    1. 交换偶数位置的节点，中间的位置存在上下关系。
    2.
'''


EXAMPLES = [
    (
        build_list_node(1, 2, 3, 4),
        build_list_node(2, 1, 4, 3),
    ),
]


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return []

        node = head.next
        if node is None:
            r = head
        else:
            head.next = node.next
            node.next = head

            r = node

        i = 1
        while node is not None:
            prev_node = node
            node = node.next if node else None
            next_node = node.next if node else None

            if i % 2 == 0 and next_node:
                node.next = next_node.next
                prev_node.next = next_node
                next_node.next = node

                node = next_node

            i += 1

        return r
