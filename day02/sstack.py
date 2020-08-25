"""

栈的顺序存储

"""


class StackError(Exception):
    pass


# 基于列表实现顺序栈
class SStack(object):
    def __init__(self):
        # 约定列表的最后一个元素为栈顶元素
        self._elements = []

    # 查看栈顶元素
    def top(self):
        if self._elements == []:
            raise StackError("stack is empty")

        return self._elements[-1]

    # 判断栈是否为空
    def is_empty(self):
        return len(self._elements) == 0

    # 入栈
    def push(self, ele):
        self._elements.append(ele)

    # 出栈
    def pop(self):
        if self._elements == []:
            raise StackError("stack is empty")
        return self._elements.pop()


if __name__ == "__main__":
    st = SStack()
    # st.top()
    print(st.is_empty())

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    print(st.pop())
