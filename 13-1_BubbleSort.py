"""
本节要掌握冒泡排序、选择排序、插入排序
"""
import random


# 冒泡：每次循环都可取出一个最小(大)值放在最后，放在最后的值不参与排序，故内层循环要减i。
def bubble_sort(seq):
    if len(seq) <= 1:
        return
    for i in range(len(seq) - 1):
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
        print(seq, "第%i次排序"%(i+1))


def test_bubble_sort():
    seq_list = list(range(10))
    random.shuffle(seq_list)
    print("=====排序前的数组=====", seq_list)
    bubble_sort(seq_list)


test_bubble_sort()

print("===========================选择排序====================")


# 选择排序：每次循环假设当前数为最小，接着循环当前数后的所有数并与当前数比较，从而取得当前的最小值
def select_sort(seq):
    if len(seq) <= 1:
        return
    for i in range(len(seq) - 1):
        min_num = i
        for j in range(i+1 , len(seq)):
            if seq[j] < seq[min_num]:
                min_num = j
        if min_num != i:
            seq[i], seq[min_num] = seq[min_num], seq[i]
        print(seq, "第%i次排序"%(i+1))


def test_select_sort():
    seq_list = list(range(10))
    random.shuffle(seq_list)
    print("=====排序前的数组=====", seq_list)
    select_sort(seq_list)


test_select_sort()


print("============================插入排序=========================")


# 插入排序：确保前i-1项有序排列，接着插入第i项
def insert_sort(seq):
    if len(seq) <= 1:
        return
    for i in range(len(seq)):
        value = seq[i]      # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        pos = i             # 找到这个值的合适位置，使得前边的数组 [0,i] 有序
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]   # 如果前边的元素比它大，就让它一直前移，直到找到合适的位置
            pos -= 1
        seq[pos] = value    # 找到了合适的位置赋值就好
        print(seq, "第%i次排序"%(i+1))


def test_insert_sort():
    seq_list = list(range(10))
    random.shuffle(seq_list)
    print("=====排序前的数组=====", seq_list)
    insert_sort(seq_list)


test_insert_sort()