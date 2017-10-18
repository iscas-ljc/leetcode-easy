class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
    	result=0
    	test=0
    	lenn=len(nums)
    	for i in range(lenn):
    		if nums[i]==1:
    			test+=1
    			result=max(result,test)
    		if nums[i]==0:
    			test=0
    	return result
