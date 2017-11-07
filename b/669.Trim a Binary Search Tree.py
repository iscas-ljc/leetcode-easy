class Solution(object):
    def trimBST(self, root, L, R):
    	if root is None:
    		return root
    	if root.val<L:
    		return trimBST(root.right,L,R)
    	if root.val>R:
    		return trimBST(root.left,L,R)
    	#根不满足条件之间减掉一半
    	root.left=trimBST(root.left)
    	root.right=trimBST(root.right)
    	#根满足条件去剪左右子树
    	return root