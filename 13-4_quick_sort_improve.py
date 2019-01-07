# 实现1
def quick_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        pivot_index = 0
        pivot = seq[0]
        less_part = [i for i in seq[pivot_index+1:] if i < pivot]
        great_part = [i for i in seq[pivot_index+1:] if i >= pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def quick_sort_test():
    array = [6,1,7,31,2,9,10,5]
    print(quick_sort(array))


quick_sort_test()


print("=========================")


"""
    13-3中的快排，其空间和时间复杂度较大，因为:
        1. less_part和great_part要存储在另外两个列表中，需要额外的存储空间
        2. 这种partition每次都要两次遍历整个数组

    下面是改进方案
"""


# 先进行partition分割操作：将比主元小的放在一边，主元大的放另一边，通常使用第一个元素作为主元pivot
def partition(array, beg, end):
    pivot_index = beg   # 将第一个元素作为主元
    pivot = array[pivot_index]
    left = beg + 1
    right = end - 1

    while True:
        if left <= right and array[left] < pivot:
            left += 1

        if right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def quicksort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quicksort_inplace(array, beg, pivot)
        quicksort_inplace(array, pivot+1, end)


def quicksort_inplace_test():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print("排序前的列表", seq)
    quicksort_inplace(seq, 0, len(seq))
    print("排序后的列表", seq)


quicksort_inplace_test()