class Solution(object):
    def minMoves(self, nums):
         return sum(nums) - len(nums) * min(nums)
#数学问题的答案