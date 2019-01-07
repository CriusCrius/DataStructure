# 使用循环双端链表cdll实现一个栈

# 首先实现cdll

class Node(object):
    def __init__(self, prev=None, next=None, value=None):
        self.prev, self.next, self.value = prev, next, value


class CircularDoubleLinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        if self.root.next is self.root:  # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:    #
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode


class EmptyError(Exception):
    pass


# 接下来实现双端队列dequeue
class Dequeue(CircularDoubleLinkedList):
    def pop(self):
        if len(self) == 0:
            raise EmptyError("empty")
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise EmptyError("empty")
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


# 最后实现stack
class Stack():
    def __init__(self):
        self.deque = Dequeue()

    def __len__(self):
        return len(self.deque)

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def is_empty(self):
        return len(self) == 0


def stack_test():
    stack = Stack()
    for i in range(3):
        stack.push(i)

    assert len(stack) == 3

    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() == 0
    assert stack.is_empty()

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        stack.pop()
    assert "empty" in str(excinfo.value)


if __name__ == '__main__':
    stack_test()
