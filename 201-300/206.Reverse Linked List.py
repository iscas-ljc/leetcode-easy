class Solution(object):
    def reverseList(self, head):
    	if head is None:
    		return None
    	n=head
    	front=None
    	m=None
    	while(n):
    		m=n.next
    		n.next=front
    		front=n
    		n=m
    	head=front
    	return head
    		


        """
        :type head: ListNode
        :rtype: ListNode
        """
        