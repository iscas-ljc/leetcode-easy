class Solution(object):
    def findWords(self, words):
    	group1=set("qwertyuiop")
    	group2=set("asdfghjkl")
    	group3=set("zxcvbnm")
    	result=[]
    	for word in words:
    		words=set(word.lower())
    		if words|group1==group1 or words|group2==group2 or words|group3==group3:
    			result.append(word)
    	return result
        """
        :type words: List[str]
        :rtype: List[str]
        """
#set操作将字符串变为字符集合
#|取两个集合的并集