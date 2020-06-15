from utils import build_binary_tree
from utils.types import TreeNode

'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

     3
    / \
   9  20
      / \
     15  7

There are two left leaves in the binary tree, with values 9 and 15 respectively.
Return 24.
'''

EXAMPLES = [
    (
        build_binary_tree(*[
            3, 9, 20, None, None, 15, 7,
        ]),
        24,
    )
]


class Solution:

    def check_leavf(self, root: TreeNode) -> bool:
        return root.left is None and root.right is None

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        r = 0
        if root:
            if root.left:
                if self.check_leavf(root.left):
                    r += root.left.val
                else:
                    r += self.sumOfLeftLeaves(root.left)

            if root.right and not self.check_leavf(root.right):
                r += self.sumOfLeftLeaves(root.right)

        return r
