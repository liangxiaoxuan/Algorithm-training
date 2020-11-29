# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary
# until the first non-whitespace character is found.
# Then, starting from this character takes an optional initial plus or minus sign followed
# by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.

# Example 2:
#
# Input: str = "   -42"
# Output: -42


def myAtoi(s):

    # trim whitespace
    s = s.strip()
    if s[0].isalpha() == 1:  # 1 == true 0== false
        return 0

    else:
        for i in range(len(s)):
            if s[i].isalpha() == 1:
                return s[:i-1]
            else:
                continue
        return s


if __name__ == '__main__':
    s = "   -42"
    print(myAtoi(s))




