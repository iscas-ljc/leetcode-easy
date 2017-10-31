class Solution(object):
    def findLHS(self, nums):
    	judge=collections.Counter(nums)
    	#collections.Counter统计了各元素的个数
    	#a有3个，则judge[a]=3
    	result=0
    	for i in judge:
    		if i+1 in judge:
    			result=max(result,judge[i]+judge[i+1])
    	return result