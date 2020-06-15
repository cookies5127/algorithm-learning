from utils import build_binary_tree
from utils.types import TreeNode


'''
面试题 04. Check Balance LCCI

Implement a function to check if a binary tree is balanced. For the purposes of this
question, a balanced tree is to be a tree such that the heights of the two subtrees
of any node never differ by more than one.

Example 1:

    Given tree [3, 9, 20, null, null, 15, 7]
      3
     / \
    9   20
       /  \
      15   7

    return true.

Example 2:

    Given [1, 2, 2, 3, 3, null, null, 4, 4]
          1
         / \
        2   2
       / \
      3   3
     / \
    4   4

    return false.
'''

'''
总结：

    1. 是否平衡取决于某节点左子树高度与右子树高度相差最多为1，也就是
       left_height - right_height in [-1, 0, 1]
'''


EXAMPLES = [
    (
        build_binary_tree(*[1, None, 2, None, 3]), False,
    ),
    (
        build_binary_tree(3, 9, 20, None, None, 15, 7), True,
    ),
    (
        build_binary_tree(*[1, 2, 2, 3, 3, None, None, 4, 4]), False,
    ),
    (
        build_binary_tree(*[1, 2, 2, 3, None, None, 3, 4, None, None, 4]), False,
    )
]


class Solution:

    def get_depth_from_node(self, node: TreeNode) -> int:
        adj = 1 if node else 0

        left_depth = 0
        if node and node.left:
            left_depth += self.get_depth_from_node(node.left)

        right_depth = 0
        if node and node.right:
            right_depth += self.get_depth_from_node(node.right)

        return max(left_depth, right_depth) + adj

    def is_balance(self, node: TreeNode) -> bool:
        left_depth = self.get_depth_from_node(node.left)
        right_depth = self.get_depth_from_node(node.right)

        return left_depth - right_depth in [-1, 0, 1]

    def isBalanced(self, root: TreeNode) -> bool:
        r = True
        if root:
            r = self.is_balance(root)
            if r and root.left:
                r = self.isBalanced(root.left)
            if r and root.right:
                r = self.isBalanced(root.right)

        return r
