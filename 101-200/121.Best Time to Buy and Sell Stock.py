class Solution(object):
    def maxProfit(self, prices):
        days=len(prices)
        if days==0:
            return 0
        min=prices[0]
        result=0
        for i in range (days):
            if(prices[i]<min):
                min=prices[i]
            elif prices[i]-min>result:
                result=prices[i]-min
        return result