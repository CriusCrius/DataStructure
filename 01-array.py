# 数据结构中的线性结构——数组和列表，线性结构特点：内存连续、可通过下标访问

# 实现一个数组
class Array(object):

    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    arr = Array(10)
    arr[0] = 0
    assert arr[0] == 0

    arr.clear()
    assert arr[0] is None
