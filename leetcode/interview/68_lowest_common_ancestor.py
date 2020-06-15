from typing import List
from utils import build_binary_tree
from utils.types import TreeNode


'''
面试题68. 二叉搜索树的最近公共祖先 LCOF

给定一个二叉搜索树，找到该树中两个指定节点的最近公共祖先。

最近的公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是
p、q 的祖先且 x 的深度尽可能大（一个结点也可以是它自己的祖先）。”

例如，给定如下的二叉搜索树： root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]

             6
           /   \
         2        8
        /  \     /  \
       0    4   7    9
           / \
          3   5

Example 1:

Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
Output: 6
Explation: 结点 2 和结点 8 的最近公共祖先是 6

            6
         /    \
        2       8
      /   \    /  \
     0     4  7    9
          / \
         3   5

Example 2:

Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
Output: 2
Explation: 结点 2 和结点 4 的最近公共祖先是 2，因为根据定义最近公共祖先结点可以为结点本身。
'''

'''
总结：

    1. 深度尽可能大，表示它距离两个结点尽可能近。
    2. 二叉搜索树导致每个结点都有通往根结点的唯一路径，不同的结点之间路径存在重合的部分。
'''

BINARY_TREE_NODE = build_binary_tree(*[
    6, 2, 8, 0, 4, 7, 9, None, None, 3, 5
])

EXAMPLES = [
    (
        (
            BINARY_TREE_NODE,
            BINARY_TREE_NODE.left,
            BINARY_TREE_NODE.right,
        ),
        BINARY_TREE_NODE,
    ),
    (
        (
            BINARY_TREE_NODE,
            BINARY_TREE_NODE.left,
            BINARY_TREE_NODE.left.right,
        ),
        BINARY_TREE_NODE.left,
    ),
    (
        (
            BINARY_TREE_NODE,
            BINARY_TREE_NODE.left.left,
            BINARY_TREE_NODE.left.right,
        ),
        BINARY_TREE_NODE.left,
    )
]


class Solution:
    def get_path_nodes(self, root: TreeNode, node: TreeNode) -> List[TreeNode]:
        r = []
        if node:
            r.append(root)
            if node.val < root.val:
                r += self.get_path_nodes(root.left, node)
            elif node.val > root.val:
                r += self.get_path_nodes(root.right, node)
        return r

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = self.get_path_nodes(root, p)

        q_path = self.get_path_nodes(root, q)

        nodes = []

        i = 0
        while i < len(p_path) and i < len(q_path):
            p_node = p_path[i]
            q_node = q_path[i]

            if p_node in q_path and q_node in p_path:
                nodes.append(p_node)
            else:
                break

            i += 1

        return nodes[-1] if nodes else None
