# valid parentheses
# given a string (with only "(" or ")"), if it's valid return true, else return false
# example: "()"->True; ")("->False


def valid_parentheses(s: str):

    count = 0
    for i in s:
        if "(" == i:
            count += 1
        else:
            count -= 1
        if count < 0 or count > 1:
            return False

    if count == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "((()()"
    print(valid_parentheses(s))