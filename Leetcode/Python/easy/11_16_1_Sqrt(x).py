# coding=utf-8
# Given a non-negative integer x, compute and return the square root of x.
#
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.

# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    # binary search
    # 1*1 =1 / 2*2 = 4 / 3*3 = 9
    if x <2:
        return x
    left = 2
    right = x // 2   # Floor division (除后的整数)

    while left <= right:
        pivot = (left+right) // 2  # 取中间数
        nums = pivot * pivot
        if nums > x:                    # 当对比左右边的平方和后 较大的一方则中间数向左退一步 反之向右进一步 until left > right
            right = pivot -1
        elif nums < x:
            left = pivot +1
        else:
            return pivot
    return right


if __name__ == '__main__':
    x = 10
    print(mySqrt(x))