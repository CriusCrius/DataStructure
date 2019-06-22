# 链式结构与线性结构不同：内存不连续、不可以通过下标方式访问
# 实现一个单链接表linkedlist，单链表由根节点(root)、头节点(head)、尾节点(tail)以及中间一个个节点组成，每个节点包含当前节点内容以及指向下一个节点。
# 单链表包含的操作有：查询(find)、追加(append,appendleft)、插入(insert)、删除(remove)、弹出(pop,popleft)、遍历(iter)
# 单链表的几个时间复杂度：append()及appendleft()是O(1)；find()及remove()是O(n)

class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next

    def __str__(self):
        return '<Node: value:{}, next:{}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """ 链接表 ADT
        [root] -> [node0] -> [node1] -> [node2]
    """
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.root = Node()              # 默认 root 节点指向 None
        self.tailNote = None
        self.next = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):            # 时间复杂度O(1)
        if self.maxSize is not None and len(self) > self.maxSize:
            raise Exception("it's full")
        node = Node(value)
        tailNode = self.tailNote
        if tailNode is None:
            self.root.next = node
        else:
            tailNode.next = node
        self.tailNote = node            # 更新最后一个节点
        self.length += 1

    def appendleft(self, value):        # 时间复杂度O(1)，插入到root节点的后边，即在当前头节点前插入一个节点
        if self.maxSize is not None and len(self) > self.maxSize:
            raise Exception("it's full")
        node = Node(value)
        if self.tailNote is None:       # 如果原链表为空，插入第一个元素需要设置 tailnode
            self.tailNote = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        curnode = self.root.next
        while curnode is not self.tailNote:
            yield curnode               # 不断yield出节点
            curnode = curnode.next      # 不断更新节点
        if curnode is not None:
            yield curnode               # 把最后一个节点yield出

    def __iter__(self):                 # 利用iter_node()方法可遍历单链表
        for node in self.iter_node():
            yield node.value

    def remove(self, value):            # 时间复杂度O(n)
        prevnode = self.root
        curnode = self.root.next
        while curnode.next is not None:
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailNote:
                    self.tailNote = prevnode
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1

    def find(self, value):              # 时间复杂度O(n)
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):                  # 将头节点删除，将根节点指向头节点的下一个节点 O(1)
        """
            删除第一个链表节点
        """
        if self.root.next is None:
            raise Exception("headnode is none")
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        if self.tailNote is headnode:      # 若是单节点则删除 tailnode 处理
            self.tailNote = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(0) == 0

    ll.remove(0)
    assert ll.find(0) == -1
    assert len(ll) == 2
    assert list(ll) == [1,2]


if __name__ == '__main__':
    test_linked_list()
