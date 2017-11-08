class Solution(object):
    def findSecondMinimumValue(self, root):
    	self.leaves=[]
    	self.find(root)
        result=list(set(self.leaves))
        #去重判断是否只有一个，有一个返回-1
        if len(result)<2:
            return -1
        result.sort()
        #有多个排序返回第二个
        return result[1]
    def find(self, root):
    	#通过find函数找所有叶子节点，因为leaves要一直更新，一定要新写一个函数
    	if root is None:
    		return
    	if root.left is None and root.right is None:
    		self.leaves.append(root.val)
    		return
    	self.find(root.left)
    	self.find(root.right)
    	return