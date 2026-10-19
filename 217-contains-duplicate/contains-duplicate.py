class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        for index,count in freq.items():    
            if count>1:
                return True
        return False        