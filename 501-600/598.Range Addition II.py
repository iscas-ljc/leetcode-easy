class Solution(object):
    def maxCount(self, m, n, ops):
        if not ops:
            return m*n
        #如果没有操作，则矩阵全是0，有mn个
        return min(i[0] for i in ops)*min(i[1] for i in ops)
        #向左上角缩小
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        