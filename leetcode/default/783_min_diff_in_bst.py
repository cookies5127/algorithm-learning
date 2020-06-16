from typing import List
from utils import build_binary_tree
from utils.types import TreeNode

'''
783. Minimum Distance Between BST Nodes

Given a Binary Search Tree (BST) with the root node root, return the minimum
difference between the values of any two different nodes in the tree.

Example:

Input: root = [4, 2, 6, 1, 3, null, null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4, 2, 6, 1, 3, null, null] is represented by the following diagram:

       4
     /   \
    2     6
  /   \
 1     3

while the minimum difference in this tree is 1, it occurs between node 1 and node 2,
also between node 3 and node 2.

Note:

    1. The size of the BST will be between 2 and 100.
    2. The BST is always valid, each node's value is an integer, and each node's
       value is different.
'''


'''
总结：

    1. 二叉搜索树的中序遍历结果就是一个升序数组，所以相邻两数之间可能存在最小差值
'''


EXAMPLES = [
    (
        build_binary_tree(*[
            90, 69, None, 49, 89, None, 52,
        ]),
        1,
    ),
]

'''
         90
        /
      69
     /  \
   49    89
     \
     52
'''


class Solution:

    def get_array(self, root: TreeNode) -> List[int]:
        r = []

        if root:
            if root.left:
                r += self.get_array(root.left)

            r += [root.val]

            if root.right:
                r += self.get_array(root.right)

        return r

    def minDiffInBST(self, root: TreeNode) -> List[int]:
        arr = self.get_array(root)
        if arr:
            ans = float('inf')
            for i, a in enumerate(arr[:-1]):
                ans = min(arr[i + 1] - a, ans)
            return ans
        else:
            return 0
