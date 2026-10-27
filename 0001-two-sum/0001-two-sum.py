class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict1={}
        for i in range(len(nums)):
            dict1[i]=nums[i]
        nums.sort()
        low=0
        high=len(nums)-1
        while low<high:
            
            if nums[low]+nums[high]==target:
                return [k for k, v in dict1.items() if v == nums[low] or v == nums[high]]
            elif nums[low]+nums[high]>target:
                high-=1
            elif nums[low]+nums[high]<target:
                low+=1