class Solution(object):
    def majorityElement(self, nums):
    	lenn=len(nums)
    	result=0
    	count=0
    	for i in range(lenn):
    		if(count==0):
    			result=nums[i]
    			count+=1
    		else:
    			if(result==nums[i]):
    				count+=1
    			else:
    				count-=1
    	return result
