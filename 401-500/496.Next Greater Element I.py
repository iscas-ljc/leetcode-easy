class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]

'''
栈stack维护nums的递减子集，记nums的当前元素为n，栈顶元素为top

重复弹出栈顶，直到stack为空，或者top大于n为止

将所有被弹出元素的next greater element置为n

'''