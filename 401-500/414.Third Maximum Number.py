class Solution(object):
    def thirdMax(self, nums):
    	nums=list(set(nums))
##利用list(set())进行排序 ，单独set会报错
    	lenn=len(nums)
    	if lenn==1:
    		return nums[0]
    	if lenn==2:
    		if nums[0]>nums[1]:
    			return nums[0]
    		else:
    			return nums[1]
    	result=[0]*3
    	result[0]=nums[0]
    	if nums[1]>nums[0]:
    		result[1]=nums[1]
    	else:
    		result[1]=result[0]
    		result[0]=nums[1]
    	if nums[2]>result[1]:
    		result[2]=nums[2]
    	elif result[0]<nums[2]<result[1]:
    		result[2]=result[1]
    		result[1]=nums[2]
    	elif result[0]>nums[2]:
    		result[2]=result[1]
    		result[1]=result[0]
    		result[0]=nums[2]
    	for i in range(lenn):
    		if result[0]<nums[i]<result[1]:
    			result[0]=nums[i]
    		if result[1]<nums[i]<result[2]:
    			result[0]=result[1]
    			result[1]=nums[i]
    		if result[2]<nums[i]:
    			result[0]=result[1]
    			result[1]=result[2]
    			result[2]=nums[i]
    	return result[0]