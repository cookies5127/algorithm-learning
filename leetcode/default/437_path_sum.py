from typing import List
from utils import build_binary_tree
from utils.types import TreeNode

'''
437. Path Sum III

You are given a binary tree in which each more contains an integers value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in range -1,000,000
to 1,000,000.

Example:

    root = [10, 5, -3, 3, 3, null, 11, 3, -2, null, 1], sum = 8
                 10
                /  \
               5    -3
             /   \     \
            3     2    11
           / \     \
          3  -2     1

    Return 3. The paths tha sum to 8 are:

    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11

'''

'''
总结：

    1. 前序遍历，target = sum - node.val，分别从左子树和右子树中寻找新的路径。
    2. 左右子树均有可能找出符合要求的路径
    3. 符合要求的答案中，可能还存在余下节点和为 0 的情况，这种情况是一个新的正确路径
'''


EXAMPLES = [
    # (
    #     (build_binary_tree(*[10, 5, -3, 3, 3, None, 11, 3, -2, None, 1]), 8),
    #     3,
    # ),
    (
        (build_binary_tree(*[1, -2, -3, 1, 3, -2, None, -1]), -1),
        4
    )
]


class Solution:

    def path_sum(self, node: TreeNode, sum: int) -> List[TreeNode]:
        count = 0
        if node:
            target = sum - node.val
            if target == 0:
                count += 1

            count += self.path_sum(node.left, target)
            count += self.path_sum(node.right, target)

        return count

    def pathSum(self, root: TreeNode, sum: int) -> int:
        r = 0
        if root:
            r += self.path_sum(root, sum)

            r += self.pathSum(root.left, sum)

            r += self.pathSum(root.right, sum)

        return r
