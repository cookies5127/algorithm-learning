from utils import build_binary_tree
from utils.types import TreeNode

'''
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes
with value between L and R (inclusive)

The binary search tree is guaranteed to have unique values.

Example 1:

    Input: root = [10, 5, 15, 3, 7, null, 18], L = 7, R = 15
    Output: 32

Example 2:

    Input: root = [10, 5, 15, 3, 7, 13, 10, 1, null, 6], L = 6, R = 10
    Output: 23
'''


EXAMPLES = [
    (
        (build_binary_tree(*[10, 5, 15, 3, 7, None, 18]), 7, 15),
        32,
    ),
    (
        (build_binary_tree(*[10, 5, 15, 3, 7, 13, 18, 1, None, 6]), 6, 10),
        23,
    ),
]


class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if root:
            if root.left:
                sum += self.rangeSumBST(root.left, L, R)

            if root.val <= R and root.val >= L:
                sum += root.val

            if root.right:
                sum += self.rangeSumBST(root.right, L, R)

        return sum
