int max(int a,int b){
    if(a>=b){
        return a;
    }else{
        return b;
    }
}
//动态规划
int maxSubArray(int* nums, int numsSize) {
   int sum = nums[numsSize - 1];
   int maxSum = sum;
   for (int i = numsSize - 2; i >= 0; i--) {
       sum = max(nums[i], sum + nums[i]);
      maxSum = max(maxSum, sum);
    }
 
   return maxSum;
}