# ou are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#  Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """

# fibonacci sequence
    if n == 0 or n == 1 or n == 2:
        return n

    s1 = 1
    s2 = 2
    for i in range(2, n):
        s2 += s1
        s1 = s2 - s1
    return s2


if __name__ == '__main__':
    n = 7
    print(climbStairs(n))