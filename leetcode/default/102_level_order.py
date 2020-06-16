from typing import List
from utils import build_binary_tree
from utils.types import TreeNode

'''
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from
left to right, level by level).

For example:
Given binary tree [3. 9. 20. null, null, 15, 7],

    3
  /   \
 9     20
      /  \
     15   7

return its level order traversal as:

[
    [3],
    [9, 20],
    [15, 7],
]
'''


EXAMPLES = [
    (
        build_binary_tree(*[3, 9, 20, None, None, 15, 7]),
        [
            [3],
            [9, 20],
            [15, 7],
        ],
    ),
]


class Solution:
    '''
    该方法用了递归和修改可变参数的方法，内存耗费较高，实际情况上为了避免内存泄漏，不应该使用该方法
    '''

    def format_level_values(self, root: TreeNode, depth: int, levels: List[List[int]]):
        if root:
            try:
                level = levels[depth]
            except IndexError as e:
                levels.append([])
                level = levels[depth]

            level.append(root.val)
            if root.left:
                self.format_level_values(root.left, depth + 1, levels)

            if root.right:
                self.format_level_values(root.right, depth + 1, levels)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []

        self.format_level_values(root, 0, levels)

        return levels
