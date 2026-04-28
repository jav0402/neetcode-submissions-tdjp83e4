class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        total = 0

        maxl = 0
        maxr = 0
        l, r = 0, len(height) - 1

        while l < r:
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)

            if height[l] < height[r]:
                total = total + (maxl - height[l])
                l += 1
            elif height[l] > height[r]:
                total = total + (maxr - height[r])
                r -= 1
            else:
                total = total + (maxl - height[l])
                l += 1

        return total
        