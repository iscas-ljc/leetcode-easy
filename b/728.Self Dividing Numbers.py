class Solution(object):
    def selfDividingNumbers(self, left, right):
    	result=[]
    	for i in range(left,right+1):
    		if '0' not in str(i) and all(i%int(digit)==0 for digit in str(i)):
    			#all表示所有都要满足,不加all满足一个就行
    		    result.append(i)
    	return result