class Solution(object):
    def findLengthOfLCIS(self, nums):
    	lenn=len(nums)
    	if lenn==0:
    		return 0
    	result=[1]*lenn
    	#全部置1，后比前大就+1，不大就不管
    	for i in range(1,lenn):
    		if nums[i]>nums[i-1]:
    			result[i]=result[i-1]+1
    	return max(result)