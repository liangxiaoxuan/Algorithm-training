# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
#
#
# Example 1:
#
# Input: s = "III"
# Output: 3

v = {"I": 1,
     "V": 5,
     "X": 10,
     "L": 50,
     "C": 100,
     "D": 500,
     "M": 1000}


def romanToInt(s):

    r = 0
    l = len(s)
    i = 0
    while i < l:

        #print(i)
        r += v[s[i]]
        # print(r)
        if i-1 < 0:
            i2 = 0
        else:
            i2 = i-1
        if v[s[i2]] < v[s[i]]:
            # print(2*v[s[i2]])
            r -= 2*v[s[i2]]
            # print(s[i])

        i += 1
    print(r)
    return r

# Runtime: 48 ms, faster than 29.02%
# Memory Usage: 13.6 MB, less than 7.46%


if __name__ == '__main__':
    s = "LVIII"
    #s = "MCMXCIV"
    romanToInt(s)
