class Solution(object):
    def maxProfit(self, prices):
        num=len(prices)
        profit=0
        for i in range(1,num):
        	if(prices[i]>prices[i-1]):
        		profit+=prices[i]-prices[i-1]
        return profit