class Solution:
    def maximumProfit(self, prices):
        # code here
        
        min_price = float("inf")
        max_profit = 0
        
        
        for price in prices:
            
            if price < min_price:
                
                min_price = price
                
            else: 
                
                profit = price - min_price
                max_profit = max(profit, max_profit)  
                
                
        return max_profit
        