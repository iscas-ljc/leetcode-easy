class Solution(object):
    def judgeSquareSum(self, c):
        for i in range(int(c**0.5)+1):
            b=c-i**2
            if (int(b**0.5)**2)==b:
                return True
        return False