from utils import build_binary_tree
from utils.types import TreeNode

'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its
center).

For example, this binary tree [1, 2, 2, 3, 4, 4, 3] is symmetric:

      1
    /   \
   2     2
  / \   / \
 3   4 4   3



         1
      /     \
     2        2
   /   \    /   \
   3    4  4     3
 /  \  / \
5    6 7  8

But the following [1, 2, 2, null, 3, null, 3] is not:

      1
    /   \
   2     2
    \     \
     3     3
'''


EXAMPLES = [
    (
        None, True,
    ),
    (
        build_binary_tree(*[1, 2, 2, 3, 4, 4, 3]),
        True,
    ),
    (
        build_binary_tree(*[1, 2, 2, None, 3, None, 3]),
        False,
    ),
    (
        build_binary_tree(*[1, 2, 2, None, 3, None, 3]),
        False,
    ),
]


'''
总结：

   1. 某节点的左子树互换位置后与右子树一致，就是队称二叉树
'''


class Solution:

    def is_equal(self, node1, node2):
        r = node1 is None and node2 is None
        if node1 and node2:
            r = node1.val == node2.val
            if r:
                left = self.is_equal(node1.left, node2.right)
                right = self.is_equal(node1.right, node2.left)
                r = left and right
        return r

    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            return self.is_equal(root.left, root.right)
        else:
            return True
