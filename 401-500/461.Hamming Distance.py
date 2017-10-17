class Solution(object):
    def hammingDistance(self, x, y):
    	t=x^y
        return bin(t).count("1")
        """
        :type x: int
        :type y: int
        :rtype: int
        """
#二进制同位不同数-->相交为1的个数