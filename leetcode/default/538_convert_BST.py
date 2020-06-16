from utils import build_binary_tree
from utils.types import TreeNode

'''
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus sum of all keys greater
than the original key in BST.

Example:

    Input: The root of a Binary Search Tree like this:

        5
      /   \
     2     13

    Output: The root of a Greater Tree like this:

          18
         /  \
        20   13

       2
     /   \
    0     3
   / \
  -4  1
'''

'''
总结：

    1. greater 是一个不断遍历不断累加的值
'''


EXAMPLES = [
    # (build_binary_tree(*[5, 2, 13]), build_binary_tree(*[18, 20, 13])),
    (build_binary_tree(*[2, 0, 3, -4, 1]), build_binary_tree(*[[5, 6, 3, 2, 6]])),
]


class Solution:
    def greater_tree(self, root: TreeNode, greater: int) -> TreeNode:
        if root:
            if root.right:
                greater = self.greater_tree(root.right, greater)

            root.val = root.val + greater
            greater = root.val

            if root.left:
                greater = self.greater_tree(root.left, greater)

        return greater

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.greater_tree(root, 0)
        return root
