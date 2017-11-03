class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
    	lenf=len(flowerbed)
    	if lenf==1:
    		if flowerbed[0]==0:
    			return n<=1
    		else:
    			return n==0
    	#只有一个元素，判断是不是为0，跟n比较
    	count=0
    	for i in xrange(lenf):
    		if i==0:
    			if flowerbed[1]==0 and flowerbed[0]==0:
    				flowerbed[0]=1
    				count+=1
    			continue
    		if i==lenf-1:
    			if flowerbed[i-1]==0 and flowerbed[i]==0:
    				flowerbed[i]=1
    				count+=1
    			continue
    		if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
    			flowerbed[i]=1
    			count+=1
    	#遍历一次，判断可以插画的位置
    	return n<=count