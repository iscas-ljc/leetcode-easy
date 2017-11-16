class Solution(object):
    def isOneBitCharacter(self, bits):
    	lenb=len(bits)
    	i=0
    	while i<lenb-1:
    		if bits[i]==0:
    			i+=1
    		if buits[i]==1:
    			i+=2
    		#1后面的数字一定跟他一组，就跳到下下个
    		#单独的0自己一组，跳到下一个
    		#最后跳出去就结尾不是0，跳到0就是0
    	return i>lenb-1