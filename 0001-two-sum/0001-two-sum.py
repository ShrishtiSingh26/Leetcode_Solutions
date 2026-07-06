class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        l=len(nums)
        for i in range(l):
            dict1[i]=nums[i]
        nums.sort()
        i=0
        j=l-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [k for k, v in dict1.items() if v==nums[i] or v==nums[j] ]
            elif nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1