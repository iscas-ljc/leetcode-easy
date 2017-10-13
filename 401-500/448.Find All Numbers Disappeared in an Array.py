class Solution(object):
    def findDisappearedNumbers(self, nums):
    	result=[]
    	for i in range(len(nums)):
    		change=abs(nums[i])-1  #将存在的位置变成负数
    		nums[change]=-abs(nums[index])
    	for i in range(len(nums)):
    		if nums[i]>0:
    			result.append(i+1)
    	return result


'''class Solution(object):
    def findDisappearedNumbers(self, nums):
    	result=[]
    	lenn=len(nums)
    	for i in xrange(1,lenn+1):
    		if i not in nums:
    			result.append(i)
    	return result
		超时