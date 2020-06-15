from typing import List
from utils import build_tree
from utils.types import Node


'''
590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each
group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:

            1
        /   |    \
       3    2     4
      / \
     5   6

Input: root = [1, null, 3, 2, 4, null, 5, 6]
Ouput: [5, 6, 3, 2, 4, 1]

Example 2:

            1
     /    /    \    \
    2    3      4    5
        / \     |   /  \
       6   7    8  9   10
           |    |  |
           11   12 13
           |
           14

Input: root = [
          1, null, 2, 3, 4, 5, null, null, 6, 7, null,
          8, null, 9, 10, null, null, 11, null, 12, null,
          13, null, null, 14
       ]
Output: [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
'''

'''
总结：

    1. 后序遍历，从左子树开始再到根结点，再到右子树。
'''


EXAMPLES = [
    # (
    #     build_tree(*[
    #         1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10,
    #         None, None, 11, None, 12, None, 13, None, None, 14,
    #     ]),
    #     [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]
    # ),
    (
        build_tree(*[
            1, None, 3, 2, 4, None, 5, 6
        ]),
        [5, 6, 3, 2, 4, 1],
    ),
]


class Solution:
    def postorder(self, root: Node) -> List[int]:
        r = []
        if root:
            if root.children:
                r += sum([
                    self.postorder(child)
                    for child in root.children
                ], [])

            r.append(root.val)

        return r
