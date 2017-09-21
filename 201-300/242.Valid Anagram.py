class Solution(object):
    def deleteNode(self, node):
    	node.val = node.next.val
        node.next = node.next.next
#差评100%，不知道题目说的什么，抄的答案