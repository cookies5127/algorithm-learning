from utils import build_list_node
from utils.types import ListNode

'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list
    becomes 1->2->3->5.
'''

'''
解题思路：

    1. 执行到第 n-1 时，交换第 n 个
'''


EXAMPLES = [
    (
        build_list_node(1, 2, 3, 4, 5),
    )
]


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head

        node_map = {}

        i = 0
        while node:
            node_map[i] = node
            node = node.next
            i += 1

        prev_node = node_map.get(i - n - 1)
        next_node = node_map.get(i - n + 1)
        if prev_node is None:
            return next_node

        prev_node.next = next_node

        return head
