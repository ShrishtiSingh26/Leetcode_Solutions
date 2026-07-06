# Last updated: 7/6/2026, 11:54:10 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dict1={}
4        l=len(nums)
5        for i in range(l):
6            dict1[i]=nums[i]
7        nums.sort()
8        i=0
9        j=l-1
10        while i<j:
11            if nums[i]+nums[j]==target:
12                return [k for k, v in dict1.items() if v==nums[i] or v==nums[j] ]
13            elif nums[i]+nums[j]>target:
14                j-=1
15            elif nums[i]+nums[j]<target:
16                i+=1