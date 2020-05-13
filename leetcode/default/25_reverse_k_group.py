from utils import build_list_node
from utils.types import ListNode


'''
25. Reverse Nodes in k-Group

Given a linked list. reverse the nodes of a linked list k at a time and return its
modified list.

k is a positive integer and is less than or equal to the length of the linked list.
if the number or nodes is not multiple to k then left-out nodes in the end should
remain as it is.

Example:

Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:

    * Only constant extra memory is allowed.
    * You may not after the values in the list's nodes, only nodes itself may be
      changed.
'''

'''
解题思路：

    1. 属于第24题的变种，在核心判断的位置处理一下就可以了。

'''


EXAMPLES = [
    (
        (build_list_node(1, 2, 3, 4, 5), 2),
        build_list_node(2, 1, 4, 3, 5),
    ),
    (
        (build_list_node(1, 2, 3, 4, 5), 3),
        build_list_node(3, 2, 1, 4, 5),
    ),
]


class Solution:
    def reverse(self, head):
        arrays = []

        node = head
        while node:
            arrays.insert(0, node)
            node = node.next

        new_node = ListNode(0)
        temp = new_node
        for n in arrays:
            n.next = None
            temp.next = n
            temp = temp.next

        return new_node.next, arrays[-1]

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        i = 0

        r = head

        node = head
        prev_node = None
        start_node = node
        while node is not None:
            if (i + 1) % k == 0:
                next_node = node.next
                node.next = None
                new_node, end_node = self.reverse(start_node)

                if prev_node:
                    prev_node.next = new_node
                    end_node.next = next_node

                else:
                    r = new_node
                    end_node.next = next_node

                node = end_node
                start_node = node.next
                prev_node = end_node

            i += 1

            node = node.next

        return r
