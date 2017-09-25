class Solution(object):
    def guessNumber(self, n):
        i=1 
        j=n
        while i<j:
            m=(i+(j-1))/2
            g=guess(m)
            if g==0:
                return m
            if g==-1:
                j=m-1
            if g==1:
                 i=m+1
        return i
        """
        :type n: int
        :rtype: int
        """