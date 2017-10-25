class Solution(object):
    def reverseWords(self, s):
        result=''
        for word in s.split():
            result+=word[::-1]+' '
        result=result[0:len(result)-1]
        #截掉最后一个空格
        return result
        