class Solution(object):
    def findContentChildren(self, g, s):
    	g.sort()
    	s.sort()
    	i=0
    	j=0
    	result=0
    	while i!=len(g) and j!=len(s):
    		if g[i]<=s[j]:
    			result+=1
    			i+=1
    			j+=1
    		else:
    			j+=1
    	return result