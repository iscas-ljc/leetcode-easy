class Solution(object):
    def getdeep(self,root):
    	if root is None:
    		return 0
    	left=self.getdeep(root.left)
    	right=self.getdeep(root.right)
    	self.deep=max(self.deep,left+right)
    	#求解左右深度和
    	return max(left,right)+1
    def diameterOfBinaryTree(self, root):
    	self.deep=0
    	self.getdeep(root)
    	return self.deep