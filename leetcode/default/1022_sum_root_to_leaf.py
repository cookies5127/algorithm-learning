from typing import List
from utils import build_binary_tree
from utils.types import TreeNode

'''
1022. Sum of Root to Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1. Each root-to-leaf path represents
a binary number starting with the most significant bit. For example, if the path
is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from root
to that leaf.

Return the sum of these numbers.

Example 1:

        1
      /   \
     0     1
    / \   / \
   0   1 0   1

Input: [1, 0, 1, 0, 1, 0, 1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
'''


EXAMPLES = [
    (build_binary_tree(*[1, 0, 1, 0, 1, 0, 1]), 22),
]


class Solution:
    def get_values(self, root: TreeNode) -> List[str]:
        r = []
        if root:
            if root.left is None and root.right is None:
                r.append(str(root.val))

            if root.left:
                left = self.get_values(root.left)
                if left:
                    r += [
                        str(root.val) + l for l in left
                    ]

            if root.right:
                right = self.get_values(root.right)
                if right:
                    r += [
                        str(root.val) + r for r in right
                    ]

        return r

    def sumRootToLeaf(self, root: TreeNode) -> int:
        result = self.get_values(root)
        return sum([
            int(r, 2)
            for r in result
        ])
