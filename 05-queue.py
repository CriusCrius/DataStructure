# 使用单链表实现队列

# 首先实现单链表
class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next

    def __str__(self):
        return '<Node: value:{}, next:{}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        self.root = node
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("it's full")
        node = Node(value=value)
        tailnode = self.tailnode
        if self.root.next is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node    # 更新节点
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("it's full")
        node = Node(value=value)
        headnode = self.root.next
        if self.root.next is None:
            self.root.next = node
        else:
            self.root.next = node
            node.next = headnode
        self.length += 1

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        prevnode = self.root
        curnode = self.root.next
        while curnode is not None:
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1
            else:
                prevnode = curnode
        return -1

    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        if self.root.next is None:
            raise Exception("headnode is none")
        headnode = self.root.next
        self.root.next = headnode.next
        value = headnode.value
        self.length -= 1
        if headnode.next is None:
            self.tailnode = Node

        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


class FullException(Exception):
    print("it's full!")


class EmptyException(Exception):
    print("it's empty!")


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self._item_linked_list) >= self.maxsize:
            raise FullException("queue full")
        return self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyException("queue empty")
        return self._item_linked_list.popleft()


def queue_test():
    queue = Queue()
    queue.push(0)
    queue.push(1)
    queue.push(2)

    assert len(queue) == 3
    assert queue.pop() == 0
    assert queue.pop() == 1
    assert queue.pop() == 2
    # assert 0

    import pytest
    with pytest.raises(EmptyException) as excinfo:
        queue.pop()
    assert 'empty' in str(excinfo.value)
    print("测试完成")


queue_test()



