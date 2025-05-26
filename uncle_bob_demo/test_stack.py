import pytest

from uncle_bob_demo.stack import Stack
from uncle_bob_demo.stack import UnderflowException


@pytest.fixture
def stack():
    return Stack()


def test_new_stack_is_empty(stack):
    assert stack.is_empty() is True


def test_after_first_push_is_not_empty(stack):
    stack.push(1)
    assert stack.is_empty() is False


def test_pop_empty_stack_raises_exception(stack):
    with pytest.raises(UnderflowException):
        stack.pop()


def test_after_one_push_and_pop_stack_is_empty(stack):
    stack.push(1)
    stack.pop()
    assert stack.is_empty() is True


def test_push_twice_pop_once_stack_is_not_empty(stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    assert stack.is_empty() is False


def test_push_twice_pop_twice_stack_is_empty(stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.is_empty() is True


def test_after_push_x_will_pop_x(stack):
    stack.push(1)
    assert stack.pop() == 1
