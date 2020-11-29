# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def longsubstring(s):

    if s == "":
        return 0
    if len(s) == 1:
        return 1

    ans = 0
    res = []
    for i in range(len(s)):
        if s[i] not in res:
            res.append(s[i])
        else:
            ans = max(ans, len(res))
            idx = res.index(s[i])
            res = res[idx+1:]
            res.append(s[i])
    ans = max(ans, len(res))
    return ans


if __name__ == '__main__':
    s = "abcabbabcde"
    print(longsubstring(s))
