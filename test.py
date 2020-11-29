# Find all string which is a combination of [‘1’,’a’,’z’,’b’,’b’,’2’,’9’] (cannot be replaced back)
# and ‘number’ cannot be the first letter of the string, and word character cannot be the last letter.
#
# Input: [‘1’,’a’,’z’,’b’,’b’,’2’,’9’]
#
# Output: List of all valid string
#
# e.g: ‘ab9zb12’, ‘b9zba21’ are valid; ‘b9zb12a’ or ‘9zbba12’ or ‘9zba12b’ is invalid
from itertools import permutations


def combinationlist(s):
    """

    :param s: string
    :return: list of all valid string
    """
    # in case s == 0
    if len(s) == 0:
        return []

    # in case s has only 1 string
    if len(s) == 1:
        return [s]

    # list of all the combinations
    ss = list(permutations(s))
    res = []
    for i in ss:
        # number != fist string and word character != last string
        if i[0].isdigit() == True or i[len(i)-1].isalpha() == True:
            continue
        else:
            ii = "".join(i)
            res.append(ii)

    return res


if __name__ == '__main__':
    s = ["1", "a", "2", "b", "b", "2", "9"]
    print(len(combinationlist(s)))
