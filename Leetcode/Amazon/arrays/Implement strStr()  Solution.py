# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
        return 0
    for i, num in enumerate(haystack):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = "Hello"
    needle = "ll"
    print(strStr(haystack, needle))
