class Solution:
    # learning
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0

        for price in prices:
            # checks left to right 
            if price < minPrice:
                # if next value is lower save
                minPrice = price
            else:
                # else comp for max price
                maxPrice = max(maxPrice, price - minPrice)
        return maxPrice
