"""
    队列
"""

from day01.node import Node


class Linklist(object):
    def __init__(self):
        self.head = Node(None)

    def init_list(self, list):

        p = self.head

        for item in list:
            p.next = Node(item)
            p = p.next

    def show(self):
        p = self.head.next

        while p:
            print(p.val, end=" ")
            p = p.next
        print()

    # 　尾部插入新的结点
    def append(self, value):
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)

    #  获取链表长度
    def get_length(self):
        lenth = 1
        p = self.head.next
        while p.next is not None:
            p = p.next
            lenth += 1
        return lenth

    # 　判断链表是否为空
    def is_empty(self):
        return self.head.next is None

    #   清空链表
    def clear(self):
        self.head.next = None

    # 　通过索引值获取value
    def get_item(self, index):
        if index < 0 or index >= self.get_length():
            raise IndexError("越界")

        p = self.head.next
        for i in range(index):
            p = p.next
        return p.val

    # 在某个位置插入结点
    def insert(self, index, item):
        if index < 0 or index > self.get_length():
            raise IndexError("越界")

        p = self.head
        for i in range(index):
            p = p.next
        p.next = Node(item, p.next)

    # 删除某个元素
    def delete(self, item):
        p = self.head
        while p.next is not None:
            if p.next.val == item:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError(str(item) + " is not in list")


if __name__ == "__main__":
    list = Linklist()
    l = [1, 2, 3, 4, 5]

    list.init_list(l)
    list.show()
    print(list.get_length())

    list.append(55)
    list.show()
    print(list.get_length())
    print("-----")
    print(list.get_item(5))
    print("-----")
    list.insert(6, 12)
    list.show()

    list.delete(551)
    list.show()
