int removeDuplicates(int* nums, int numsSize) {
    int result=0;
    for(int i=0;i<numsSize;i++){
        while(i>0&&i<numsSize&&nums[i]==nums[i-1])i++;
        if(i<numsSize){
            nums[result++] = nums[i];//因为是排序好的数列，用后面的数字代替前面重复的数字12234---12334---12344---1234\0
        }
    }
    return result;
        
}