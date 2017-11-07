class Solution(object):
    def imageSmoother(self, M):
    	r=len(M)
    	c=len(M[0])
    	result=[]
    	for i in range(r):
    		row=[]
    		for j in range(c):
    		#判定上下左右存不存在，存在就加上然后数量+1
    			num=1
    			a=M[i][j]
    			if i-1>=0 and j-1>=0:
    				a+=M[i-1][j-1]
    				num+=1
    			if i-1>=0:
    				a+=M[i-1][j]
    				num+=1
    			if i-1>=0 and j+1<c:
    				a+=M[i-1][j+1]
    				num+=1
    			if j-1>=0:
    				a+=M[i][j-1]
    				num+=1
    			if j+1<c:
    				a+=M[i][j+1]
    				num+=1
    			if i+1<r:
    				a+=M[i+1][j]
    				num+=1
    			if i+1<r and j-1>=0:
    				a+=M[i+1][j-1]
    				num+=1
    			if i+1<r and j+1<c:
    				a+=M[i+1][j+1]
    				num+=1
    			row.append(a/num)
    		result.append(row)
    	return result