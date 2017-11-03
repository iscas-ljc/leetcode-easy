class Solution(object):
    def findMaxAverage(self, nums, k):
    	#滑动窗口
    	sumk=0
    	result=-99999
    	#应用result=None代替
    	for i in range(len(nums)):
    		sumk+=nums[i]
    		if i>=k:
    			sumk-=nums[i-k]
    		if i>=k-1:
    			result=max(result,sumk*1.0/k)
    	return result