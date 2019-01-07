"""
    分治法与归并排序
"""
import random


def merger_sort(seq):

    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq)/2)
        left_half = merger_sort(seq[:mid])  # 其实就是切片
        right_half = merger_sort(seq[mid:])
        # 合并两个有序的数组
        new_seq = merger_sort_list(left_half, right_half)
        return new_seq


def merger_sort_list(left_seq, right_seq):
    length_a, length_b = len(left_seq), len(right_seq)
    a = b = 0
    new_sorted_seq = list()
    while a < length_a and b < length_b:
        if left_seq[a] < right_seq[b]:
            new_sorted_seq.append(left_seq[a])
            a += 1
        else:
            new_sorted_seq.append(right_seq[b])
            b += 1

    while a < length_a:
        new_sorted_seq.append(left_seq[a])
        a += 1

    while b < length_b:
        new_sorted_seq.append(right_seq[b])
        b += 1

    return new_sorted_seq


def test_merger_sort():
    seq_list = list(range(10))
    random.shuffle(seq_list)
    print("=====排序前的数组=====", seq_list)
    print("=====排序后的数组=====", merger_sort(seq_list))


test_merger_sort()