# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
    	if s is None or t is None:
    		return not s and not t 
    	if self.check(s,t):
    		return True
    	return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    	#检测是不是从根的子树，不是的化监测是不是左右子树的子树
    	#左右有一个成立就是子树
    def check(self,s,t):
    	if s is None or t is None:
    		return not s and not t
    	if s.val!=t.val:
    		return False
    	return self.check(s.left,t.left) and self.check(s.right,t.right)
    	#左右都一样才能认为相等
        