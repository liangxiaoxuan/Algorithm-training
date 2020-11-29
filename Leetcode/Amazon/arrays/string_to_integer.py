# mplement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.

# Example 1:
#
# Input: str = "42"
# Output: 42


def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    s1 = s.split()  # split s
    if len(s1) == 0: return 0  # exclude just blank
    s1_0 = s1[0]  # first block
    result = 0
    pm = ['+', '-']  # plus minus
    if not (s1_0[0].isdigit() or (len(s1_0) > 1 and (s1_0[0] in pm) and s1_0[1].isdigit())):  # number~ or (pm)+number~
        return 0
    if s1_0[(s1_0[0] in pm):].isdigit():
        result = s1_0
    # k = 0
    # for i in s1_0[(s1_0[0] in pm):]:
    #     if not i.isdigit():
    #         result = s1_0[:k + (s1_0[0] in pm)]
    #         break
    #     else:
    #         k += 1
    if int(result) > (2 ** 31) - 1:
        return (2 ** 31) - 1
    elif int(result) < (-2 ** 31):
        return (-2 ** 31)
    else:
        return int(result)


if __name__ == '__main__':
    s = "4193 with word"
    s1 = "12a"
    #print(s1.isdigit())
    print(myAtoi(s))