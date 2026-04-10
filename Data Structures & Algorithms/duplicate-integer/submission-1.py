class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i],nums[j])
                if nums[i] == nums[j]:
                    return True
            
        return False