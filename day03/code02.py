"""

队列的链式存储

front 指向第一个节点的前一个
rear 指向最后一个节点

"""

from day01.node import Node


class QueueError(Exception):
    pass


class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        return self.front is self.rear

    def enqueue(self, ele):
        self.rear.next = Node(ele)
        self.rear = self.rear.next

    def dequeue(self):
        if self.is_empty():
            raise QueueError("队列为空")

        self.front = self.front.next
        return self.front.val

    # 取对头元素
    def first(self):
        if self.is_empty():
            raise QueueError("queue is empty")
        return self.front.next.val

    # 清空队列
    def clear(self):
        self.front = self.rear


if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(12)
    lq.enqueue(22)
    lq.enqueue(32)

    print(lq.first())

    while not lq.is_empty():
        print(lq.dequeue())
