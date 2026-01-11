# Maximum Subarray Sum (Kadane's Algorithm)

A comprehensive guide to understanding and implementing **Kadane's Algorithm** for finding the maximum sum of a contiguous subarray with detailed explanations, dry runs, and visual examples.

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

Given an integer array `arr[]`, find the **maximum sum** of a contiguous subarray (containing at least one element).

### Requirements

✅ Find contiguous subarray with maximum sum  
✅ Subarray must contain at least one element  
✅ Handle negative numbers  
✅ O(n) time complexity  
✅ O(1) space complexity  

### What is a Subarray?

A **subarray** is a continuous part of an array.
```
Array: [1, 2, 3, 4, 5]

Valid subarrays:
[1], [2], [3], [4], [5]
[1, 2], [2, 3], [3, 4], [4, 5]
[1, 2, 3], [2, 3, 4], [3, 4, 5]
[1, 2, 3, 4], [2, 3, 4, 5]
[1, 2, 3, 4, 5]

Invalid (not contiguous):
[1, 3], [1, 4], [2, 5], etc.
```

---

## 💡 Examples

### Example 1: Mixed Positive and Negative
```
Input:  arr = [2, 3, -8, 7, -1, 2, 3]
Output: 11

Explanation: 
Subarray [7, -1, 2, 3] has maximum sum
7 + (-1) + 2 + 3 = 11

Visual:
[2, 3, -8, 7, -1, 2, 3]
           └──────────┘
           Sum = 11 (Maximum)
```

### Example 2: All Negative Numbers
```
Input:  arr = [-2, -4]
Output: -2

Explanation: 
When all numbers are negative, choose the least negative
Subarray [-2] has maximum sum -2

Note: We must include at least one element
```

### Example 3: All Positive Numbers
```
Input:  arr = [5, 4, 1, 7, 8]
Output: 25

Explanation: 
All numbers are positive, so include entire array
[5, 4, 1, 7, 8]
5 + 4 + 1 + 7 + 8 = 25
```

### Example 4: Single Element
```
Input:  arr = [42]
Output: 42

Explanation: Only one element, that's the answer
```

### Example 5: Negative at Start
```
Input:  arr = [-3, 4, -1, 2, 1, -5, 4]
Output: 6

Explanation: 
Subarray [4, -1, 2, 1] has maximum sum
4 + (-1) + 2 + 1 = 6

Visual:
[-3, 4, -1, 2, 1, -5, 4]
     └─────────┘
     Sum = 6 (Maximum)
```

### Example 6: Large Negative in Middle
```
Input:  arr = [1, 2, -10, 3, 4]
Output: 7

Explanation: 
Don't include the -10, restart from 3
Subarray [3, 4] has maximum sum = 7

Visual:
[1, 2, -10, 3, 4]
 └──┘  X   └───┘
Sum=3      Sum=7 (Maximum)
```

---

## 🚫 Constraints

- `1 <= arr.size() <= 10^5`
- `-10^4 <= arr[i] <= 10^4`
- Array can have all negative numbers
- Array can have all positive numbers
- Array can have mix of positive and negative

---

## 🧠 Approach

### Kadane's Algorithm (Dynamic Programming)

**Core Idea**: At each position, decide whether to:
1. **Extend** the current subarray (add current element)
2. **Start new** subarray from current element

### Key Insight
```
At each element, we have two choices:
1. currSum + arr[i]  (extend current subarray)
2. arr[i]            (start fresh from here)

We choose whichever is larger!

If currSum becomes negative, it will only decrease
future sums, so we reset to 0 (start fresh).
```

### Why This Works

- **Negative sum hurts future**: If current sum is negative, adding it to any future element only makes things worse
- **Greedy choice**: At each step, make the locally optimal decision
- **Track maximum**: Keep updating the best sum we've seen

### Strategy Visualization
```
Array: [2, 3, -8, 7, -1, 2, 3]

Position 0: currSum = 2,  maxSum = 2
Position 1: currSum = 5,  maxSum = 5  (2+3)
Position 2: currSum = 0,  maxSum = 5  (5-8=-3, reset!)
Position 3: currSum = 7,  maxSum = 7  (fresh start)
Position 4: currSum = 6,  maxSum = 7  (7-1)
Position 5: currSum = 8,  maxSum = 8  (6+2)
Position 6: currSum = 11, maxSum = 11 (8+3) ✓

Answer: 11
```

---

## 📝 Algorithm

### Kadane's Algorithm Steps
```
1. Initialize:
   - currSum = 0 (current subarray sum)
   - maxSum = -∞ (maximum sum found)

2. For each element in array:
   a. Add element to currSum
   b. Update maxSum if currSum is larger
   c. If currSum becomes negative:
      - Reset currSum to 0 (start fresh)

3. Return maxSum
```

### Alternative Formulation
```
function maxSubarraySum(arr):
    currSum = 0
    maxSum = -infinity
    
    for num in arr:
        # At each position, choose better option:
        currSum = max(num, currSum + num)
        maxSum = max(currSum, maxSum)
    
    return maxSum
```

---

## 💻 Implementation

### Python (Given Solution)
```python
class Solution:
    def maxSubarraySum(self, arr):
        """
        Find maximum sum of contiguous subarray using Kadane's Algorithm
        
        Args:
            arr: List of integers
            
        Returns:
            Maximum subarray sum
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        currSum = 0                  # Current subarray sum
        maxSum = float('-inf')       # Maximum sum found
        
        for num in range(len(arr)):
            currSum += arr[num]      # Add current element
            maxSum = max(currSum, maxSum)  # Update maximum
            
            if currSum < 0:          # Negative sum won't help
                currSum = 0          # Start fresh
        
        return maxSum
```

### Python (Cleaner Version)
```python
class Solution:
    def maxSubarraySum(self, arr):
        currSum = 0
        maxSum = float('-inf')
        
        for num in arr:  # Iterate through values directly
            currSum += num
            maxSum = max(currSum, maxSum)
            
            if currSum < 0:
                currSum = 0
        
        return maxSum
```
---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**
```
- Single pass through array: O(n)
- Each operation inside loop: O(1)
  * Addition: O(1)
  * Comparison: O(1)
  * max() function: O(1)

Total: O(n)
```

**Why O(n)?**
- Visit each element exactly once
- No nested loops
- Constant time operations per element

### Space Complexity: **O(1)**
```
Variables used:
- currSum: 1 variable
- maxSum: 1 variable
- num (loop variable): 1 variable

Total: O(1) constant space
```

**Why O(1)?**
- Only three variables regardless of input size
- No extra arrays or data structures
- In-place calculation

### Comparison with Alternative Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| **Kadane's Algorithm** ⭐ | O(n) | O(1) | Optimal |
| Brute Force (All subarrays) | O(n³) | O(1) | Too slow |
| Brute Force (Optimized) | O(n²) | O(1) | Still slow |
| Divide and Conquer | O(n log n) | O(log n) | Recursive |
| Dynamic Programming (Array) | O(n) | O(n) | Unnecessary space |

---

## 🔍 Detailed Dry Run

### Input Array
```
arr = [2, 3, -8, 7, -1, 2, 3]
```

### Initial State
```
currSum = 0
maxSum = -∞ (negative infinity)
```

---

## 🎬 Step-by-Step Execution

### **Iteration 0: num = 2**

**Before:**
```
currSum = 0
maxSum = -∞
arr[0] = 2
```

**Operations:**
```
currSum += arr[0]
currSum = 0 + 2 = 2

maxSum = max(currSum, maxSum)
maxSum = max(2, -∞) = 2

Check: currSum < 0?
2 < 0 → False ❌
No reset
```

**After:**
```
currSum = 2
maxSum = 2
```

**Meaning:** Subarray [2] has sum 2

---

### **Iteration 1: num = 3**

**Before:**
```
currSum = 2
maxSum = 2
arr[1] = 3
```

**Operations:**
```
currSum += arr[1]
currSum = 2 + 3 = 5

maxSum = max(5, 2) = 5

Check: currSum < 0?
5 < 0 → False ❌
```

**After:**
```
currSum = 5
maxSum = 5
```

**Meaning:** Subarray [2, 3] has sum 5

---

### **Iteration 2: num = -8**

**Before:**
```
currSum = 5
maxSum = 5
arr[2] = -8
```

**Operations:**
```
currSum += arr[2]
currSum = 5 + (-8) = -3

maxSum = max(-3, 5) = 5
(No update, -3 is not better)

Check: currSum < 0?
-3 < 0 → True ✅
currSum = 0  (RESET!)
```

**After:**
```
currSum = 0
maxSum = 5
```

**Meaning:** [2, 3, -8] = -3 is worse than [2, 3] = 5. Negative sum won't help future, so reset.

---

### **Iteration 3: num = 7**

**Before:**
```
currSum = 0
maxSum = 5
arr[3] = 7
```

**Operations:**
```
currSum += arr[3]
currSum = 0 + 7 = 7

maxSum = max(7, 5) = 7
(New maximum found!)

Check: currSum < 0?
7 < 0 → False ❌
```

**After:**
```
currSum = 7
maxSum = 7
```

**Meaning:** Starting fresh from [7], sum = 7 (new best)

---

### **Iteration 4: num = -1**

**Before:**
```
currSum = 7
maxSum = 7
arr[4] = -1
```

**Operations:**
```
currSum += arr[4]
currSum = 7 + (-1) = 6

maxSum = max(6, 7) = 7
(Not better than current max)

Check: currSum < 0?
6 < 0 → False ❌
```

**After:**
```
currSum = 6
maxSum = 7
```

**Meaning:** [7, -1] = 6, not as good as [7] = 7 alone, but still positive so keep going

---

### **Iteration 5: num = 2**

**Before:**
```
currSum = 6
maxSum = 7
arr[5] = 2
```

**Operations:**
```
currSum += arr[5]
currSum = 6 + 2 = 8

maxSum = max(8, 7) = 8
(New maximum!)

Check: currSum < 0?
8 < 0 → False ❌
```

**After:**
```
currSum = 8
maxSum = 8
```

**Meaning:** [7, -1, 2] = 8 (new best)

---

### **Iteration 6: num = 3**

**Before:**
```
currSum = 8
maxSum = 8
arr[6] = 3
```

**Operations:**
```
currSum += arr[6]
currSum = 8 + 3 = 11

maxSum = max(11, 8) = 11
(New maximum!)

Check: currSum < 0?
11 < 0 → False ❌
```

**After:**
```
currSum = 11
maxSum = 11
```

**Meaning:** [7, -1, 2, 3] = 11 (best subarray!)

---

### Final Result
```
maxSum = 11
```

✅ **Best Subarray:** [7, -1, 2, 3] with sum 11

---

## 📊 Detailed Step Table

| Iteration | arr[i] | currSum (before) | currSum (after add) | maxSum (before) | maxSum (after) | Reset? |
|-----------|--------|------------------|---------------------|-----------------|----------------|--------|
| 0 | 2 | 0 | 2 | -∞ | 2 | ❌ |
| 1 | 3 | 2 | 5 | 2 | 5 | ❌ |
| 2 | -8 | 5 | -3 | 5 | 5 | ✅ → 0 |
| 3 | 7 | 0 | 7 | 5 | 7 | ❌ |
| 4 | -1 | 7 | 6 | 7 | 7 | ❌ |
| 5 | 2 | 6 | 8 | 7 | 8 | ❌ |
| 6 | 3 | 8 | 11 | 8 | **11** | ❌ |

---

## 🎨 Visual Representation

### Subarray Sum Evolution
```
Array: [2, 3, -8, 7, -1, 2, 3]

Step 0: [2]
        Sum = 2 ✓

Step 1: [2, 3]
        Sum = 5 ✓✓

Step 2: [2, 3, -8]
        Sum = -3 ✗ (Reset!)

Step 3:         [7]
                Sum = 7 ✓✓✓

Step 4:         [7, -1]
                Sum = 6 ✓✓

Step 5:         [7, -1, 2]
                Sum = 8 ✓✓✓✓

Step 6:         [7, -1, 2, 3]
                Sum = 11 ✓✓✓✓✓ (MAXIMUM!)
```

### Graph Visualization
```
currSum over iterations:

 11│                           ●
 10│
  9│
  8│                      ●
  7│              ●
  6│                 ●
  5│    ●
  4│
  3│
  2│ ●
  1│
  0├─●──────────────●──────────────→
 -1│
 -2│
 -3│         ● (reset to 0)
 -4│
    0  1  2  3  4  5  6  Iteration

Maximum at iteration 6 = 11
```

### Decision Tree
```
At each position, we decide:

[2] → currSum = 2 (positive, keep)
  ↓
[2, 3] → currSum = 5 (positive, keep)
  ↓
[2, 3, -8] → currSum = -3 (negative, RESET!)
  ↓
[7] → currSum = 7 (start fresh)
  ↓
[7, -1] → currSum = 6 (still positive, keep)
  ↓
[7, -1, 2] → currSum = 8 (growing, keep)
  ↓
[7, -1, 2, 3] → currSum = 11 (best!)
```

---

## 🔢 Another Detailed Example

### Input Array
```
arr = [-3, 4, -1, 2, 1, -5, 4]
```

### Execution Steps

| i | arr[i] | currSum (before) | currSum (after) | maxSum | Reset? | Explanation |
|---|--------|------------------|-----------------|--------|--------|-------------|
| 0 | -3 | 0 | -3 | -3 | ✅ → 0 | Negative, reset |
| 1 | 4 | 0 | 4 | 4 | ❌ | New start |
| 2 | -1 | 4 | 3 | 4 | ❌ | Still positive |
| 3 | 2 | 3 | 5 | 5 | ❌ | Growing |
| 4 | 1 | 5 | 6 | **6** | ❌ | Best! |
| 5 | -5 | 6 | 1 | 6 | ❌ | Still positive |
| 6 | 4 | 1 | 5 | 6 | ❌ | Not better |

**Result:** maxSum = 6 (subarray [4, -1, 2, 1])

---

## 🎯 Key Takeaways

### Core Concepts

1. **Kadane's Algorithm**: Optimal solution for maximum subarray sum
2. **Greedy Choice**: At each step, extend or restart subarray
3. **Reset on Negative**: Negative sum won't help future elements
4. **Track Maximum**: Always keep the best sum found
5. **Single Pass**: O(n) time with no extra space

### Memory Trick

> **"Add to current, update max, reset if negative - that's Kadane!"**

### Algorithm Pattern
```
Pattern: Running Sum with Reset
Common in: Maximum subarray, best time problems, cumulative sums

Template:
1. Initialize current and maximum trackers
2. For each element:
   - Update current tracker
   - Update maximum if better
   - Reset current if becomes unfavorable
3. Return maximum
```

### When to Use This Approach

- ✅ Finding maximum/minimum of contiguous subarrays
- ✅ Problems involving running sums
- ✅ Optimization problems with sequential data
- ✅ When greedy choice leads to optimal solution

---

## ⚠️ Common Mistakes

### Mistake 1: Initializing maxSum to 0
```python
# ❌ Wrong - Fails for all negative arrays
def maxSubarraySum(arr):
    currSum = 0
    maxSum = 0  # Wrong initialization!
    
    for num in arr:
        currSum += num
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    return maxSum

# Problem: arr = [-2, -4]
# Result: 0 (Wrong! Should be -2)
```

**Correct:**
```python
# ✅ Correct - Use negative infinity
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')  # Handles all negative arrays
    
    for num in arr:
        currSum += num
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    return maxSum
```

---

### Mistake 2: Resetting Before Updating maxSum
```python
# ❌ Wrong - Order of operations matters!
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')
    
    for num in arr:
        currSum += num
        
        if currSum < 0:  # Reset BEFORE updating max
            currSum = 0
        
        maxSum = max(currSum, maxSum)  # Might miss the peak!
    
    return maxSum

# Problem: arr = [5, -10, 3]
# At i=0: currSum=5, but if we reset before max,
# we lose the value!
```

**Correct:**
```python
# ✅ Correct - Update max BEFORE reset
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')
    
    for num in arr:
        currSum += num
        maxSum = max(currSum, maxSum)  # Update first!
        
        if currSum < 0:
            currSum = 0  # Then reset
    
    return maxSum
```

---

### Mistake 3: Not Handling Single Negative Element
```python
# ❌ Wrong - Doesn't work for single negative
def maxSubarraySum(arr):
    if not arr:
        return 0
    
    currSum = 0
    maxSum = 0  # Problem here!
    
    for num in arr:
        currSum = max(0, currSum + num)
        maxSum = max(maxSum, currSum)
    
    return maxSum

# Problem: arr = [-5]
# Result: 0 (Wrong! Should be -5)
# Must include at least one element!
```

**Correct:**
```python
# ✅ Correct - Initialize to -infinity
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')
    
    for num in arr:
        currSum += num
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    
    return maxSum
```

---

### Mistake 4: Using Wrong Loop Variable
```python
# ❌ Wrong - Using index instead of value
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')
    
    for i in range(len(arr)):
        currSum += i  # Bug! Should be arr[i]
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    
    return maxSum

# Adds indices (0, 1, 2...) instead of values!
```

**Correct:**
```python
# ✅ Correct - Use arr[i] or iterate values
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')
    
    for num in arr:  # Or use arr[i]
        currSum += num
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    
    return maxSum
```

---

### Mistake 5: Brute Force Approach
```python
# ❌ Wrong - O(n²) or O(n³) time complexity
def maxSubarraySum(arr):
    maxSum = float('-inf')
    
    # Check all possible subarrays
    for i in range(len(arr)):
        currSum = 0
        for j in range(i, len(arr)):
            currSum += arr[j]
            maxSum = max(maxSum, currSum)
    
    return maxSum

# Works but O(n²) - too slow for large inputs!
```

**Correct:**
```python
# ✅ Correct - O(n) Kadane's algorithm
def maxSubarraySum(arr):
    currSum = 0
    maxSum = float('-inf')
    
    for num in arr:
        currSum += num
        maxSum = max(currSum, maxSum)
        if currSum < 0:
            currSum = 0
    
    return maxSum
```

---

## 🔗 Practice Problems

### Similar Problems on LeetCode

- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Exact same problem
- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)
- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)
- [1186. Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)

### GeeksforGeeks Problems

