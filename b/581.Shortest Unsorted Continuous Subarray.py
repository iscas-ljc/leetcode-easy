class Solution(object):
    def findUnsortedSubarray(self, nums):
        sort=sorted(nums)
        lenn=len(nums)
        first=0
        last=lenn-1
        while sort[last]==nums[last]:
            if last==first:
                return 0
            #防止原本函数有序
            last-=1
        while sort[first]==nums[first]:
            first+=1
        return last-first+1