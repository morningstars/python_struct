"""
检测一段文字中 括号是否成对出现
"""
from day02.sstack import SStack


def check_pair():
    str = "[{}]("
    st = SStack()
    for c in str:
        if c == "(" or c == "{" or c == "[":
            st.push(c)
        elif c == ")" or c == "}" or c == "]":
            if st.is_empty():
                return False
            else:
                top = st.top()
                if (top == "(" and c == ")") \
                        or (top == "{" and c == "}") \
                        or (top == "[" and c == "]"):
                    st.pop()
                else:
                    return False
    return st.is_empty()


if __name__ == "__main__":
    print(check_pair())
