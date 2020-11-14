# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.

# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    if not l1: return l2
    if not l2: return l1

    result = l1 + l2
    result = sorted(result)

    print(l1)
    print(result)
    return result

# 不能用加法


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    mergeTwoLists(l1, l2)