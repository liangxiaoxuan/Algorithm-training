# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


def longestsub2(s):  # 若没有重复字母就一直append，若重复了之前的一个，就从那个字母的之后开始重新循环，比较哪个组合最大）
    ans = 0
    temp = []

    for i in range(len(s)):
        if s[i] not in temp:
            temp.append(s[i])
            print(temp)
        else:
            ans = max(ans, len(temp))
            idx = temp.index(s[i])
            temp = temp[idx + 1:]
            temp.append(s[i])
            print(temp)

    ans = max(ans, len(temp))
    return ans


if __name__ == '__main__':
    s = "abcb"
    print(longestsub2(s))





