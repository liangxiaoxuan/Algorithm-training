# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def PrintTree(self):
        print (self.val)


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:

            return True

        if p is None:

            return False
        if q is None:

            return False
        if p.val != q.val:

            return False

        # recurison if left == right
        leftissame = self.isSameTree(p.left, q.left)
        rightissame = self.isSameTree(p.right, q.right)

        return leftissame and rightissame


if __name__ == '__main__':

    # set up the trees
    rootp = TreeNode(1)
    p1 = TreeNode(2)
    p2 = TreeNode(2)
    rootp.left = p1
    rootp.right = p2
    # p1.PrintTree()
    # p2.PrintTree()

    rootq = TreeNode(1)
    q1 = TreeNode(1)
    q2 = TreeNode(2)
    rootq.left = q1
    rootq.right = q2
    #
    s = Solution()
    print(s.isSameTree(rootp, rootq))
