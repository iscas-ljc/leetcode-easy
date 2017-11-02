class Solution(object):
    def mergeTrees(self, t1, t2):
    	if t1 is None:
    		return t2
    	if t2 is None:
    		return t1
    	t1.left=self.mergeTrees(t1.left,t2.left)
    	t1.right=self.mergeTrees(t1.right,t2.right)
    	t1.val+=t2.val
    	return t1
    	#循环调用使两棵树相加