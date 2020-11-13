# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    i = 0
    i2 = i+1
    result = []
    for n in range(len(min(strs))):
        print(n)
        while (strs[i][n] == strs[i2][n]):
            if i2 == len(strs)-1 :
                break
            else:

                i += 1
                i2 += 1


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    longestCommonPrefix(strs)