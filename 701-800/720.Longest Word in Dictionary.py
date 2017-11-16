class Solution(object):
    def longestWord(self, words):
    	find=['']
    	result=''
    	for word in sorted(words):
    		#从字符长度遍历，1个字符的均可，2个字符找第一个字符是不是有
    		#因为前缀需要均在，找不到的就删除即可
    		#之后再比较长度
    		if word[:-1] in find:
    			find.append(word)
    			if len(word)>len(result):
    				result=word
    	return result
