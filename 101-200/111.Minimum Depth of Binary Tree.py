# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
    	if root is None:
    		return 0
    	leftdep=self.minDepth(root.left)
    	rightdep=self.minDepth(root.right)
    	if leftdep==0 :
    		return rightdep+1
    	if rightdep==0 :
    		return leftdep+1
    	if leftdep<rightdep:
    		return leftdep+1
    	if leftdep>=rightdep:
    		return rightdep+1

#map(self.minDepth,(root.left,root.right))
#对左右都执行同一个函数self.minDepth