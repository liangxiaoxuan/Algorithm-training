# coding=utf-8
# 2 string , find the longest common substring
# Dynamic programming

def commonsubstring(s1, l1, s2, l2):

    # create a zero value matrix
    dp = [[0 for x in range(l2+1)] for i in range(l1+1)]
    print dp
    result = 0

    for i in range(l1+1):   # 从i每一个跟同一个j对比
        for j in range(l2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1   # 对角数+1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result


if __name__ == '__main__':
    string1 = "Helloa"
    string2 = "abcHello"
    len1 = len(string1)
    len2 = len(string2)
    print(commonsubstring(string1, len1, string2, len2))
