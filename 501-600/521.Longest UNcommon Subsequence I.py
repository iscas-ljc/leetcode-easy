class Solution(object):
    def findLUSlength(self, a, b):
        lena=len(a)
        lenb=len(b)
        if a==b:
            return -1
        if a!=b:
            return max(lena,lenb)