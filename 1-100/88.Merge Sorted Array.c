void merge(int* nums1, int m, int* nums2, int n) {
     int i1 = m - 1, i2 = n - 1, k = m + n - 1;
         while (i1>= 0 && i2>=0){
              if (nums1[i1] < nums2[i2])
             {
                 nums1[k--] = nums2[i2--];
             }
             else{
                nums1[k--] = nums1[i1--];
           }
       }
       while (i2 >= 0){
           nums1[k--] = nums2[i2--];
         }
 
        return;
}