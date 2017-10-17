class Solution(object):
    def repeatedSubstringPattern(self, s):
    	lens=len(s)
    	if lens==0:
    		return False
    	for i in range(1,lens):
    		if lens%i==0:
    			if s[:i]*(lens/i)==s:
    				return True
    	return False