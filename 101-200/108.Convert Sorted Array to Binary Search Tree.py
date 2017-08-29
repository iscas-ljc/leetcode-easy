# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
    	if len(nums)==0:
    		return None;
    	mid=len(nums)//2     # //表示整除   /表示浮点数除法
    	root=TreeNode(nums[mid])
    	root.left=self.sortedArrayToBST(nums[:mid]) #[:number] 取前number个数
    	root.right=self.sortedArrayToBST(nums[mid+1:])#[number:] 从number到结束
    	return root