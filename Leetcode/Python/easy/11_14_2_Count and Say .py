# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
# Then for each group, say the number of characters, then say the character.
# To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

# Example 2:
#
# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    # c.s(1) = "1" —— 1
    # c.s(2) = "11" —— say(c.s(1)) (result)
    # c.s(3) = "21" —— say(c.s(2)) (result)

    # say()
    def say(v):
        #v = str(v)
        i = 0
        n1 = list(v)
        while i < len(n1) - 1:
            if n1[i] == n1[i + 1]:
                del n1[i]
            else:
                i += 1
        n2 = "".join(n1)

        result = []
        for ii in n2:

            s = n2.count("1")  ## 这里一直有问题

            result.append(str(s))
            result.append(str(ii))
        result = "".join(result)
        #print(result)
        return result

    if n == 1:
        return "1"
    if n >= 2:
        return say(countAndSay(n-1))


if __name__ == '__main__':
    n = 3

    print(countAndSay(n))