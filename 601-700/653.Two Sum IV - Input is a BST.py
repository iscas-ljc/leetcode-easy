class Solution(object):
    def findTarget(self, root, k):
        self.root = root
        self.k = k
        return self.findNumber(root)
    def findNumber(self, root):
        if not root: return False
        node = self.root
        n = self.k - root.val
        if n != root.val:
            while node:
                if node.val == n: return True
                if n > node.val: node = node.right
                else: node = node.left
        return self.findNumber(root.left) or self.findNumber(root.right)
'''
class Solution(object):
    def findTarget(self, root, k):
    	if root is None:
    		return False
    	test=root
    	target1=k-root.val
    	if target1!=root.val:
    		#查找差值
    		while test:
    			if test.val==target1:
    				return True
    			if test.val<target1:
    				test=test.right
    			elif test.val>target1:
    				test=test.left
    			#不能写另一个if
    	return findTarget(root.left) or findTarget(root.right)
    	'''
#区别在于答案每个差值都从根开始找
#而我的答案每个差值都是从当前根找，如果答案在左右两边，则找不到