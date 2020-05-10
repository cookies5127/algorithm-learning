from .types import ListNode


def build_list_node(*args: int) -> ListNode:
    n = ListNode(0)
    temp = n
    for v in args:
        temp.next = ListNode(v)
        temp = temp.next

    return n.next if n.next else n
