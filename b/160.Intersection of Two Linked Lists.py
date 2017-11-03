# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None :
        	return None
        lena=1
        lenb=1
        a=headA
        b=headB
        while a.next != None:
        	a = a.next
        	lena += 1
        while b.next != None:
        	b = b.next
        	lenb += 1
        if a != b:
        	return None
        a=headA
        b=headB
        if lena>lenb :
        	for i in range (lena-lenb):
        		a=a.next
        else:
        	for i in range (lenb-lena):
        		b=b.next
        while a!=b:
        	a=a.next
        	b=b.next
        return a