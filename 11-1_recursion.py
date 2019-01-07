# 递归
"""
    本节用栈模拟递归
"""
from collections import deque


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    stack = Stack()
    while n > 0:
        stack.push(n)
        n -= 1

    while not stack.is_empty():
        print(stack.pop())


print_num_use_stack(10)
