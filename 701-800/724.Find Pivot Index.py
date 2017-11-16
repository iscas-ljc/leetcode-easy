class Solution(object):
    def pivotIndex(self, nums):
    	total=sum(nums)
    	a=total
    	for i in range(len(nums)):
    		a-=nums[i]
    		if a==(total-nums[i])/2.0:
    		#如果不是2.0，[-1,-1,-1,-1,-1,-1]就会报错
    			return i
    	return -1
