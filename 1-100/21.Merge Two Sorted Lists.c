struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *head;
    struct ListNode *result;
    if(!l1&&l2){
        return l2;
    }
    if(l1&&!l2){
        return l1;
    }
    if(!l1&&!l2){
        return NULL;
    }
    if(l1->val>=l2->val){
        head=l2;
        l2=l2->next;
    }
    //  if(l1->val<l2->val)  错误，因为l2发生过改变
    else {
        head=l1;
        l1=l1->next;
    }
        result=head;
    while(l1&&l2){
        if(l1->val<l2->val){
            head->next=l1;
            l1=l1->next;
        }
        //  if(l1->val>=l2->val)  错误，因为l1发生过改变
        else{
            head->next=l2;
            l2=l2->next;
        }
        head->next->next=NULL;
        head=head->next;
    }
    if(l1){
        head->next=l1;
    }
    if(l2){
        head->next=l2;
    }
    return result;
}