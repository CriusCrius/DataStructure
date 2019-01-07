# 线性查找的几种方式

num_list = [9, 8, 4, 7, 3, 8, 1, 6, 5, 8, 0, 4, 7]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):  # 注意index,val的顺序不能错！
        if val == value:
            return index

    return -1


print(linear_search(7, num_list))


# 传入函数predicate
def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1


print(linear_search_v2(lambda x: x == 5, num_list))


# 使用递归实现线性查找
def linear_search_recursion(array, value):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recursion(array[0:index], value)


print(linear_search_recursion(num_list, 5))
