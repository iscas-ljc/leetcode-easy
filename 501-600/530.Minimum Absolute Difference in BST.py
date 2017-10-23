class Solution(object):
    def getMinimumDifference(self, root):
    	left=root.left
    	right=root.right
    	result=9999999
    	#让result很大，以便向小更新
    	if left is not None:
    		while left.right:
    			left=left.right
    		result=min(root.val-left.val,self.getMinimumDifference(root.left))
    	if right is not None:
    		while right.left:
    			right=right.left
    		result=min(right.val-root.val,result,self.getMinimumDifference(root.right))
    	return result