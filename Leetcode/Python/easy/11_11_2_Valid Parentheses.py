# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid.
#
# An input string is valid if:
# 1.Open brackets must be closed by the same type of brackets.
# 2.Open brackets must be closed in the correct order.

# Example 2:
#
# Input: s = "()[]{}"
# Output: true


def isValid(s):
    """

    :param s: str
    :return: bool
    """

    # stack: First in Last out
    st = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            st.insert(0, s[i])

        else:
            if st:  # 非空list
                tmp = st.pop(0)  # 把index=0的value推出stack

            else:
                return False

            if tmp == "(" and s[i] != ")":
                return False
            if tmp == "[" and s[i] != "]":
                return False
            if tmp == "{" and s[i] != "}":
                return False

    if st:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "([{}]]"
    #s = "(())"
    print(isValid(s))