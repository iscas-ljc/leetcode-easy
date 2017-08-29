# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        def check(root):
        if root is None:
        	return 0;
        left=check(root.left)
        right=check(root.right)
        if left==-1 or right==-1 or abs(left-right)>1:
        	return -1
        return 1+max(right,left)
    return check(root)!=-1
#python 严格要求列对齐