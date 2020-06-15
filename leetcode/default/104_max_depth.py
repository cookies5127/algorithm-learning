# from typing import List
from utils import build_binary_tree
from utils.types import TreeNode


'''
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3, 9, 20, null, null, 15, 7]

     3
    / \
   9   20
      /  \
     15   7

return its depth = 3
'''

EXAMPLES = [
    (build_binary_tree(*[3, 9, 20, None, None, 15, 7]), 3),
]


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root:
            left_depth = 0
            if root.left:
                left_depth += self.maxDepth(root.left)

            right_depth = 0
            if root.right:
                right_depth += self.maxDepth(root.right)

            depth += max(left_depth, right_depth) + 1

        return depth
