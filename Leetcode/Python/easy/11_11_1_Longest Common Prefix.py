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

    result = []
    for n in range(len(min(strs))):
        i = 0
        i2 = i + 1

        while (strs[i][n] == strs[i2][n]):
            if i2 == len(strs)-1 and strs[i][n] == strs[i2][n]:
                result.append(strs[i][n])
                break
            else:
                i += 1
                i2 += 1
        else:
            result.append("")
            break
    str = ""
    result2 = str.join(result)
    print(result2)
    return result2

# Runtime Error
# min() arg is an empty sequence


if __name__ == '__main__':
    #strs = ["flower", "flow", "flgg", "flag"]
    #strs = ["dog","racecar","car"]
    strs = []
    longestCommonPrefix(strs)