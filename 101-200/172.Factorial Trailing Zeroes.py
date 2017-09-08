class Solution(object):
    def trailingZeroes(self, n):
        result=0
        while(n):
            n=n//5
            result+=n
        return result