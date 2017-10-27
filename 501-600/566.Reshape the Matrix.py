class Solution(object):
    def matrixReshape(self, nums, r, c):
    	result=[]
    	r1=len(nums)
    	r2=len(nums[0])
    	p=q=0
    	if r1*r2!=r*c:
    		return nums
    	#长宽乘积不一样则输出原来的
    	for i in range(r):
    		rnew=[]
    		for j in range(c):
    			rnew.append(nums[p][q])
    			q+=1
    			if q==r2:
    				p+=1
    				q=0
    			#一个小数组加完转到下一个小数组
    		result.append(rnew)
    	return result


        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        