class Solution(object):
    def compress(self, chars):
        last, n, y = chars[0], 1, 0
        for x in range(1, len(chars)):
            c = chars[x]
            if c == last: n += 1
            else:
                for ch in last + str(n > 1 and n or ''):
                    chars[y] = ch
                    y += 1
                last, n = c, 1
        for ch in last + str(n > 1 and n or ''):
            chars[y] = ch
            y += 1
        while len(chars) > y: chars.pop()
        return y
'''
class Solution(object):
    def compress(self, chars):
    	lenc=len(chars)
    	if lenc==0:
    		return 0
    	result=''
        result+=chars[0]
    	times=1
    	for i in range(1,lenc):
    		if chars[i]!=chars[i-1]:
    			if times!=1:
    				result+=str(times)
    			result+=chars[i]
    			times=1
    		if chars[i]==chars[i-1]:
    			#if times==1 or times==9 or times==99 or times==999 or times==9999:
    			#	result+=1
    			times+=1
    	return result
'''