import math
from typing import Union  # noqa


class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Union[ListNode, None] = None

    def __repr__(self) -> str:
        values = []

        cls: Union[ListNode, None] = self
        while cls:
            values.append(str(cls.val))
            cls = cls.next

        v = '->'.join(values)
        return f'LN: {v}'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def get_tree(self):
        depth = self.get_depth()

        values = [self]
        for i in range(depth):
            n = 2**i - 1
            for node in values[n:]:
                values += [
                    node.left if node else None,
                    node.right if node else None,
                ]

        return [v.val if v else '.' for v in values]

    def show_tree(self):
        values = self.get_tree()

        depth = int(math.log(len(values) + 1, 2))
        for i in range(depth, 0, -1):
            n = depth - i
            for v in values[2**n-1:2**(n+1)-1]:
                print(i*'   ', v, end='')
            print(i*'   ')

    def get_depth_from_node(self, node):
        left_depth = 0
        if node.left:
            left_depth += 1
            left_depth += self.get_depth_from_node(node.left)

        right_depth = 0
        if node.right:
            right_depth += 1
            right_depth += self.get_depth_from_node(node.right)

        return max(left_depth, right_depth)

    def get_depth(self):
        return self.get_depth_from_node(self)

    def __repr__(self) -> str:
        return f'<TreeNode: {self.val}>'


class Node:

    def __init__(self, val, children=None):
        self.val = val
        self.children = children

    def print_tree(self, node, depth=0):
        print(depth*'   ', node.val)
        if node.children:
            for child in node.children:
                self.print_tree(child, depth=depth+1)

    def show_tree(self):
        self.print_tree(self)
