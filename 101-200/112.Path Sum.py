class Solution(object):
    def hasPathSum(self, root, sum):
    	if sum==0 and root is None:
    		return False
    	if root is None and sum!=0:
    		return False
    	if not root.left and not root.right and root.val==sum:
    		return True
    	sum=sum-root.val
    	return (self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum))