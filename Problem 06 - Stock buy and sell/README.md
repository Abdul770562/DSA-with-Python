# Stock Buy and Sell - Max One Transaction Allowed

A comprehensive guide to understanding and implementing the "Best Time to Buy and Sell Stock" algorithm with detailed explanations, dry runs, and visual examples.

## 📋 Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Approach](#approach)
- [Algorithm](#algorithm)
- [Implementation](#implementation)
- [Complexity Analysis](#complexity-analysis)
- [Dry Run](#dry-run)
- [Visual Representation](#visual-representation)
- [Key Takeaways](#key-takeaways)
- [Common Mistakes](#common-mistakes)
- [Practice Problems](#practice-problems)

---

## 🎯 Problem Statement

Given an array `prices[]` where `prices[i]` represents the stock price on the `i-th` day, find the maximum profit you can achieve by buying and selling the stock **exactly once**.

### Requirements

✅ Buy stock on one day and sell on a future day  
✅ Only one transaction allowed (1 buy + 1 sell)  
✅ Stock must be bought before being sold  
✅ Return 0 if no profit is possible  
✅ O(n) time complexity  

### Key Rules

- **Must buy before selling** (can't sell then buy)
- **Only one transaction** (can't buy-sell-buy-sell)
- **Maximize profit** (selling price - buying price)

---

## 💡 Examples

### Example 1: Standard Case
```
Input:  prices = [7, 10, 1, 3, 6, 9, 2]
Output: 8

Explanation: 
- Buy on day 2 (price = 1)
- Sell on day 5 (price = 9)
- Profit = 9 - 1 = 8

Visual:
Day:    0   1   2   3   4   5   6
Price:  7  10   1   3   6   9   2
             ↑ Buy       ↑ Sell
             
Maximum profit = 9 - 1 = 8
```

### Example 2: Decreasing Prices
```
Input:  prices = [7, 6, 4, 3, 1]
Output: 0

Explanation: 
- Prices keep decreasing
- No day to sell at higher price than any previous day
- No profit possible

Visual:
Day:    0   1   2   3   4
Price:  7   6   4   3   1
        ↓   ↓   ↓   ↓   ↓  (Always decreasing)
        
Cannot make profit → Return 0
```

### Example 3: Increasing Prices
```
Input:  prices = [1, 3, 6, 9, 11]
Output: 10

Explanation: 
- Buy on day 0 (price = 1)
- Sell on day 4 (price = 11)
- Profit = 11 - 1 = 10

Visual:
Day:    0   1   2   3   4
Price:  1   3   6   9  11
        ↑ Buy           ↑ Sell
        
Maximum profit = 11 - 1 = 10
```

### Example 4: Single Price Point
```
Input:  prices = [5]
Output: 0

Explanation: 
- Only one day, cannot buy and sell
- Return 0
```

### Example 5: Two Days
```
Input:  prices = [3, 8]
Output: 5

Explanation: 
- Buy on day 0 (price = 3)
- Sell on day 1 (price = 8)
- Profit = 8 - 3 = 5
```

### Example 6: Multiple Peaks and Valleys
```
Input:  prices = [3, 1, 4, 8, 7, 2, 5]
Output: 7

Explanation: 
- Buy on day 1 (price = 1)
- Sell on day 3 (price = 8)
- Profit = 8 - 1 = 7

Note: We don't buy at 2 and sell at 5 (profit=3)
      because 1→8 (profit=7) is better
```

---

## 🚫 Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
- Array can have duplicate values
- Prices can be in any order
- Must complete transaction (buy + sell) to make profit

---

## 🧠 Approach

### Greedy Algorithm with Single Pass

The key insight is:
- **Track the minimum price** seen so far (best buying opportunity)
- **Calculate profit** at each price by selling at current price
- **Keep track of maximum profit** encountered

### Core Idea
```
For each price:
  1. Is this the lowest price so far? → Update minimum
  2. If we sell today, what's the profit? → current - minimum
  3. Is this profit better than our best? → Update maximum profit
```

### Why This Works

- We always know the **best buying price** up to current day
- At each day, we calculate **potential profit** if we sell today
- We keep the **best profit** we've seen
- No need to check all pairs (O(n²))

### Strategy Visualization
```
Prices: [7, 10, 1, 3, 6, 9, 2]

Day 0: min=7,  profit=0   (first day)
Day 1: min=7,  profit=3   (10-7)
Day 2: min=1,  profit=3   (new minimum found!)
Day 3: min=1,  profit=3   (3-1=2, not better)
Day 4: min=1,  profit=5   (6-1=5)
Day 5: min=1,  profit=8   (9-1=8) ← Best!
Day 6: min=1,  profit=8   (2-1=1, not better)

Result: 8
```

---

## 📝 Algorithm

### Step-by-Step Process
```
1. Initialize:
   - min_price = infinity (or very large number)
   - max_profit = 0

2. For each price in array:
   a. If price < min_price:
      - Update min_price = price
      - (Found better buying opportunity)
   
   b. Else:
      - Calculate profit = price - min_price
      - Update max_profit = max(profit, max_profit)
      - (Check if selling today gives better profit)

3. Return max_profit
```
---

## 💻 Implementation

### Python
```python
class Solution:
    def maximumProfit(self, prices):
        """
        Find maximum profit from single stock transaction
        
        Args:
            prices: List of stock prices
            
        Returns:
            Maximum profit possible (0 if no profit)
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        min_price = float("inf")  # Track minimum price seen
        max_profit = 0             # Track maximum profit found
        
        for price in prices:
            # Found new minimum price (better buying opportunity)
            if price < min_price:
                min_price = price
            
            # Calculate profit if we sell at current price
            else:
                profit = price - min_price
                max_profit = max(profit, max_profit)
        
        return max_profit
```
---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**
```
- Single pass through array: O(n)
- Each operation inside loop: O(1)
  * Comparison: O(1)
  * Subtraction: O(1)
  * max() function: O(1)

Total: O(n)
```

**Why O(n)?**
- We visit each element exactly once
- No nested loops
- Constant time operations per element

### Space Complexity: **O(1)**
```
Variables used:
- min_price: 1 variable
- max_profit: 1 variable
- price (loop variable): 1 variable
- profit (temporary): 1 variable

Total: O(1) constant space
```

**Why O(1)?**
- Only a fixed number of variables regardless of input size
- No extra arrays or data structures
- In-place calculation

### Comparison with Alternative Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| **One Pass (Greedy)** ⭐ | O(n) | O(1) | Optimal |
| Brute Force (Check all pairs) | O(n²) | O(1) | Too slow |
| Dynamic Programming | O(n) | O(n) | Unnecessary space |
| Kadane's Algorithm variant | O(n) | O(1) | Similar idea |
| Divide and Conquer | O(n log n) | O(log n) | Overcomplicated |

---

## 🔍 Detailed Dry Run

### Input Array
```
prices = [7, 10, 1, 3, 6, 9, 2]
```

### Initial State
```
min_price = ∞ (infinity)
max_profit = 0
```

---

## 🎬 Step-by-Step Execution

### **Iteration 0: price = 7**

**Before:**
```
min_price = ∞
max_profit = 0
price = 7
```

**Check: price < min_price?**
```
7 < ∞ → True ✅
```

**Action:**
```
Update min_price = 7
(Found first buying opportunity)
```

**After:**
```
min_price = 7
max_profit = 0
```

---

### **Iteration 1: price = 10**

**Before:**
```
min_price = 7
max_profit = 0
price = 10
```

**Check: price < min_price?**
```
10 < 7 → False ❌
```

**Action:**
```
Enter else block:
profit = price - min_price
profit = 10 - 7 = 3

max_profit = max(3, 0) = 3
```

**After:**
```
min_price = 7
max_profit = 3
```

**Meaning:** If we buy at 7 and sell at 10, profit = 3

---

### **Iteration 2: price = 1**

**Before:**
```
min_price = 7
max_profit = 3
price = 1
```

**Check: price < min_price?**
```
1 < 7 → True ✅
```

**Action:**
```
Update min_price = 1
(Found better buying opportunity!)
```

**After:**
```
min_price = 1
max_profit = 3
```

**Meaning:** Price of 1 is better than 7 for buying

---

### **Iteration 3: price = 3**

**Before:**
```
min_price = 1
max_profit = 3
price = 3
```

**Check: price < min_price?**
```
3 < 1 → False ❌
```

**Action:**
```
profit = 3 - 1 = 2
max_profit = max(2, 3) = 3
(Current profit not better than existing)
```

**After:**
```
min_price = 1
max_profit = 3
```

---

### **Iteration 4: price = 6**

**Before:**
```
min_price = 1
max_profit = 3
price = 6
```

**Check: price < min_price?**
```
6 < 1 → False ❌
```

**Action:**
```
profit = 6 - 1 = 5
max_profit = max(5, 3) = 5
(Better profit found!)
```

**After:**
```
min_price = 1
max_profit = 5
```

**Meaning:** Buy at 1, sell at 6 → profit = 5

---

### **Iteration 5: price = 9**

**Before:**
```
min_price = 1
max_profit = 5
price = 9
```

**Check: price < min_price?**
```
9 < 1 → False ❌
```

**Action:**
```
profit = 9 - 1 = 8
max_profit = max(8, 5) = 8
(Even better profit!)
```

**After:**
```
min_price = 1
max_profit = 8
```

**Meaning:** Buy at 1, sell at 9 → profit = 8 (Best so far!)

---

### **Iteration 6: price = 2**

**Before:**
```
min_price = 1
max_profit = 8
price = 2
```

**Check: price < min_price?**
```
2 < 1 → False ❌
```

**Action:**
```
profit = 2 - 1 = 1
max_profit = max(1, 8) = 8
(Current profit not better)
```

**After:**
```
min_price = 1
max_profit = 8
```

---

### Final Result
```
max_profit = 8
```

✅ **Best Transaction:** Buy at price 1, Sell at price 9

---

## 📊 Detailed Step Table

| Iteration | Price | min_price (before) | price < min? | Action | profit | max_profit (after) |
|-----------|-------|-------------------|--------------|--------|--------|-------------------|
| 0 | 7 | ∞ | ✅ Yes | Update min | - | 0 |
| 1 | 10 | 7 | ❌ No | Calc profit | 3 | 3 |
| 2 | 1 | 7 | ✅ Yes | Update min | - | 3 |
| 3 | 3 | 1 | ❌ No | Calc profit | 2 | 3 |
| 4 | 6 | 1 | ❌ No | Calc profit | 5 | 5 |
| 5 | 9 | 1 | ❌ No | Calc profit | 8 | **8** |
| 6 | 2 | 1 | ❌ No | Calc profit | 1 | 8 |

---

## 🎨 Visual Representation

### Price Graph with Buy/Sell Points
```
Price
 11│
 10│    ●
  9│                    ● ← SELL HERE (Profit = 8)
  8│
  7│ ●
  6│                ●
  5│
  4│
  3│            ●
  2│                        ●
  1│        ● ← BUY HERE
  0└────────────────────────────→ Day
    0   1   2   3   4   5   6

Prices: [7, 10, 1, 3, 6, 9, 2]
Best Transaction: Buy at 1, Sell at 9
Maximum Profit: 8
```

### State Evolution Diagram
```
Step 0: [7, 10, 1, 3, 6, 9, 2]
         ↑
      min=7, profit=0

Step 1: [7, 10, 1, 3, 6, 9, 2]
         └──↑
      min=7, profit=3 (10-7)

Step 2: [7, 10, 1, 3, 6, 9, 2]
              ↑
      min=1, profit=3 (new min!)

Step 3: [7, 10, 1, 3, 6, 9, 2]
              └──↑
      min=1, profit=3 (3-1=2, not better)

Step 4: [7, 10, 1, 3, 6, 9, 2]
              └─────↑
      min=1, profit=5 (6-1=5)

Step 5: [7, 10, 1, 3, 6, 9, 2]
              └────────↑
      min=1, profit=8 (9-1=8) ← BEST!

Step 6: [7, 10, 1, 3, 6, 9, 2]
              └───────────↑
      min=1, profit=8 (2-1=1, not better)
```

---

## 🔢 Another Detailed Example

### Input Array
```
prices = [3, 1, 4, 8, 7, 2, 5]
```

### Execution Steps

| Day | Price | min_price | Condition | profit | max_profit | Explanation |
|-----|-------|-----------|-----------|--------|-----------|-------------|
| 0 | 3 | ∞ | 3 < ∞ | - | 0 | First price, set min |
| 1 | 1 | 3 | 1 < 3 | - | 0 | New minimum found |
| 2 | 4 | 1 | 4 ≮ 1 | 3 | 3 | Sell at 4, profit = 3 |
| 3 | 8 | 1 | 8 ≮ 1 | 7 | **7** | Sell at 8, profit = 7 |
| 4 | 7 | 1 | 7 ≮ 1 | 6 | 7 | Not better than 7 |
| 5 | 2 | 1 | 2 ≮ 1 | 1 | 7 | Not better than 7 |
| 6 | 5 | 1 | 5 ≮ 1 | 4 | 7 | Not better than 7 |

**Result:** max_profit = 7 (Buy at 1, Sell at 8)

---

## 🎯 Key Takeaways

### Core Concepts

1. **Greedy Approach**: Make locally optimal choice at each step
2. **Single Pass**: Process array once from left to right
3. **Track Minimum**: Always know the best buying price so far
4. **Calculate Potential**: Check profit at each selling opportunity
5. **Update Maximum**: Keep the best profit found

### Memory Trick

> **"Buy low, sell high - track the lowest, calculate at every high!"**

### Algorithm Pattern
```
Pattern: Tracking Min/Max with Single Pass
Common in: Stock problems, Kadane's algorithm, Water trapping

Template:
1. Initialize tracker variable (min/max)
2. Initialize result variable
3. For each element:
   - Update tracker if better found
   - Calculate result using current element and tracker
   - Update result if better
4. Return result
```

### When to Use This Approach

- ✅ Finding optimal buy-sell in single transaction
- ✅ Maximum subarray problems
- ✅ Best time to do something once
- ✅ Problems requiring tracking of previous optimal value

---

## ⚠️ Common Mistakes

### Mistake 1: Checking All Pairs (Brute Force)
```python
# ❌ Wrong - O(n²) time complexity
def maximumProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(profit, max_profit)
    return max_profit

# Problem: Too slow for large inputs
# Time: O(n²) instead of O(n)
```

**Correct:**
```python
# ✅ Correct - O(n) single pass
def maximumProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit, max_profit)
    return max_profit
```

---

### Mistake 2: Updating max_profit in Wrong Place
```python
# ❌ Wrong - Updates profit even when updating min
def maximumProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price  # Always 0 when price is new min!
        max_profit = max(profit, max_profit)
    return max_profit

# Problem: When price becomes new minimum,
# profit = price - price = 0
# This masks actual profit calculations
```

**Correct:**
```python
# ✅ Correct - Only calculate profit when not updating min
def maximumProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:  # Only calculate when price >= min_price
            profit = price - min_price
            max_profit = max(profit, max_profit)
    return max_profit
```

---

### Mistake 3: Not Handling Empty or Single Element
```python
# ❌ Wrong - Doesn't handle edge cases
def maximumProfit(prices):
    min_price = prices[0]  # IndexError if empty!
    max_profit = 0
    for price in prices[1:]:
        # ...
```

**Correct:**
```python
# ✅ Correct - Handles all edge cases
def maximumProfit(prices):
    if not prices or len(prices) < 2:
        return 0
    
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit, max_profit)
    return max_profit
```

---

### Mistake 4: Returning Negative Profit
```python
# ❌ Wrong - Might return negative profit
def maximumProfit(prices):
    min_price = prices[0]
    max_profit = float("-inf")  # Wrong initialization!
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(profit, max_profit)
    return max_profit

# Problem: If all prices decrease, returns negative
# Example: [5, 4, 3, 2, 1] → returns -4
# Should return 0 (no profit possible)
```

**Correct:**
```python
# ✅ Correct - Initialize max_profit to 0
def maximumProfit(prices):
    min_price = float("inf")
    max_profit = 0  # Minimum profit is 0 (don't trade)
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit, max_profit)
    return max_profit
```

---

### Mistake 5: Selling Before Buying
```python
# ❌ Wrong - Might sell before buying
def maximumProfit(prices):
    # Finds max and min in entire array
    max_price = max(prices)
    min_price = min(prices)
    return max_price - min_price

# Problem: Max might come before min
# Example: [9, 1, 5] → returns 9-1=8 (Wrong!)
# Can't sell at 9 then buy at 1
# Correct answer: 5-1=4
```

**Correct:**
```python
# ✅ Correct - Ensures chronological order
def maximumProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:  # Process in order
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(profit, max_profit)
    return max_profit
```

---

## 🔗 Practice Problems

### Similar Problems on LeetCode

- [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Exact same problem
- [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) - Multiple transactions
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) - At most 2 transactions
- [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) - At most k transactions
- [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)

### GeeksforGeeks Problems

- [Stock buy and sell](https://www.geeksforgeeks.org/stock-buy-sell/)
- [Maximum profit by buying and selling a share at most twice](https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/)
- [Maximum profit by buying and selling a share at most k times](https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/)

### Variations to Try

#### 1. Multiple Transactions Allowed
```python
def maxProfitMultiple(prices):
    """
    Can buy and sell multiple times
    Buy only after selling previous stock
    """
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

#### 2. With Transaction Fee
```python
def maxProfitWithFee(prices, fee):
    """
    Pay fee for each transaction
    """
    cash = 0  # Max profit if don't own stock
    hold = -prices[0]  # Max profit if own stock
    
    for i in range(1, len(prices)):
        cash = max(cash, hold + prices[i] - fee)
        hold = max(hold, cash - prices[i])
    
    return cash
```

#### 3. With Cooldown
```python
def maxProfitWithCooldown(prices):
    """
    Must wait 1 day after selling before buying again
    """
    if not prices:
        return 0
    
    sold = 0
    hold = -prices[0]
    rest = 0
    
    for price in prices[1:]:
        prev_sold = sold
        sold = hold + price
        hold = max(hold, rest - price)
        rest = max(rest, prev_sold)
    
    return max(sold, rest)
```

---

## 🧪 Test Cases
```python
# Test Case 1: Standard case
assert maximumProfit([7, 10, 1, 3, 6, 9, 2]) == 8

# Test Case 2: Decreasing prices (no profit)
assert maximumProfit([7, 6, 4, 3, 1]) == 0

# Test Case 3: Increasing prices
assert maximumProfit([1, 3, 6, 9, 11]) == 10

# Test Case 4: Single element
assert maximumProfit([5]) == 0

# Test Case 5: Two elements (profit possible)
assert maximumProfit([3, 8]) == 5

# Test Case 6: Two elements (no profit)
assert maximumProfit([8, 3]) == 0

# Test Case 7: All same prices
assert maximumProfit([5, 5, 5, 5]) == 0

# Test Case 8: Multiple peaks
assert maximumProfit([3, 1, 4, 8, 7, 2, 5]) == 7

# Test Case 9: Peak at start
assert maximumProfit([10, 5, 3, 1]) == 0

# Test Case 10: Peak at end
assert maximumProfit([1, 3, 5, 10]) == 9

# Test Case 11: With zeros
assert maximumProfit([0, 6, -3, 7]) == 10  # 7 - (-3)

# Test Case 12: Large numbers
assert maximumProfit([10000, 1, 10000]) == 9999

# Test Case 13: Empty array
assert maximumProfit([]) == 0

# Test Case 14: V-shaped (valley)
assert maximumProfit([5, 2, 1, 2, 5]) == 4

# Test Case 15: Inverted V (peak)
assert maximumProfit([1, 5, 3, 1]) == 4
```

---

## 📝 Interview Tips

### What Interviewers Look For

1. ✅ **Understanding of greedy approach**
2. ✅ **Optimal O(n) solution (not brute force)**
3. ✅ **Handling edge cases**
4. ✅ **Clean, readable code**
5. ✅ **Explanation of why it works**

### Common Interview Questions

**Q: Why not check all buy-sell pairs?**
A: That would be O(n²) - too slow for large inputs.
The greedy approach achieves O(n) by tracking minimum
price and calculating profit at each step.

**Q: What if prices keep decreasing?**
A: max_profit stays at 0 because we initialize it to 0
and never find a positive profit. Return 0 means
"don't trade" which is the correct answer.

**Q: Can we sell before we buy?**
A: No, because we process prices left-to-right and
always use min_price from BEFORE current index.
This ensures chronological order.

**Q: What if we want the actual buy/sell days?**
```python
# Track indices when updating max_profit
def maximumProfitWithDays(prices):
    min_price = float("inf")
    max_profit = 0
    buy_day = 0
    sell_day = 0
    temp_buy = 0
    
    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            temp_buy = i
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                buy_day = temp_buy
                sell_day = i
    
    return max_profit, buy_day, sell_day
```

**Q: Time and space complexity?**
A: Time: O(n) - single pass through array
Space: O(1) - only two variables
This is optimal for this problem.

---

## 🎉 Congratulations!

You now completely understand the **Stock Buy and Sell (Single Transaction)** algorithm!

**Remember**: 
> "Track the minimum, calculate at every step, keep the maximum - profit maximized!" 📈💰

---

## 📄 License

This documentation is free to use for educational purposes.

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Algorithm Difficulty**: Easy ⭐  
**Topics**: Arrays, Greedy, Dynamic Programming, Kadane's Algorithm Variant  
**Companies**: Amazon, Microsoft, Google, Facebook, Apple, Bloomberg
This comprehensive README covers everything about the stock buy-sell problem including detailed explanations, multiple dry runs, visual representations, common mistakes, edge cases, test cases, and interview preparation tips!Claude is AI and can make mistakes. Please double-check responses. Sonnet 4.5Clau
