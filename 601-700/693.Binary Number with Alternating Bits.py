class Solution(object):
    def hasAlternatingBits(self, n):
    	b=bin(n)
    	lenb=len(b)
        b=b[2:lenb]
        lenb=len(b)
        #bin函数会返回'0b....'需要进行截取
    	if lenb==0:
    		return True
    	judge=b[0]
    	for i in range(1,lenb):
    	#逐位判断
    		if judge==b[i]:
    			return False
    		elif b[i]!='1' and b[i]!='0':
    			return False
    		elif judge!=b[i]:
    			judge=b[i]
    	return True
