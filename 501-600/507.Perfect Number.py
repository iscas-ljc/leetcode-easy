class Solution(object):
    def checkPerfectNumber(self, num):
    	result=1
    	x=2
    	while x*x<=num:
    		if num%x==0:
    			result+=x
    			if x*x!=num:
    				result+=(num/x)
    				#平方根只加一次
    		x+=1
    	return num>1 and result==num