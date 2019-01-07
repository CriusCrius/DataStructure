# 使用lru cache最近最少使用算法，并使用装饰器

# 下面是自己的实现，很复杂。。
'''
class fit(object):
    def __init__(self, a=0, b=0, max=0):
        self.a = a
        self.b = b
        self.max = max

    def cal(self):
        i = 0
        while i < self.max:
            self.a, self.b = self.b, self.a + self.b
            print(self.b)
            i += 1
        return self.b


if __name__ == '__main__':
    fit = fit(1, 1, 10)
    fit.cal()
    # print(fit.cal())
'''

# 下面是较为简洁版的
'''
def cache(func):
    data = {}

    def wrapper(n):
        if n in data:
            return data[n]
        else:
            res = func(n)
            data[n] = res
            return res

    return wrapper


@cache
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 10):
    print(fib(i))
'''


# 若内存有限则需要使用lru
class Node(object):
    def __init__(self, prev=None, next=None, key=None, value=None):
        self.prev, self.next, self.key, self.value = prev, next, key, value


class CircularDoubleLinkedList(object):
    def __init__(self):
        node = Node()
        node.prev, node.next = node, node
        self.rootnode = node

    def headnode(self):
        return self.rootnode.next

    def tailnode(self):
        return self.rootnode.prev

    def remove(self, node):
        if node is self.rootnode:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def append(self, node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.rootnode
        self.rootnode.prev = node


class LRUcache(object):
    def __init__(self, maxsize=16):
        self.maxsize = maxsize
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= self.maxsize

    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:
                self.access.remove(cachenode)
                self.access.append(cachenode)
                return cachenode.value
            else:
                value = func(n)
                if not self.isfull:
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode, self.access.rootnode, n, value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                    self.isfull = len(self.cache) >= self.maxsize
                    return value
                else:
                    lru_node = self.access.headnode()
                    del self.cache[lru_node.key]
                    self.access.remove(lru_node)
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode, self.access.rootnode, n, value)
                    self.access.append(newnode)
                    self.cache[n] = newnode
                return value

        return wrapper


@LRUcache()
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 10):
    print(fib(i))
