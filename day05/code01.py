"""

二叉树

"""


class TreeNode(object):
    def __init__(self, ele, left=None, right=None):
        self.ele = ele
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def add(self, ele):
        pass

    def preorder(self, node):
        if node is None:
            return
        print(node.ele)
        self.preorder(node.left)
        self.preorder(node.right)

    def levelorder(self, node):
        # 使用队列
        pass


if __name__ == "__main__":
    bt = BinaryTree()
    print(bt.is_empty())

    #   按照后序遍历增加结点
    b = TreeNode('B')
    f = TreeNode('F')
    g = TreeNode('G')
    d = TreeNode('D', f, g)
    i = TreeNode('I')
    h = TreeNode('H')
    e = TreeNode('E', i, h)
    c = TreeNode('C', d, e)
    a = TreeNode('A', b, c)  # 根节点

    bt = BinaryTree(a)  # 初始化树对象，传入根结点

    bt.preorder(bt.root)
