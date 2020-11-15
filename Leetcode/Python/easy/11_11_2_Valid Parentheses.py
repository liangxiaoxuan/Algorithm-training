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

    # stack
    count = 0
    for i in s:

        if "(" or "[" or "{" == i:
            count += 1
        else:
            count -= 1
        #if count < 0 or count

    if count == 0:
        return True


if __name__ == '__main__':
    s = "([}}"
    #s = "()}"

    print(isValid(s))