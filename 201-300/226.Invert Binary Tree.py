# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if root is not None:
            self.invertTree(root.left)
            self.invertTree(root.right)
            p=root.left
            root.left=root.right
            root.right=p
        return root
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        