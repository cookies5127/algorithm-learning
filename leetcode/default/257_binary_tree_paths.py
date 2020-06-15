from typing import List
from utils import build_binary_tree
from utils.types import TreeNode

'''
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

   1
 /   \
2     3
 \
   5


Ouput: ['1->2->5', '1->3']

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

EXAMPLES = [
    (
        build_binary_tree(*[1, 2, 3, None, 5]),
        ['1->2->5', '1->3'],
    ),
]


class Solution:
    def get_tree_paths(self, root: TreeNode) -> List[List[str]]:
        nodes = []
        if root:
            if root.left is None and root.right is None:
                nodes.append(
                    [str(root.val)]
                )
            else:
                left_results = self.get_tree_paths(root.left)
                if left_results:
                    nodes += [
                        [str(root.val)] + l
                        for l in left_results
                    ]

                right_results = self.get_tree_paths(root.right)
                if right_results:
                    nodes += [
                        [str(root.val)] + r
                        for r in right_results
                    ]
        return nodes

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        results = self.get_tree_paths(root)
        return ['->'.join(r) for r in results]
