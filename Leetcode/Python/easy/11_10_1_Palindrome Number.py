# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same
# backward as forward.
#
# Follow up: Could you solve it without converting the integer to a string?
#
# Example 1:
#
# Input: x = 121
# Output: true


def isPalindrome(x):

    num = str(x)
    if x < -(2**31) or x > (2**31-1):
        print("False")
        return False
    else:

        if x > 0 and num == num[::-1]:
            print("True")
            return True
        elif x == 0:
            print("True")
            return True
        else:
            print("False")
            return False


# Runtime: 44 ms, faster than 87.88%
# Memory Usage: 13.5 MB, less than 17.65%


if __name__ == '__main__':
    x = 1234
    isPalindrome(x)
