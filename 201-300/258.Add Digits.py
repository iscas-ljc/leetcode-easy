class Solution(object):
    def addDigits(self, num):
        while num>=10:
            test=0
            while num>0:
                test+=num%10
                num/=10
            num=test
        return num