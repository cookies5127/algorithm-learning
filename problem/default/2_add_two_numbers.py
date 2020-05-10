from utils import build_list_node
from utils.types import ListNode

'''
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each or their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Examples:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    OUtput: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
'''

'''
总结：

    1. carry_node = r.next, carry_node = ListNode(0), r.next != carry_node
'''


EXAMPLES = [
    (
        (build_list_node(2, 4, 3), build_list_node(5, 6, 4)),
        build_list_node(7, 0, 8),
    ),
]


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode(0)

        node1 = l1
        node2 = l2

        carry = 0
        carry_node = r
        while node1 or node2 or carry != 0:
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0
            carry += v1 + v2

            v = carry % 10
            carry_node.next = ListNode(v)
            carry_node = carry_node.next

            carry = carry // 10

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        return r.next
