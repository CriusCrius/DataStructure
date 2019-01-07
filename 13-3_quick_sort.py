"""
    实现快速排序：找到一个基准线，比基准线小的放一边，大的放另一边
"""
import random


def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot_index = 0
        pivot = seq[pivot_index]
        less_part = [i for i in seq[pivot_index+1:] if i <= pivot]
        great_part = [i for i in seq[pivot_index+1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort():
    seq_list = list(range(10))
    random.shuffle(seq_list)
    # quick_sort(seq_list)
    print("=====排序前的数组=====", seq_list)
    print("=====排序后的数组=====", quick_sort(seq_list))


test_quick_sort()