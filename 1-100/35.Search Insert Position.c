int searchInsert(int* nums, int numsSize, int target) {
    if(numsSize==0||nums[0]>=target){
		return 0;
	}
    if(target>nums[numsSize-1]){
        return numsSize;
    }
	for(int i=0;i<numsSize;i++){
		if(nums[i]==target){
            return i;
        }
	}
    for(int j=0;j<numsSize;j++){
        if(nums[j]>target){
            return j;
        }

    }
    return 100;
}