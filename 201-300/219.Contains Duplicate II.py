class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False
#python大括号{ }花括号：
#代表dict字典数据类型，字典是由键对值组组成。
#冒号':'分开键和值，逗号','隔开组。