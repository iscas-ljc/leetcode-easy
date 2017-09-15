class Solution(object):
    def containsDuplicate(self, nums):
        lenn=len(nums)
        if lenn==0:
            return False
        nums.sort()
        if lenn==1:
        	return False
        for i in range(lenn-1):
        	if nums[i]==nums[i+1]:
        		return True
        return False

        
        """
        :type nums: List[int]
        :rtype: bool
        """
        