class Solution(object):
    def constructRectangle(self, area):
    	mid=int(math.sqrt(area))
    	for i in range(mid,0,-1):
    		if area%i==0:
    			return [area/i,i]