# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# def addTwoNumbers(l1:ListNode, l2:ListNode):
#     """
#     :type l1: ListNode
#     :type l2: ListNode
#     :rtype: ListNode
#     """
#
#     resultlist = curr = ListNode(0)
#     carry = 0
#
#     while l1 or l2 or carry:
#         if l1:
#             carry += l1.val
#             l1 = l1.next
#         if l2:
#             carry += l2.val
#             l2 = l2.next
#         curr.next = ListNode(carry%10)
#         curr = curr.next
#         carry = carry //10
#
#     return resultlist.next


def reverse_str(s):
    left, right = 0, len(s) - 1

    #s = list(s)

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)
    return print(s)


if __name__ == '__main__':
    l1 = [9, 9]
    l2 = [9]
    s = [1,2,3]
    #print(addTwoNumbers(l1, l2))
    print(reverse_str(s))
