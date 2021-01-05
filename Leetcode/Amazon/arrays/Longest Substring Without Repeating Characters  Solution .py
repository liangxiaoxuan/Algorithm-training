# coding=utf-8
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
            # print(temp)
        else:
            ans = max(ans, len(temp))
            idx = temp.index(s[i])
            temp = temp[idx+1:]   # 从重复的后一位有接着开始 不断分片
            temp.append(s[i])     # 把去掉的之前的s[i] 再补回来接着
            # print(temp)

    ans = max(ans, len(temp))   # 对比最后的分片的temp和之前的最大值 # 对比的收拾length
    return ans


if __name__ == '__main__':
    s = "abcabcbb"
    #print()
    #longestsub2(s)
    print(longestsub2(s))





