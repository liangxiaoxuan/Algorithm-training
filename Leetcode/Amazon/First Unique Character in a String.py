# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    res = []
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    #print(dic)
    for index, char in enumerate(s):
        if dic[char] == 1:
            return index
    return -1


if __name__ == '__main__':
    s = "leetlcode"
    print(firstUniqChar(s))