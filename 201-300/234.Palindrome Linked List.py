class Solution(object):
    def isPalindrome(self, head):
        s=[]
        while head!=None:
            s.append(head.val)
            head=head.next
        for i in range(len(s)/2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
#翻转整个链表比较