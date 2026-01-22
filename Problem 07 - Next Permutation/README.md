# Next Permutation - Algorithm Documentation

A comprehensive guide to understanding and implementing the **Next Permutation** algorithm with detailed explanations, dry runs, and visual examples.

## 📋 Table of Contents

- [Problem Statement](#problem-statement)
- [Examples](#examples)
- [Constraints](#constraints)
- [Approach](#approach)
- [Algorithm](#algorithm)
- [Implementation](#implementation)
- [Complexity Analysis](#complexity-analysis)
- [Detailed Dry Run](#detailed-dry-run)
- [Visual Representation](#visual-representation)
- [Key Takeaways](#key-takeaways)
- [Common Mistakes](#common-mistakes)
- [Practice Problems](#practice-problems)
- [Edge Cases](#edge-cases-to-consider)
- [Additional Resources](#additional-resources)
- [Quick Reference Card](#quick-reference-card)
- [Interview Tips](#interview-tips)

---

## 🎯 Problem Statement

Given an array of integers `arr[]` representing a permutation, rearrange the numbers into the **lexicographically next greater permutation**. If no such permutation exists (the array is in descending order), rearrange it into the **lowest possible order** (ascending order).

### Requirements

✅ Find next lexicographically greater permutation  
✅ If not possible, return smallest permutation (sorted ascending)  
✅ Modify array in-place  
✅ O(n) time complexity  
✅ O(1) space complexity  

### What is Lexicographical Order?

Lexicographical order is like dictionary order:
- `[1, 2, 3]` comes before `[1, 3, 2]`
- `[2, 1, 3]` comes before `[2, 3, 1]`
- `[3, 2, 1]` is the last permutation of `[1, 2, 3]`

---

## 💡 Examples

### Example 1: Standard Case
```
Input:  arr = [2, 4, 1, 7, 5, 0]
Output: [2, 4, 5, 0, 1, 7]

Explanation: 
Step 1: Find pivot (1) - first decreasing element from right
        [2, 4, 1, 7, 5, 0]
              ↑
Step 2: Find successor (5) - smallest element > 1 on right
        [2, 4, 1, 7, 5, 0]
                    ↑
Step 3: Swap pivot and successor
        [2, 4, 5, 7, 1, 0]
              ↑     ↑
Step 4: Reverse suffix after position i
        [2, 4, 5, 0, 1, 7]
                 --------
                 reversed
```

### Example 2: Last Permutation
```
Input:  arr = [3, 2, 1]
Output: [1, 2, 3]

Explanation: 
Array is in descending order (last permutation)
No next greater permutation exists
Return smallest permutation (ascending order)

[3, 2, 1] → Reverse entire array → [1, 2, 3]
```

### Example 3: Multiple Changes
```
Input:  arr = [3, 4, 2, 5, 1]
Output: [3, 4, 5, 1, 2]

Explanation:
Step 1: Pivot at index 2 (value 2)
        [3, 4, 2, 5, 1]
              ↑
Step 2: Successor at index 3 (value 5)
        [3, 4, 2, 5, 1]
                  ↑
Step 3: Swap
        [3, 4, 5, 2, 1]
Step 4: Reverse from index 3 onwards
        [3, 4, 5, 1, 2]
```

### Example 4: Already Sorted
```
Input:  arr = [1, 2, 3]
Output: [1, 3, 2]

Explanation:
Pivot at index 1 (value 2)
Successor at index 2 (value 3)
Swap and reverse: [1, 3, 2]
```

### Example 5: Single Element
```
Input:  arr = [5]
Output: [5]

Explanation:
Only one permutation exists
Return as is
```

---

## 🚫 Constraints

- `1 <= arr.size() <= 10^5`
- `0 <= arr[i] <= 10^5`
- Array can have duplicate elements
- Modify array in-place

---

## 🧠 Approach

### Three-Step Algorithm

The next permutation algorithm follows three key steps:
```
1. Find the PIVOT
   - Rightmost position where arr[i] < arr[i+1]
   - This is the position we need to increase

2. Find the SUCCESSOR
   - Smallest element greater than pivot (from right)
   - This will replace the pivot

3. REVERSE the suffix
   - Reverse everything after pivot position
   - Makes the suffix smallest possible
```

### Why This Works

**Key Insight**: To get the next permutation:
1. We need to increase the number as little as possible
2. We should change the rightmost digit that can be increased
3. After swapping, make the rest as small as possible

### Visual Understanding
```
Original: [2, 4, 1, 7, 5, 0]
              ↑
          Find this: Last position where increase is possible
          (1 < 7, so we can increase from here)

Next:     [2, 4, 5, 0, 1, 7]
              ↑
          Replace 1 with next greater (5)
          Then make rest smallest (reverse [7,1,0] → [0,1,7])
```

---

## 📝 Algorithm

### Detailed Steps
```
Step 1: Find Pivot (rightmost i where arr[i] < arr[i+1])
   - Start from second last element (i = n-2)
   - Move left while arr[i] >= arr[i+1]
   - If i < 0: entire array is descending → reverse and return

Step 2: Find Successor (smallest element > arr[i] from right)
   - Start from last element (j = n-1)
   - Move left while arr[j] <= arr[i]
   - arr[j] is the successor

Step 3: Swap pivot and successor
   - Swap arr[i] and arr[j]

Step 4: Reverse suffix (from i+1 to end)
   - Reverse arr[i+1:] to get smallest arrangement
   
Step 5: Return modified array
```

---

## 💻 Implementation

### Python (Given Solution)
```python
class Solution:
    def nextPermutation(self, arr):
        """
        Find next lexicographically greater permutation
        
        Args:
            arr: List of integers
            
        Returns:
            Next permutation (modifies in-place)
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        
        # Step 1: Find pivot (rightmost i where arr[i] < arr[i+1])
        i = n - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        
        # If no pivot found, array is in descending order
        if i < 0:
            arr.reverse()
            return arr
        
        # Step 2: Find successor (smallest element > arr[i] from right)
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        
        # Step 3: Swap pivot and successor
        arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse suffix to get smallest arrangement
        arr[i+1:] = reversed(arr[i+1:])
        
        return arr
```

### Python (Alternative with Manual Reverse)
```python
class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        
        # Find pivot
        i = n - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        
        if i < 0:
            arr.reverse()
            return arr
        
        # Find successor
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        
        # Swap
        arr[i], arr[j] = arr[j], arr[i]
        
        # Manual reverse using two pointers
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
```

---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**
```
Step 1: Find pivot - O(n) worst case
Step 2: Find successor - O(n) worst case
Step 3: Swap - O(1)
Step 4: Reverse suffix - O(n) worst case

Total: O(n) + O(n) + O(1) + O(n) = O(n)
```

**Detailed Breakdown:**
- Finding pivot: Scan from right, worst case entire array = O(n)
- Finding successor: Scan from right, worst case n elements = O(n)
- Reversing suffix: At most n elements = O(n)
- All linear operations = O(n)

### Space Complexity: **O(1)**
```
Variables used:
- n: array length (constant)
- i: pivot index (constant)
- j: successor index (constant)

No extra arrays or data structures
In-place modification

Total: O(1) constant space
```

### Comparison with Alternative Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| **Our Algorithm** ⭐ | O(n) | O(1) | Optimal |
| Generate all permutations | O(n! × n) | O(n!) | Extremely slow |
| STL next_permutation | O(n) | O(1) | Same algorithm |
| Recursive | O(n) | O(n) | Call stack |

---

## 🔍 Detailed Dry Run

### Input Array
```
arr = [2, 4, 1, 7, 5, 0]
```

### Initial State
```
n = 6
i = n - 2 = 4
```

---

## 🎬 Step-by-Step Execution

### **Step 1: Find Pivot**

Looking for rightmost position where `arr[i] < arr[i+1]`

#### **Iteration 1: i = 4**
```
Array: [2, 4, 1, 7, 5, 0]
Index:  0  1  2  3  4  5
                    ↑
                   i=4

Check: arr[4] >= arr[5]?
       5 >= 0 → True ✅
       
Action: Move left (i--)
        i = 3
```

#### **Iteration 2: i = 3**
```
Array: [2, 4, 1, 7, 5, 0]
Index:  0  1  2  3  4  5
                 ↑
                i=3

Check: arr[3] >= arr[4]?
       7 >= 5 → True ✅
       
Action: Move left (i--)
        i = 2
```

#### **Iteration 3: i = 2**
```
Array: [2, 4, 1, 7, 5, 0]
Index:  0  1  2  3  4  5
              ↑
             i=2

Check: arr[2] >= arr[3]?
       1 >= 7 → False ❌
       
Action: FOUND PIVOT!
        i = 2 (pivot index)
        arr[i] = 1 (pivot value)
```

**After Step 1:**
```
Pivot found at index 2
arr[2] = 1

Array: [2, 4, 1, 7, 5, 0]
              ↑
            Pivot
```

---

### **Step 2: Check if Last Permutation**
```
if i < 0:  → 2 < 0 → False ❌
Skip reverse, continue to find successor
```

---

### **Step 3: Find Successor**

Looking for smallest element greater than `arr[i]` from right
```
j = n - 1 = 5
arr[i] = 1 (need to find element > 1)
```

#### **Iteration 1: j = 5**
```
Array: [2, 4, 1, 7, 5, 0]
Index:  0  1  2  3  4  5
              ↑         ↑
              i         j

Check: arr[5] <= arr[2]?
       0 <= 1 → True ✅
       
Action: Move left (j--)
        j = 4
```

#### **Iteration 2: j = 4**
```
Array: [2, 4, 1, 7, 5, 0]
Index:  0  1  2  3  4  5
              ↑      ↑
              i      j

Check: arr[4] <= arr[2]?
       5 <= 1 → False ❌
       
Action: FOUND SUCCESSOR!
        j = 4 (successor index)
        arr[j] = 5 (successor value)
```

**After Step 3:**
```
Successor found at index 4
arr[4] = 5

Array: [2, 4, 1, 7, 5, 0]
              ↑      ↑
            Pivot  Successor
```

---

### **Step 4: Swap Pivot and Successor**
```
Swap arr[i] and arr[j]
Swap arr[2] and arr[4]
Swap 1 and 5

Before: [2, 4, 1, 7, 5, 0]
              ↑      ↑
              
After:  [2, 4, 5, 7, 1, 0]
              ↑      ↑
           Swapped!
```

---

### **Step 5: Reverse Suffix**

Reverse from index `i+1` to end
```
i + 1 = 3
Reverse arr[3:] = [7, 1, 0]

Before: [2, 4, 5, 7, 1, 0]
                 ---------
                 suffix

After:  [2, 4, 5, 0, 1, 7]
                 ---------
                 reversed
```

**Reverse Process:**
```
Suffix: [7, 1, 0]
         ↑     ↑
         swap

Step 1: [0, 1, 7]
            ↑
        (middle, stop)

Result: [0, 1, 7]
```

---

### Final Result
```
arr = [2, 4, 5, 0, 1, 7]
```

✅ **Next Permutation Found!**

---

## 📊 Detailed Step Table

| Step | Operation | i | j | Array State | Description |
|------|-----------|---|---|-------------|-------------|
| 0 | Initial | 4 | - | [2,4,1,7,5,0] | Start from i=n-2 |
| 1 | Find pivot | 4→2 | - | [2,4,1,7,5,0] | Scan left for arr[i]<arr[i+1] |
| 2 | Check i<0 | 2 | - | [2,4,1,7,5,0] | Pivot found, continue |
| 3 | Find successor | 2 | 5→4 | [2,4,1,7,5,0] | Scan left for arr[j]>arr[i] |
| 4 | Swap | 2 | 4 | [2,4,5,7,1,0] | Swap arr[2] and arr[4] |
| 5 | Reverse suffix | 2 | - | [2,4,5,0,1,7] | Reverse arr[3:] |

---

## 🎨 Visual Representation

### Complete Transformation
```
Step 0: Initial Array
┌───┬───┬───┬───┬───┬───┐
│ 2 │ 4 │ 1 │ 7 │ 5 │ 0 │
└───┴───┴───┴───┴───┴───┘

Step 1: Find Pivot (scan from right)
┌───┬───┬───┬───┬───┬───┐
│ 2 │ 4 │ 1 │ 7 │ 5 │ 0 │
└───┴───┴───┴───┴───┴───┘
          ↑
        Pivot (1 < 7)

Step 2: Find Successor (scan from right)
┌───┬───┬───┬───┬───┬───┐
│ 2 │ 4 │ 1 │ 7 │ 5 │ 0 │
└───┴───┴───┴───┴───┴───┘
          ↑       ↑
        Pivot  Successor (5 > 1)

Step 3: Swap Pivot and Successor
┌───┬───┬───┬───┬───┬───┐
│ 2 │ 4 │ 5 │ 7 │ 1 │ 0 │
└───┴───┴───┴───┴───┴───┘
          ↑       ↑
         Swapped

Step 4: Reverse Suffix (from i+1 to end)
┌───┬───┬───┬───┬───┬───┐
│ 2 │ 4 │ 5 │ 0 │ 1 │ 7 │
└───┴───┴───┴───┴───┴───┘
              -----------
              Reversed!

Result: [2, 4, 5, 0, 1, 7] ✅
```

### Why Reverse the Suffix?
```
After swap: [2, 4, 5, 7, 1, 0]
                     ---------
                     suffix is in descending order

We want the NEXT permutation (smallest increase)
So we need suffix in ASCENDING order

Reverse: [7, 1, 0] → [0, 1, 7]

Final: [2, 4, 5, 0, 1, 7] ✅
```

---

## 🔢 Another Detailed Example

### Input Array
```
arr = [3, 2, 1]
```

### Execution

#### **Step 1: Find Pivot**
```
i = n - 2 = 1

Check i=1: arr[1] >= arr[2]? → 2 >= 1 → True
Move left: i = 0

Check i=0: arr[0] >= arr[1]? → 3 >= 2 → True
Move left: i = -1

Loop ends: i = -1
```

#### **Step 2: Check if Last Permutation**
```
if i < 0:  → -1 < 0 → True ✅

This is the LAST permutation!
Reverse entire array
```

#### **Step 3: Reverse**
```
Before: [3, 2, 1]
After:  [1, 2, 3]
```

### Final Result
```
arr = [1, 2, 3]
```

✅ **Wrapped around to first permutation!**

---

## 🎯 Key Takeaways

### Core Concepts

1. **Lexicographical Order**: Dictionary-like ordering of permutations
2. **Pivot**: Rightmost position where we can increase the value
3. **Successor**: Smallest value greater than pivot (from right)
4. **Reverse Suffix**: Makes remaining part smallest possible
5. **Edge Case**: Descending order = last permutation → reverse all

### Memory Trick

> **"Find pivot, find successor, swap, reverse suffix - that's the next permutation!"**

### Algorithm Pattern
```
Pattern: In-place Array Manipulation
Common in: Permutations, combinations, array rearrangement

Key Steps:
1. Find critical position (pivot)
2. Find replacement value (successor)
3. Perform swap
4. Optimize remaining part (reverse)
```

### When to Use This Approach

- ✅ Need next/previous permutation
- ✅ Lexicographical ordering required
- ✅ In-place modification needed
- ✅ Optimal time complexity required

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Pivot Condition
```python
# ❌ Wrong - Using > instead of >=
while i >= 0 and arr[i] > arr[i+1]:  # Wrong!
    i -= 1

# Problem: Misses cases with equal elements
# Example: [1, 5, 1] would fail

# ✅ Correct - Use >=
while i >= 0 and arr[i] >= arr[i+1]:
    i -= 1
```

---

### Mistake 2: Not Checking i < 0
```python
# ❌ Wrong - Forgetting last permutation case
def nextPermutation(arr):
    i = n - 2
    while i >= 0 and arr[i] >= arr[i+1]:
        i -= 1
    
    # Missing check for i < 0!
    j = n - 1
    while arr[j] <= arr[i]:  # Index error if i = -1!
        j -= 1

# ✅ Correct - Check for last permutation
if i < 0:
    arr.reverse()
    return arr
```

---

### Mistake 3: Wrong Successor Condition
```python
# ❌ Wrong - Using < instead of <=
while arr[j] < arr[i]:  # Wrong!
    j -= 1

# Problem: Might pick wrong successor
# Example: [1, 3, 2] → would pick 3 instead of 2

# ✅ Correct - Use <=
while arr[j] <= arr[i]:
    j -= 1
```

---

### Mistake 4: Not Reversing Suffix
```python
# ❌ Wrong - Just swapping without reversing
arr[i], arr[j] = arr[j], arr[i]
return arr  # Missing reverse!

# Problem: Doesn't give NEXT permutation
# Example: [1, 2, 3] → [1, 3, 2] but suffix not reversed

# ✅ Correct - Always reverse suffix
arr[i], arr[j] = arr[j], arr[i]
arr[i+1:] = reversed(arr[i+1:])
```

---

### Mistake 5: Reversing Wrong Range
```python
# ❌ Wrong - Reversing from wrong index
arr[i:] = reversed(arr[i:])  # Wrong! Should be i+1

# Problem: Includes swapped element in reverse
# Example: Changes the pivot position value

# ✅ Correct - Reverse from i+1
arr[i+1:] = reversed(arr[i+1:])
```

---

## 🔗 Practice Problems

### Similar Problems on LeetCode

- [31. Next Permutation](https://leetcode.com/problems/next-permutation/) - Exact same problem
- [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/)
- [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)
- [46. Permutations](https://leetcode.com/problems/permutations/)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
- [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

### GeeksforGeeks Problems

- [Next Permutation](https://www.geeksforgeeks.org/next-permutation/)
- [Previous Permutation](https://www.geeksforgeeks.org/find-previous-permutation-of-a-number/)
- [Lexicographically next string](https://www.geeksforgeeks.org/lexicographically-next-string/)
- [Find nth permutation](https://www.geeksforgeeks.org/find-n-th-permutation/)

### Variations to Try

#### 1. Previous Permutation
```python
def previousPermutation(arr):
    """
    Find lexicographically previous permutation
    """
    n = len(arr)
    
    # Find pivot (rightmost i where arr[i] > arr[i+1])
    i = n - 2
    while i >= 0 and arr[i] <= arr[i+1]:  # Note: <= instead of >=
        i -= 1
    
    if i < 0:
        arr.reverse()
        return arr
    
    # Find successor (largest element < arr[i] from right)
    j = n - 1
    while arr[j] >= arr[i]:  # Note: >= instead of <=
        j -= 1
    
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    
    return arr
```

#### 2. kth Permutation
```python
def kthPermutation(n, k):
    """
    Find kth permutation of numbers 1 to n
    """
    import math
    
    numbers = list(range(1, n + 1))
    result = []
    k -= 1  # Convert to 0-indexed
    
    for i in range(n, 0, -1):
        factorial = math.factorial(i - 1)
        index = k // factorial
        result.append(numbers[index])
        numbers.pop(index)
        k %= factorial
    
    return result
```

#### 3. All Permutations
```python
def allPermutations(arr):
    """
    Generate all permutations using next permutation
    """
    arr.sort()  # Start with smallest
    result = [arr.copy()]
    
    while True:
        arr = nextPermutation(arr)
        if arr <= result[0]:  # Wrapped around
            break
        result.append(arr.copy())
    
    return result
```

---



---

## 📝 Interview Tips

### What Interviewers Look For

1. ✅ **Understanding of lexicographical order**
2. ✅ **Optimal O(n) solution**
3. ✅ **Handling edge cases (last permutation)**
4. ✅ **In-place modification**
5. ✅ **Clear explanation of algorithm steps**

### Common Interview Questions

```
**Q: Why do we reverse the suffix?**
A: After swapping, the suffix is in descending order.
To get the NEXT permutation (smallest increase),
we need the suffix in ascending order. Reversing
a descending sequence gives ascending order.

```

```
**Q: What if the array is in descending order?**
A: It's the last permutation. No greater permutation
exists, so we return the first permutation by
reversing the entire array (ascending order).
```

```
**Q: Can you explain the time complexity?**
A: We make at most 3 passes through the array:

Find pivot: O(n)
Find successor: O(n)
Reverse suffix: O(n)
Total: O(n) - linear time
```

```

**Q: Why scan from right to left?**
A: We want the SMALLEST increase. This means changing
the RIGHTMOST position possible. Scanning from
right ensures we find the rightmost pivot.

```
```
**Q: How would you find the previous permutation?**
A: Similar algorithm, but reversed conditions:

Pivot: rightmost i where arr[i] > arr[i+1]
Successor: largest element < arr[i] from right
Then swap and reverse suffix
```
```
**Q: What about duplicates?**
A: The algorithm handles duplicates correctly.
Using >= (not >) in pivot search ensures we find
the right position even with duplicate values.
```
---

## 🎉 Congratulations!

You now completely understand the **Next Permutation** algorithm!

**Remember**: 
> "Pivot, Successor, Swap, Reverse - the four steps to next permutation perfection!" 🔄✨

---

## 📄 License

This documentation is free to use for educational purposes.

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Algorithm Difficulty**: Medium ⭐⭐  
**Topics**: Arrays, Permutations, In-place Algorithms, Lexicographical Order  
**Companies**: Google, Facebook, Amazon, Microsoft, Apple, Bloomberg

---

**Famous Applications**:
- **Combinatorics**: Generating all permutations
- **Cryptography**: Permutation-based ciphers
- **Optimization**: Branch and bound algorithms
- **Gaming**: Puzzle solving (Rubik's cube, etc.)
