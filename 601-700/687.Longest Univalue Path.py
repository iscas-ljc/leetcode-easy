class Solution(object):
    def longestUnivaluePath(self, root):
    	if root is None:
    		return 0
    	return max(self.find(root.left,root.val)+self.find(root.right,root.val),self.longestUnivaluePath(root.left),self.longestUnivaluePath(root.right))
    def find(self,root,val):
    	if root is None:
    		return 0
    	if root.val!=val:
    		return 0
    	return 1+max(self.find(root.left,val),self.find(root.right,val))
    	#如果左右子树和根一样，判断最长是多长，左+右+根