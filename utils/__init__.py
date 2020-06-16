from typing import Union, List
from .types import ListNode, TreeNode, Node


def build_list_node(*args: int) -> ListNode:
    n = ListNode(0)
    temp = n
    for v in args:
        temp.next = ListNode(v)
        temp = temp.next

    return n.next if n.next else n


def build_binary_tree(*args: Union[int, None]) -> TreeNode:
    nodes = []

    nodes_length = 1
    start = end = 0

    root_index = None
    while start < len(args):
        end = nodes_length

        for i, v in enumerate(args[start:end]):
            n = TreeNode(v) if v is not None else None
            nodes.append(n)

            if n is not None:
                nodes_length += 2
                if root_index is None:
                    root_index = 0
                else:
                    root = nodes[root_index]
                    if root:
                        if i % 2 == 0:
                            root.left = n
                        elif i % 2 == 1:
                            root.right = n

            if i % 2 == 1:
                root_index += 1
                root = nodes[root_index]
                while root is None and root_index < len(nodes) - 1:
                    root_index += 1
                    root = nodes[root_index]

        start = end

    return nodes[0]


def build_tree(*args: Union[int, None]) -> Node:
    nodes = []

    children = []

    root_index = None
    for value in args + (None,):
        if value is None:
            if root_index is None:
                root_index = 0
            else:
                root = nodes[root_index]
                root.children = children

                root_index += 1

            nodes += children
            children = []
        else:
            children.append(
                Node(value),
            )

    return nodes[0]
