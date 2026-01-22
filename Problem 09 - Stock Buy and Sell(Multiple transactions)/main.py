from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        
        profit = 0
        
        for i in range(1, len(arr)):
            if prices[i] > prices[i-1]:
                
                profit += prices[i] - prices[i-1]
                
        return profit