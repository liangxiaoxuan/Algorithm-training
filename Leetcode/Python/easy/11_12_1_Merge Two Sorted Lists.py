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

#linkde node
def mergeTwoLists2(l1, l2):
    if not l1 and not l2:
        return None

    if l1 and not l2:
        return l1

    if not l1 and l2:
        return l2

    output = ListNode()
    tail = output
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return output.next


if __name__ == '__main__':
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    mergeTwoLists(l1, l2)