"""
    本节掌握二叉树的代码实现

    - 节点深度(depth): 节点对应的 level 数字
    - 树的高度(height): 二叉树的高度就是 level 数 + 1，因为 level 从 0开始计算的
    - 树的宽度(width): 二叉树的宽度指的是包含最多节点的层级的节点数
    - 树的 size: 二叉树的节点总个数。
"""

node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


# 首先实现二叉树节点
class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


# 构建二叉树
class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """通过节点信息构造二叉树
        第一次遍历我们构造 node 节点
        第二次遍历我们给 root 和 孩子赋值

        :param node_list: {'data': 'A', 'left': None, 'right': None, 'is_root': False}
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)

        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)

    # 先序遍历：先处理根，之后是左子树，然后是右子树
    def preorder_trav(self, subtree):
        if subtree is not None:
            print(subtree.data)  # 递归函数里先处理根
            self.preorder_trav(subtree.left)  # 递归处理左子树
            self.preorder_trav(subtree.right)  # 递归处理右子树

    # 中序遍历二叉树：先处理左子树，之后是根，最后是右子树
    def midorder_trav(self, subtree):
        if subtree is not None:
            self.midorder_trav(subtree.left)
            print(subtree.data)
            self.midorder_trav(subtree.right)

    # 后序遍历二叉树：先处理左子树，之后是右子树，最后是根
    def postorder_trav(self, subtree):
        if subtree is not None:
            self.midorder_trav(subtree.left)
            self.midorder_trav(subtree.right)
            print(subtree.data)


    # 反转二叉树
    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


btree = BinTree.build_from(node_list)
print("=========前序遍历===========")
btree.preorder_trav(btree.root)
print("=========中序遍历===========")
btree.midorder_trav(btree.root)
print("=========后序遍历===========")
btree.postorder_trav(btree.root)






