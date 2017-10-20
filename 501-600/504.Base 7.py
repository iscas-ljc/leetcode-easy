class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'
    	sym=1
    	if num<0:
    		sym=-1
    	result=''
    	num=abs(num)
    	while num:
    		result+=str(num%7)
    		num=num/7
    	result=result[::-1]
    	if sym==1:
    		return result
    	if sym==-1:
    		result='-'+result
    		return result

        """
        :type num: int
        :rtype: str
        """