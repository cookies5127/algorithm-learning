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
