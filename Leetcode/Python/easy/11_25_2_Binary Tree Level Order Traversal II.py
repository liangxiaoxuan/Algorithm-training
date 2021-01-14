# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print (self.val)


class Solution(object):
    def levelOrderBottom(self, root):

        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels




if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root2 = root.left
    root3 = root.right
    root3.left = TreeNode(15)
    root3.right = TreeNode(7)
    root3.left.PrintTree()
    root3.right.PrintTree()

