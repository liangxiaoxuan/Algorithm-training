# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def listprint(self):
        printval = self.val
        while printval is not None:
            print (printval.val)
            printval = printval.next


class Slinkedlist:
    def __init__(self):
        self.headval = None


class Solution(object):

    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    head = [1, 1, 2, 3]
    list1 = ListNode(1)
    ll = ListNode(1)
    lll = ListNode(2)
    llll = ListNode(3)
    list1.next = ll
    ll.next = lll
    lll.next = llll
    s = Solution()
    result = s.deleteDuplicates(list1)

    while result.next is not None:
        print result.val
        result = result.next
    print result.val






