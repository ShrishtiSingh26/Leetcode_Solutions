class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        x=dict1.values()
        for n in x:
            if n>1:
                return True
            
        return False