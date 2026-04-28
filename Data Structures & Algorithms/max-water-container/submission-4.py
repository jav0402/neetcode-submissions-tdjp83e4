class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        res = 0
        for i in range(len(heights)):
            l, r = 0, len(heights) - 1
            while l < r:
                area = (r-l) * min(heights[l],heights[r])
                res = max(res, area)

                # move pointer of the lower heights
                if heights[l] < heights[r]:
                    l += 1
                elif heights[l] > heights[r]:
                    r -= 1
                # if height is == move left pointer
                else:
                    l += 1

            

        return res
        
            
                 
                