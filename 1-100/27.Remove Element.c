int removeElement(int* nums, int numsSize, int val) {
    int len=numsSize;
    for(int i=0;i<len;i++){
        if(nums[i]==val){
            if(i!=len-1){
            nums[i]=nums[len-1];
            i--;
            }
            len--;
        }
    }
    return len;
    
}