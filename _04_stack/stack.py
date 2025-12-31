class UnderflowException(Exception):
    pass


class Stack:
    def __init__(self):
        self._size = 0
        self._elements: list[int] = []

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, value: int) -> None:
        if value is None:
            raise ValueError("value cannot be None")

        self._elements.append(value)
        self._size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise UnderflowException
        self._size -= 1

        return self._elements.pop()

    def peek(self) -> int:
        if self.is_empty():
            raise UnderflowException
        return self._elements[-1]
