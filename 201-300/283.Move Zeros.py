class Solution(object):
    def moveZeroes(self, nums):
    	lenn=len(nums)
    	count=0
    	result=[]
    	for i in range(lenn):
    		if nums[i]==0:
    			count+=1
    		if nums[i]!=0:
    			result.append(nums[i])
    	for i in range(count):
    		result.append(0)
    	for i in range(lenn):
    		nums[i]=result[i]
    	        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        