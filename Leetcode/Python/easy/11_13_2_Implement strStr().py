# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
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
    if haystack == "" and needle == "":
        return 0
    else:

        result = haystack.find(needle)
        print(result)
        return result

# Runtime: 8 ms, faster than 99.61% o
# Memory Usage: 13.7 MB, less than 70.80%


if __name__ == '__main__':
    # haystack = "hello"
    # needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    strStr(haystack, needle)