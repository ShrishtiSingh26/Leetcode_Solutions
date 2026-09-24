class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            summ=sum((int(y) for y in str(nums[i])))
            if summ==i:
                return i
            
        return -1
            
        