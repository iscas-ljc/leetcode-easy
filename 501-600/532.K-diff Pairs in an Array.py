class Solution(object):
    def findPairs(self, nums, k):
        c=collections.Counter(nums)
        if k>0:
            return sum(c[n+k]>1-1 for n in c.keys())
        if k==0:
            return sum(c[n]>1 for n in c.keys())
        if k<0:
            return 0
        