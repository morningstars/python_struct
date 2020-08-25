"""

栈的链式存储

以左侧作为栈顶   如果以右侧作为栈顶 则在删除时，无法找到前一个结点

"""

from day01.node import Node
from day02.sstack import StackError


class LStack(object):
    def __init__(self):
        self.head = Node(None)

    def top(self):
        if self.head.next == None:
            raise StackError("stack is empty")

        return self.head.next.val

    def is_empty(self):
        return self.head.next == None

    def push(self, ele):
        self.head.next = Node(ele, self.head.next)

    def pop(self):
        if self.head.next == None:
            raise StackError("stack is empty")

        node = self.head.next
        self.head.next = node.next
        return node.val


if __name__ == "__main__":
    st = LStack()
    print(st.is_empty())
    st.push(12)
    st.push(24)
    st.push(36)
    print(st.top())
    while not st.is_empty():
        print(st.pop())
