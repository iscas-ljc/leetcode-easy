class Solution(object):
    def isHappy(self, n):
        arr=[]
        while n!=1 and n not in arr:
            arr.append(n)
            a=0
            while n!=0:
                a+=(n%10)*(n%10)
                n=n//10
            n=a
        return n==1
        """
        :type n: int
        :rtype: bool
        """
        