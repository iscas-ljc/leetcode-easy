class Solution(object):
    def findRestaurant(self, list1, list2):
        dict={word1:number1 for number1,word1 in enumerate(list1)}
        #建立一个单词对应序号的字典
        result=[]
        summin=len(list1)+len(list2)
        #定一个不能超越的极限值
        for number2,word2 in enumerate(list2):
            if word2 not in dict:
                continue
            nowsum=dict[word2]+number2
            #计算当前序号和
            if nowsum<summin:
                summin=nowsum
                result=[word2]
            elif nowsum==summin:
            #由于if改过summin的值，不能写一个并列的if
                result.append(word2)
        return result