class Solution(object):
    def plusOne(self, digits):
        lend=len(digits)
        for i in range(lend-1,-1,-1):
        	if(digits[i]!=9):
        		digits[i]+=1
        		break
        	else:
        		digits[i]=0
        if digits[0]==0:
        	digits.append(0)
        	digits[0]=1
        return digits
        