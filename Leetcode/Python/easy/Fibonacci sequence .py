# 1,1,2,3,5,8,13,21
# output =第N 个值
# Recurison 递归：1；递推：复杂的问题化为简单的问题 2，回归： 化简问题后，逐步返回，依次得到复杂的解

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    if n > 2:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    n = 3
    fib(n)