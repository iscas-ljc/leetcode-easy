class Solution(object):
    def rob(self, nums):
        lenn=len(nums)
        if lenn==0:
        	return 0
        if lenn==1:
        	return nums[0]
        if lenn==2:
        	if(nums[1]>nums[0]):
        		return nums[1]
        	else:
        		return nums[0]
        result=[0]*(lenn)
        for i in range (lenn):
        	if i==0:
        		result[i]=nums[i]
        	if i==1:
        		if(nums[1]>nums[0]):
        			result[i]=nums[1]
        		else:
        			result[i]=nums[0]
        	if nums[i]+result[i-2]>result[i-1]:
        		result[i]=nums[i]+result[i-2]
        	else:
        		result[i]=result[i-1]
        return result[lenn-1]
        