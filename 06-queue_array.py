# 使用数组实现一个队列

class Array(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.length = 0
        self._item = [None] * maxsize

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self._item[index]

    def __setitem__(self, index, value):
        self._item[index] = value

    def clear(self):
        for index in range(len(self._item)):
            self._item[index] = None

    def __iter__(self):
        for i in self._item:
            yield i

class FullError(Exception):
    pass


# 开始实现
class ArrayQueue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError("it's full")
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

def test_array_queue():
    import pytest
    q = ArrayQueue(5)
    for i in range(5):
        q.push(i)

    with pytest.raises(FullError) as excinfo:
        q.push(5)
    assert "full" in str(excinfo.value)

    assert q.pop() == 0
    assert q.pop() == 1

    assert len(q) == 3
    q.push(5)

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5
    print("测试通过")


test_array_queue()
