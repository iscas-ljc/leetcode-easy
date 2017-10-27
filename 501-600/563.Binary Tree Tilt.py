# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        self.result=0
        def sumtree(root):
            if root is None:
                return 0
            lsum=sumtree(root.left)
            rsum=sumtree(root.right)
            self.result+=abs(lsum-rsum)
            return lsum+rsum+root.val
        sumtree(root)
        return self.result
        