class Solution(object):
    def twoSum(self, nums, target):
        mydict=dict()
        for idx,num in enumerate(nums):
            if target-num in mydict:
                return [mydict[target-num],idx]
            mydict[num]=idx