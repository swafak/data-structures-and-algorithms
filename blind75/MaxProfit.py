
# Time Complexity: O(n) (single pass)
# Space Complexity: O(1) (only two variables)

def maxProfit(prices):
      

        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price 
                max_profit = max(max_profit, profit)
        return max_profit
    
    
prices = [2,11,15,7]
profit = maxProfit(prices)

print(profit)



# brute force

def maxProfit(self, prices):
        
        max_p = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j]- prices[i]
                max_p = max(max_p, profit)
        return max_p