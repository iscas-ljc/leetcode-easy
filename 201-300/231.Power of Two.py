class Solution(object):
    def isPowerOfTwo(self, n):
        while n/2.0>=1:
            n=n/2.0
        return n==1

#/后写浮点数，才做浮点数除法