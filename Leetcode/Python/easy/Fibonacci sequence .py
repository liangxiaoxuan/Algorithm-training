# coding=utf-8
# 1,1,2,3,5,8,13,21
# output =第N 个值
# Recurison 递归：1；递推：复杂的问题化为简单的问题 2，回归： 化简问题后，逐步返回，依次得到复杂的解

# Recurison
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    if n > 2:
        return fib(n - 1) + fib(n - 2)


# Memorized solution
def fib2(n):
    if n in memo:
        return memo[n]   # if the value exist , return the value
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib2(n-1) + fib2(n-2)
    memo[n] = result
    return result


if __name__ == '__main__':
    n = 4
    memo = {}
    #print(fib(n))
    print (fib2(n))
   #print (fib(n))