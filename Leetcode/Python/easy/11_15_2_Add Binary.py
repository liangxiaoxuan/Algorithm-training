# Given two binary strings a and b, return their sum as a binary string.

# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


def Binary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: s
    """
    result = []
    if a == "0" and b == "0":
        return "0"
    total = int(a)+int(b)
    while total > 0:
        if total % 2 == 0:
            result.append("0")
            t2 = total // 2
            total = t2
        else:
            result.append("1")
            total = total // 2
        if total == 1:
            result.append("1")
            break

    result = result[::-1]
    str= ""
    result = str.join(result)
    return result


def addBinary(a, b):
    print(a[-1::])
    

if __name__ == '__main__':
    a ="1234"
    b ="1"
    #print(Binary(a, b))
    print(addBinary(a, b))

