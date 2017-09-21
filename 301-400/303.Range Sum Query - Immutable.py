class NumArray(object):

    def __init__(self, nums):
        self.a=nums
        for i in range(1,len(nums)):
            self.a[i]+=self.a[i-1]
        

    def sumRange(self, i, j):
        if i==0:
            return self.a[j]
        else:
            return self.a[j]-self.a[i-1]