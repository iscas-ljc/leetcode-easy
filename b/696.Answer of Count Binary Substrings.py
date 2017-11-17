class Solution(object):
    def countBinarySubstrings(self, s):
        n=len(s)
        res=0
        start=0
        lastcount=1
        for i in xrange(1,n):
            if s[i]!=s[i-1]:
                res+=1
                lastcount=i-start
                start=i
            else:
                if i-start<lastcount:
                    res+=1
        return res
        