# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left and root.right is None:
            return 1
        return self.dfs(root)

    # recursion
    def dfs(self, node, depth=0):
        if not node:
            return depth
        return max(depth, self.dfs(node.left, depth+1), self.dfs(node.right, depth+1))


if __name__ == '__main__':
    # root = [1, "null", 2]
    root = TreeNode(1)
    root.right = TreeNode(2)
    # root.left = TreeNode(0)
    s = Solution()
    print (s.maxDepth(root))

