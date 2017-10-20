class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = collections.Counter()
        def traverse(root):
            if not root: return
            counter[root.val] += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        maxn = max(counter.values() + [None])
        return [e for e, v in counter.iteritems() if v == maxn]
#Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，
#以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。Counter类和其他语言的bags或multisets很相似。
'''
超时
class Solution(object):
    def findMode(self, root):
    	count=[0]*1000
    	result=[]
    	def countnum(self,root):
    		if root is None:
    			return
    		count[root.val]+=1
    		countnum(root.left)
    		countnum(root.right)
    	countnum(root)
    	maxn=0
    	for i in range(len(count)):
    		if count[i]>maxn:
    			maxn=count[i]
    	for i in range(len(count)):
    		if count[i]==maxn:
    			result.append(count[i])
    	return result
'''