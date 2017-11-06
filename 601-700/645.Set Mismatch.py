class Solution(object):
    def findErrorNums(self, nums):
    	lenn=len(nums)
    	a=[0]*(lenn+1)
    	for i in range(lenn):
    		a[nums[i]]+=1
    	for i in range (1,lenn+1):
    		if a[i]==2:
    			result1=i
    		if a[i]==0:
    			result2=i
    	return result1,result2
    	#建立一个序号索引的数组
    	#遍历一遍，出现两次的和零次的返回
