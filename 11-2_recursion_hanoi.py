# 使用递归解决汉诺塔问题

"""

    汉诺塔问题：有三根杆子A，B，C。A杆上有N个(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆：
但是有两个条件：
    - 每次只能移动一个圆盘；
    - 大盘不能叠在小盘上面。
"""


def hanoi_move(n, source, dest, intermediate):
    if n >= 1:
        hanoi_move(n - 1, source, intermediate, dest)
        print("move %s -> %s" % (source, dest))
        hanoi_move(n - 1, intermediate, dest, source)


hanoi_move(3, 'A', 'C', 'B')
