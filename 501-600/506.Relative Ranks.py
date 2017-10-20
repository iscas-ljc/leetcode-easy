class Solution(object):
    def findRelativeRanks(self, nums):
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + map(str, range(4, len(nums) + 1))
        return map(dict(zip(sort, rank)).get, nums)
#sort，rank从第一名到最后一名对应
#range(1,5) --> 1,2,3,4
#zip将两者绑定
#dict转化为字典类