- [Largest Sum Contiguous Subarray](https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/)
- [Maximum Subarray Sum Excluding Certain Elements](https://www.geeksforgeeks.org/maximum-subarray-sum-excluding-certain-elements/)
- [Maximum Sum Subarray of size K](https://www.geeksforgeeks.org/find-maximum-minimum-sum-subarray-size-k/)

### Variations to Try

#### 1. Return the Subarray Indices
```python
def maxSubarrayWithIndices(arr):
    """
    Return (maxSum, start_index, end_index)
    """
    currSum = 0
    maxSum = float('-inf')
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(len(arr)):
        currSum += arr[i]
        
        if currSum > maxSum:
            maxSum = currSum
            start = temp_start
            end = i
        
        if currSum < 0:
            currSum = 0
            temp_start = i + 1
    
    return maxSum, start, end
```

#### 2. Maximum Product Subarray
```python
def maxProduct(arr):
    """
    Find maximum product instead of sum
    """
    max_prod = arr[0]
    min_prod = arr[0]
    result = arr[0]
    
    for i in range(1, len(arr)):
        temp = max_prod
        max_prod = max(arr[i], max_prod * arr[i], min_prod * arr[i])
        min_prod = min(arr[i], temp * arr[i], min_prod * arr[i])
        result = max(result, max_prod)
    
    return result
```

#### 3. Maximum Circular Subarray Sum
```python
def maxCircularSum(arr):
    """
    Array is circular (last element connects to first)
    """
    # Case 1: Maximum subarray is not circular
    max_kadane = kadane(arr)
    
    # Case 2: Maximum subarray is circular
    # Total sum - minimum subarray
    total_sum = sum(arr)
    
    # Invert array to find minimum subarray
    inverted = [-x for x in arr]
    max_inverted = kadane(inverted)
    min_subarray = -max_inverted
    
    max_circular = total_sum - min_subarray
    
    # Handle all negative case
    if max_circular == 0:
        return max_kadane
    
    return max(max_kadane, max_circular)
```

---

## 📝 Interview Tips

### What Interviewers Look For

1. ✅ **Understanding of Kadane's algorithm**
2. ✅ **Optimal O(n) solution**
3. ✅ **Handling all negative arrays**
4. ✅ **Clean implementation**
5. ✅ **Explaining the greedy choice**

### Common Interview Questions

**Q: Why is this called Kadane's Algorithm?**
```
A: Named after Jay Kadane, who discovered this elegant
solution in 1984. It's a classic example of dynamic
programming and greedy approach combined.
```

**Q: What if all numbers are negative?**
```
A: We must include at least one element, so we choose
the least negative number. This is why we initialize
maxSum to negative infinity, not 0.
```

**Q: Can you prove this algorithm is correct?**
```
A: At each position, we decide: extend current subarray
or start fresh. If currSum is negative, adding it
to any future element only decreases the sum, so
starting fresh is always better. This greedy choice
leads to the optimal solution.
```

**Q: What's the difference between this and DP approach?**
```
A: Kadane's is essentially DP with space optimization.
DP version: dp[i] = max(arr[i], dp[i-1] + arr[i])
Kadane's: currSum = arr[i] if currSum < 0 else currSum + arr[i]
Same logic, O(1) space instead of O(n).
```

**Q: Can you modify it to return the actual subarray?**
```python
# Yes, track start and end indices:
def maxSubarrayWithIndices(arr):
    currSum = 0
    maxSum = float('-inf')
    start = end = 0
    temp_start = 0
    
    for i, num in enumerate(arr):
        currSum += num
        
        if currSum > maxSum:
            maxSum = currSum
            start = temp_start
            end = i
        
        if currSum < 0:
            currSum = 0
            temp_start = i + 1
    
    return arr[start:end+1], maxSum
```

---

## 🎉 Congratulations!

You now completely understand **Kadane's Algorithm** for the maximum subarray problem!

**Remember**: 
> "Add, update max, reset if negative - the rhythm of Kadane!" 🎵

---

## 📄 License

This documentation is free to use for educational purposes.

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Algorithm Difficulty**: Medium ⭐⭐  
**Topics**: Arrays, Dynamic Programming, Greedy, Kadane's Algorithm  
**Companies**: Google, Amazon, Microsoft, Facebook, Apple, Bloomberg, Adobe

---

**Famous Quote**:
> "This problem is a classic example of how a clever algorithm can reduce complexity from O(n²) or O(n³) to O(n). Kadane's algorithm is a must-know for any software engineer." - *Programming Interview Experts*
