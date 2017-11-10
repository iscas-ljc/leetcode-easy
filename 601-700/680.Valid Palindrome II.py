class Solution(object):
    def validPalindrome(self, s):
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        #lambda为匿名函数，是一种函数声明方式
        size = len(s)
        lo, hi = 0, size - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return isPalindrome(strPart(s, lo)) or isPalindrome(strPart(s, hi))
            lo += 1
            hi -= 1
        return True
        #下面方法超时
'''
class Solution(object):
    def validPalindrome(self, s):
        a=list(s)
        b=list(s)
        a.reverse()        
        if b==a:
            return True
        lens=len(s)
        a=b=[]
        for i in range(lens):
            a=list(s)
            b=list(s)
            del a[i]
            del b[i]
            a.reverse()
            if a==b:
                return True
        return False
        #tips1：a=b改变b，a也会变
        #tips2: a.reverse() a==b True
        #       a.reverse()==b False
        