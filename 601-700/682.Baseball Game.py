class Solution(object):
    def calPoints(self, ops):
    	result=[]
    	for i in ops:
    		if i!='+' and i!='D' and i!='C':
    			result.append(int(i))
    			#转化成int存入数组再陆续进行后续操作
    		if i=='+':
    			result.append(result[len(result)-1]+result[len(result)-2])
    		if i=='D':
    			result.append(result[len(result)-1]*2)
    		if i=='C':
    			result.pop()
    	return sum(result)