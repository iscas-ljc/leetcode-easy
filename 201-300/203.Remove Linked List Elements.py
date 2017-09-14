class Solution(object):
    def removeElements(self, head, val):
        if head==None:
            return head
        p=ListNode(-1)
        p.next=head
        a=p
        while head!=None:
            if head.val==val:
                a.next=head.next
            else:
                a=a.next
            head=head.next
        return p.next