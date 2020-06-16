from utils import build_binary_tree
from utils.types import TreeNode

'''
100. Same Tree

Given two binary tree, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.

Example 1:

Input:     1          1
          / \        / \
         2   3      2   3

Output: true

Exmalpe 2:

Input:    1           1
         /             \
        2               2

Output: false
'''

EXAMPLES = [
    (
        (build_binary_tree(*[1, 2, 3]), build_binary_tree(*[1, 2, 3])),
        True,
    ),
    (
        (build_binary_tree(*[1, 2]), build_binary_tree(*[1, None, 2])),
        False,
    ),
]


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        r = p is not None and q is not None if p or q else True
        if p and q:
            r = p.val == q.val
            if r:
                r = self.isSameTree(p.left, q.left)
            if r:
                r = self.isSameTree(p.right, q.right)

        return r
