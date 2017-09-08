class Solution(object):
    def rotate(self, nums, k):
        lenn=len(nums)
        if k>lenn:
            k=k-lenn
        b=[0]*(lenn)
        for i in range(lenn):
        	if(i+k<=lenn-1):
        		target=i+k
        	else:
        		target=i+k-lenn
        	b[target]=nums[i]
        for i in range(lenn):
            nums[i]=b[i]

        
        