class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        maxl = 0
        maxr = 0

        l, r = 0, len(height) - 1

        while l < r:
            # find max height of both pointer
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)

            if height[l] < height[r]:
                # move left pointer if lower than right height
                total = total + (maxl - height[l])
                l += 1
            elif height[l] > height[r]:
                # mover right pointer if lower than left height
                total = total + (maxr - height[r])
                r -= 1
            else:
                # if same move left pointer
                total = total + (maxl - height[l])
                l += 1
    
        return total
        