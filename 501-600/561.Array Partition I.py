class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])
        #等价于return sum(sorted(nums)[::2])
        #将数组从小到大排序，取下标为偶数的元素求和即为答案
