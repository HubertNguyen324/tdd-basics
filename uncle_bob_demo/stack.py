class UnderflowException(Exception):
    pass


class Stack:
    def __init__(self):
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, value: int) -> None:
        self.element = value
        self.size += 1

    def pop(self) -> int:
        if self.is_empty():
            raise UnderflowException
        self.size -= 1

        return self.element
