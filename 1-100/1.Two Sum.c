/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    //int i,j,k;
    int *a=(int*)malloc(2*sizeof(1));
    for(int i=0;i<numsSize;i++){
        for(int j=0;j<i;j++){
        if(nums[i]+nums[j]==target){
        a[0]=i;
        a[1]=j;
        }
        }
    }
    return a;
}