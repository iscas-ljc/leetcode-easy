class Solution(object):
    def convertBST(self, root):
    	self.total=0
    	def trans(root):
    		if root is None:
    			return 
    		trans(root.right)
    		root.val+=self.total
    		self.total=root.val
    		trans(root.left)
    	trans(root)
    	return root

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        