# 二分法查找
"""
    注意二分法查找，一定查找的是'有序'的
"""


def binary_search(sorted_array, value):
    if not sorted_array:
        return -1

    begin = 0
    end = len(sorted_array) - 1

    while begin <= end:
        mid = int((begin + end)/2)
        if value == sorted_array[mid]:
            return mid
        elif value > sorted_array[mid]:
            begin = mid + 1
        elif value < sorted_array[mid]:
            end = mid -1
    return -1


a = list(range(10))

print(binary_search(a, 6))
