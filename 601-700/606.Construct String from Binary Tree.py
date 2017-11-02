class Solution(object):
    def tree2str(self, t):
    	if t is None:
    		return ''
    	result=str(t.val)
    	if t.left is not None or t.right is not None:
    		result+='('+self.tree2str(t.left)+')'
    	if t.right is not None:
    		result+='('+self.tree2str(t.right)+')'
    	return result
        #递归调用将二叉树转化为字符串