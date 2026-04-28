class Solution:
    # learning 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort array
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                # remove dups as array is sorted if left num == cur num (skip cur num)
                continue

            l, r = i + 1, len(nums) - 1

            while l < r: # this is twosum
                total = nums[i] + nums[l] + nums[r]
                 
                #moving left pointer
                if total < 0:
                    l += 1
                # move right pointer
                elif total > 0:
                    r -= 1

                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # if = 0 move both pointer
                    l += 1
                    

                    while l < r and nums[l] == nums[l - 1]:
                        # if same value as right num move right pointer
                        l += 1
                    


        return res