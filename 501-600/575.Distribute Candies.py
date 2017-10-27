class Solution(object):
    def distributeCandies(self, candies):
        kind=len(set(candies))
        return min(kind,len(candies)/2)
        """
        :type candies: List[int]
        :rtype: int
        """
        