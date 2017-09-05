class Solution(object):
    def twoSum(self, numbers, target):
        lena=len(numbers)
        low=0
        high=lena-1
        while(numbers[low]+numbers[high]!=target):
            if(numbers[low]+numbers[high]<target):
                low+=1
            else:
                high-=1
        return[low+1,high+1]