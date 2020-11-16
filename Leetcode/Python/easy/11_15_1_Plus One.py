# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    l = len(digits)-1
    while l >= 0:
        if digits[l] == 9:
            digits[l] = 0
        else:
            digits[l] += 1
            return digits
        l -= 1
        if digits[l] == 0:
            digits2 = [1] + digits
            return digits2

    print(digits)

# runtime: 16 ms, faster than 89.48%
# Memory Usage: 13.6 MB, less than 11.94%


if __name__ == '__main__':
    digits = [9, 9, 9]
    print(plusOne(digits))

