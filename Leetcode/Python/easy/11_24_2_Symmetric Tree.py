# coding=utf-8
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
#
# Follow up: Solve it both recursively and iteratively.


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print (self.val)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.ismirror(root.left, root.right)  # 调用下面的函数

    def ismirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:  # level 2
            return False
        if left.val != right.val:
            return False

        return self.ismirror(left.left, right.right) and self.ismirror(left.right, right.left)


if __name__ == '__main__':
    root = [1, 2, 2, 3,4,4,3]
    # Set up the tree
    rootp = TreeNode(1)
    r1 = TreeNode(2)
    r2 = TreeNode(3)
    r3 = TreeNode(4)

    rootp.left = r1
    rootp.right = r1

    rootp.left.left = TreeNode(3)
    rootp.right.right = TreeNode(3)
    rootp.left.right = TreeNode(4)
    rootp.right.left = TreeNode(4)
    rootp.left.left.PrintTree()
    rootp.right.right.PrintTree()

    # 被覆盖

    s = Solution()
    print(s.isSymmetric(rootp))

