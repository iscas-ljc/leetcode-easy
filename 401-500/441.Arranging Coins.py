class Solution(object):
     def arrangeCoins(self, n):
         from math import sqrt
         return int((sqrt(1+8*n) - 1) / 2)
#循环减法会超时