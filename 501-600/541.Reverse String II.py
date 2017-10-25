class Solution(object):
    def reverseStr(self, s, k):
    	result=''
    	times=int(math.ceil(len(s)/(2.0*k)))
    	#ceil函数向上取整，求出翻转次数
    	for i in range(times):
    		result+=s[i*2*k:(i*2+1)*k][::-1]
    		#0-k翻转
    		result+=s[(i*2+1)*k:(i*2+2)*k]
    		#k-2k不变
    	return result
