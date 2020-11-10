# Given a 32-bit signed integer, reverse digits of an integer.
# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# Example 1:
#
# Input: x = 123
# Output: 321


def reverse(x):


    if x < 0:
        x = abs(x)
        a = str(x)
        r = -int(a[::-1])
    else:
        a = str(x)
        r = int(a[::-1])

    if r % 10 == 0:
        r = r // 10

    if r < -(2**31) or r > 2**31:
        print(0)
        return 0
    else:
        print(r)
        return r

##Runtime: 24 ms, faster than 42.23%
##Memory Usage: 13.5 MB, less than 17.26%


if __name__ == '__main__':
    x = 1534236469
    reverse(x)
