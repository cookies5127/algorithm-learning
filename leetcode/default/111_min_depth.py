from utils import build_binary_tree
from utils.types import TreeNode

'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum its the numbers of nodes along the shortest path from the
root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Exmalpe:

Given binary tree [3, 9, 20, null, null, 15, 7]

     3
    / \
   9   20
       / \
      15  7

return its minimum depth = 2.
'''

'''
总结：

    1. 最小深度是根结点到最近叶子结点的深度，不包括根结点本身。
    2. 根结点如果存在左右子树，


         -9
        /   \
      -3     2
        \   / \
         4 4   0
        /  /
       -6  -5
'''

EXAMPLES = [
    (build_binary_tree(*[3, 9, 20, None, None, 15, 7]), 2),
    (build_binary_tree(*[1, 2]), 2),
    (build_binary_tree(*[-9, -3, 2, None, 4, 4, 0, -6, None, -5]), 3)
]


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        r = 0
        if root:
            r += 1

            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)

            if left_depth and right_depth:
                r += min(left_depth, right_depth)
            elif left_depth:
                r += left_depth
            elif right_depth:
                r += right_depth

        return r
