# Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
#
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
#
# Input: s = "Hello World"
# Output: 5


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    s = s.strip()
    s1 = s.split((" "))

    if len(s1) == 0:

        return 0

    else:
        s2 = s1[len(s1)-1]
        result = len(s2)

        return result


if __name__ == '__main__':
    s = "Hello World"
    print(lengthOfLastWord(s))