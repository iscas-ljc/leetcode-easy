class Solution(object):
    def checkPossibility(self, nums):
    	lenn=len(nums)
    	if lenn==1 or lenn==0:
    		return True
    	if nums[0]>nums[1]:
    		nums[0]=nums[1]
    		a=sorted(nums)
    		return nums==a
    	chance=1
    	for i in range(1,lenn):
    		if nums[i]<nums[i-1]:
    			chance-=1
    			if i>1 and nums[i]<nums[x-2]:
    				nums[i]=nums[i-1]
    			#a1,a2,a3,a4,a5 如果a4<a3则必须改变其中一个才能有序
    			#如果a4<a2则必须改变a4（通过让a4=a3)
    			#如果a4>a2那么改变a3即可，则不需要进行操作
    	return chance>=0