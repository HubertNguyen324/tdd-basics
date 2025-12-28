import pytest

from .stack import Stack, UnderflowException


@pytest.fixture
def stack() -> Stack:
    return Stack()


def test_instantiation(stack: Stack):
    assert isinstance(stack, Stack)


def new_stack_is_empty(stack: Stack):
    assert stack.is_empty() is True


def after_first_push_is_not_empty(stack: Stack):
    stack.push(1)
    assert stack.is_empty() is False


def push_none_raises_exception(stack: Stack):
    with pytest.raises(ValueError):
        stack.push(None)  # type: ignore


def pop_empty_stack_raises_exception(stack: Stack):
    with pytest.raises(UnderflowException):
        stack.pop()


def after_one_push_and_pop_stack_is_empty(stack: Stack):
    stack.push(1)
    stack.pop()
    assert stack.is_empty() is True


def push_twice_pop_once_stack_is_not_empty(stack: Stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.is_empty() is False


def push_twice_pop_twice_stack_is_empty(stack: Stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty() is True


def after_push_x_will_pop_x(stack: Stack):
    stack.push(1)
    assert stack.pop() == 1


def test_push_two_elements_then_pop_sequentially(stack: Stack):
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_peek(stack: Stack):
    stack.push(1)
    assert stack.peek() == 1
    stack.push(2)
    assert stack.peek() == 2


def peek_an_empty_stack_raise_exception(stack: Stack):
    with pytest.raises(UnderflowException):
        stack.peek()
