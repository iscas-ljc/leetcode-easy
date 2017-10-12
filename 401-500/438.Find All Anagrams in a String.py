class Solution(object):
	def findAnagrams(self, s, p):
		lenp=len(p)
		lens=len(s)
		result=[]
		for i in range(0,lens-lenp):
			test=s[i:i+lenp]
			l1=list(p)
			l2=list(test)
			l1.sort()
			l2.sort()
			if l1==l2:
				result.append(i)
		return result