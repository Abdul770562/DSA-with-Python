# Rotate Array - Algorithm Documentation

A comprehensive guide to understanding and implementing the "Rotate Array by D positions" algorithm using the **Reversal Algorithm** with detailed explanations, dry runs, and visual examples.

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

Given an array of integers and a number `d`, rotate the array by `d` positions in **counter-clockwise (left) direction**. The rotation should be performed **in-place** without using extra space.

### Requirements

✅ Rotate array by d positions to the left  
✅ In-place modification (no extra array)  
✅ O(n) time complexity  
✅ O(1) space complexity  
✅ Handle cases where d > n  

---

## 💡 Examples

### Example 1: Basic Rotation
```
Input:  arr = [1, 2, 3, 4, 5], d = 2
Output: [3, 4, 5, 1, 2]

Explanation: 
- Rotate left by 2 positions
- First 2 elements [1, 2] move to end
- Remaining elements [3, 4, 5] shift to front
```

### Example 2: Single Position
```
Input:  arr = [10, 20, 30, 40, 50], d = 1
Output: [20, 30, 40, 50, 10]

Explanation: Rotate left by 1 position
```

### Example 3: d Greater Than n
```
Input:  arr = [1, 2, 3, 4, 5], d = 7
Output: [3, 4, 5, 1, 2]

Explanation: 
- d = 7, n = 5
- Effective rotation = d % n = 7 % 5 = 2
- Same as rotating by 2 positions
```

### Example 4: d Equals n
```
Input:  arr = [1, 2, 3, 4], d = 4
Output: [1, 2, 3, 4]

Explanation: 
- d = 4, n = 4
- Effective rotation = d % n = 4 % 4 = 0
- Array remains unchanged
```

### Example 5: No Rotation
```
Input:  arr = [5, 10, 15, 20], d = 0
Output: [5, 10, 15, 20]

Explanation: No rotation needed
```

---

## 🚫 Constraints

- Array can contain any integers
- No extra array allowed (in-place operation)
- d can be greater than array length
- Array length: 1 ≤ n ≤ 10^6
- Rotation positions: 0 ≤ d ≤ 10^9

---

## 🧠 Approach

### Reversal Algorithm (Juggling Algorithm)

This is the **most optimal approach** using three reversals:
```
To rotate array left by d positions:
1. Reverse first d elements
2. Reverse remaining n-d elements
3. Reverse entire array
```

### Why This Works - The Magic! ✨

Let's understand with example: `[1, 2, 3, 4, 5]`, d = 2
```
Original:        [1, 2 | 3, 4, 5]
                  -----   ---------
                  Part A   Part B

Goal:            [3, 4, 5, 1, 2]
                 (Part B first, then Part A)

Step 1: Reverse Part A (first d elements)
        [2, 1 | 3, 4, 5]

Step 2: Reverse Part B (remaining elements)
        [2, 1 | 5, 4, 3]

Step 3: Reverse entire array
        [3, 4, 5, 1, 2] ✅
```

### Key Insight

- Reversing twice = Original position swap
- Three strategic reversals = Perfect rotation!

---

## 📝 Algorithm

### Step-by-Step Process
```
1. Calculate effective rotation: d = d % n
   (Handles d > n case)

2. Define helper function reverse(i, j):
   - Reverse array from index i to j
   - Use two-pointer technique

3. Apply three reversals:
   - Reverse(0, d-1)      → Reverse first d elements
   - Reverse(d, n-1)      → Reverse remaining elements
   - Reverse(0, n-1)      → Reverse entire array

4. Array is now rotated!
```

### Pseudocode
```
function rotateArr(arr, d):
    n = length of arr
    d = d % n  // Handle d > n
    
    // Helper function to reverse
    function reverse(i, j):
        while i < j:
            swap arr[i] and arr[j]
            i = i + 1
            j = j - 1
    
    // Three reversals
    reverse(0, d-1)        // Reverse first part
    reverse(d, n-1)        // Reverse second part
    reverse(0, n-1)        // Reverse whole array
```

---

## 💻 Implementation

### Python
```python
class Solution:
    def rotateArr(self, arr, d):
        """
        Rotate array by d positions counter-clockwise using reversal algorithm
        
        Args:
            arr: List of integers
            d: Number of positions to rotate
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        
        # Handle case where d > n
        # Also handles d = n (no rotation) and d = 0
        d = d % n
        
        # Helper function to reverse array from index i to j
        def reverse(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        # Three strategic reversals
        reverse(0, d - 1)      # Reverse first d elements
        reverse(d, n - 1)      # Reverse remaining elements
        reverse(0, n - 1)      # Reverse entire array
```

---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**
```
Three reversal operations:
1. Reverse first d elements:     O(d)
2. Reverse remaining elements:    O(n-d)
3. Reverse entire array:          O(n)

Total = O(d) + O(n-d) + O(n)
      = O(n) + O(n)
      = O(2n)
      = O(n)
```

### Space Complexity: **O(1)**

- Only uses variables: `n`, `d`, `i`, `j`
- No extra array or data structure
- In-place modification using reversal

### Comparison with Alternative Approaches

| Approach | Time | Space | In-Place | Complexity |
|----------|------|-------|----------|------------|
| **Reversal Algorithm** ⭐ | O(n) | O(1) | ✅ Yes | Simple |
| Using Temp Array | O(n) | O(n) | ❌ No | Very Simple |
| One by One Rotation | O(n×d) | O(1) | ✅ Yes | Inefficient |
| Juggling Algorithm | O(n) | O(1) | ✅ Yes | Complex |
| Using Deque | O(n) | O(n) | ❌ No | Simple |

**Why Reversal Algorithm is Best:**
- ✅ Optimal time: O(n)
- ✅ Optimal space: O(1)
- ✅ Easy to understand
- ✅ Easy to implement
- ✅ No complex mathematics

---

## 🔍 Detailed Dry Run

### Input Array
```
arr = [1, 2, 3, 4, 5]
d = 2
```

### Initial State
```
n = 5
d = 2
d % n = 2 % 5 = 2 (no change needed)
```

---

## 🎬 Step-by-Step Execution

### **Step 0: Initial Array**
```
Array: [1, 2, 3, 4, 5]
        -----  -------
        Part A  Part B
        (d=2)   (n-d=3)

Goal: Move Part A to end → [3, 4, 5, 1, 2]
```

---

### **Step 1: Reverse First d Elements (0 to d-1)**
```
reverse(0, d-1) → reverse(0, 1)
```

#### Execution of reverse(0, 1):

**Before:**
```
Array: [1, 2, 3, 4, 5]
        ↑  ↑
        i  j
       i=0 j=1
```

**Iteration 1:**
```
Condition: i < j → 0 < 1 → True ✅

Swap arr[0] and arr[1]:
arr[0], arr[1] = arr[1], arr[0]
1, 2 = 2, 1

Array: [2, 1, 3, 4, 5]

Update pointers:
i = 1, j = 0

Condition: i < j → 1 < 0 → False ❌
Loop exits
```

**After Step 1:**
```
Array: [2, 1, 3, 4, 5]
        -----
        Reversed!
```

---

### **Step 2: Reverse Remaining Elements (d to n-1)**
```
reverse(d, n-1) → reverse(2, 4)
```

#### Execution of reverse(2, 4):

**Before:**
```
Array: [2, 1, 3, 4, 5]
              ↑     ↑
              i     j
             i=2   j=4
```

**Iteration 1:**
```
Condition: i < j → 2 < 4 → True ✅

Swap arr[2] and arr[4]:
arr[2], arr[4] = arr[4], arr[2]
3, 5 = 5, 3

Array: [2, 1, 5, 4, 3]

Update pointers:
i = 3, j = 3

Condition: i < j → 3 < 3 → False ❌
Loop exits
```

**After Step 2:**
```
Array: [2, 1, 5, 4, 3]
              ---------
              Reversed!
```

---

### **Step 3: Reverse Entire Array (0 to n-1)**
```
reverse(0, n-1) → reverse(0, 4)
```

#### Execution of reverse(0, 4):

**Before:**
```
Array: [2, 1, 5, 4, 3]
        ↑           ↑
        i           j
       i=0         j=4
```

**Iteration 1:**
```
Condition: i < j → 0 < 4 → True ✅

Swap arr[0] and arr[4]:
Array: [3, 1, 5, 4, 2]

Update: i = 1, j = 3
```

**Iteration 2:**
```
Condition: i < j → 1 < 3 → True ✅

Swap arr[1] and arr[3]:
Array: [3, 4, 5, 1, 2]

Update: i = 2, j = 2
```

**Iteration 3:**
```
Condition: i < j → 2 < 2 → False ❌
Loop exits
```

**After Step 3:**
```
Array: [3, 4, 5, 1, 2]
        ---------------
        Fully Reversed!
```

---

### Final Output
```
Array: [3, 4, 5, 1, 2]
```

✅ Array successfully rotated left by 2 positions!

---

## 🎨 Visual Representation

### Complete Transformation
```
Step 0: Initial Array
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  -----   -----------
  Part A    Part B

Step 1: Reverse Part A (first d=2 elements)
┌───┬───┬───┬───┬───┐
│ 2 │ 1 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  -----
  Reversed

Step 2: Reverse Part B (remaining elements)
┌───┬───┬───┬───┬───┐
│ 2 │ 1 │ 5 │ 4 │ 3 │
└───┴───┴───┴───┴───┘
          -----------
          Reversed

Step 3: Reverse Entire Array
┌───┬───┬───┬───┬───┐
│ 3 │ 4 │ 5 │ 1 │ 2 │
└───┴───┴───┴───┴───┘
  ---------------
  Final Result! ✅
```

---

## 🔢 Another Detailed Example

### Input Array
```
arr = [10, 20, 30, 40, 50, 60]
d = 3
```

### Initial State
```
n = 6
d = 3 % 6 = 3
```

---

### Step-by-Step Execution

#### **Step 0: Initial**
```
Array: [10, 20, 30, 40, 50, 60]
        -----------  -----------
         Part A        Part B
         (d=3)        (n-d=3)
```

#### **Step 1: reverse(0, 2)**
```
Before: [10, 20, 30, 40, 50, 60]
         ↑       ↑
         i=0    j=2

Swap 1: [30, 20, 10, 40, 50, 60]
             ↑
           i=1, j=1 (stop)

After:  [30, 20, 10, 40, 50, 60]
```

#### **Step 2: reverse(3, 5)**
```
Before: [30, 20, 10, 40, 50, 60]
                     ↑       ↑
                    i=3     j=5

Swap 1: [30, 20, 10, 60, 50, 40]
                         ↑
                       i=4, j=4 (stop)

After:  [30, 20, 10, 60, 50, 40]
```

#### **Step 3: reverse(0, 5)**
```
Before: [30, 20, 10, 60, 50, 40]
         ↑                   ↑
        i=0                 j=5

Swap 1: [40, 20, 10, 60, 50, 30]
             ↑           ↑
            i=1         j=4

Swap 2: [40, 50, 10, 60, 20, 30]
                 ↑   ↑
                i=2 j=3

Swap 3: [40, 50, 60, 10, 20, 30]
                     ↑
                   i=3, j=2 (stop)

After:  [40, 50, 60, 10, 20, 30]
```

### Final Output
```
[40, 50, 60, 10, 20, 30]
```

✅ Rotated left by 3 positions!

---

## 📊 Detailed Step Table

### For Array: [1, 2, 3, 4, 5], d = 2

| Step | Operation | Range | Array State | Description |
|------|-----------|-------|-------------|-------------|
| 0 | Initial | - | [1, 2, 3, 4, 5] | Original array |
| 1 | reverse(0, 1) | First 2 | [2, 1, 3, 4, 5] | Reverse Part A |
| 2 | reverse(2, 4) | Last 3 | [2, 1, 5, 4, 3] | Reverse Part B |
| 3 | reverse(0, 4) | All | [3, 4, 5, 1, 2] | Reverse entire |
| Final | - | - | [3, 4, 5, 1, 2] | ✅ Rotated! |

---

## 🎯 Why Reversal Algorithm Works - Mathematical Proof

### Concept

For array `A = [a₁, a₂, ..., aₐ, aₐ₊₁, ..., aₙ]` where d elements need to move:
```
Part A: [a₁, a₂, ..., aₐ]
Part B: [aₐ₊₁, aₐ₊₂, ..., aₙ]

Goal: [Part B, Part A]
```

### Reversal Steps

**Step 1: Reverse Part A**
```
[aₐ, aₐ₋₁, ..., a₁] + [aₐ₊₁, ..., aₙ]
```

**Step 2: Reverse Part B**
```
[aₐ, aₐ₋₁, ..., a₁] + [aₙ, aₙ₋₁, ..., aₐ₊₁]
```

**Step 3: Reverse Entire Array**
```
Reverse of: [aₐ, aₐ₋₁, ..., a₁, aₙ, aₙ₋₁, ..., aₐ₊₁]
Result:     [aₐ₊₁, aₐ₊₂, ..., aₙ, a₁, a₂, ..., aₐ]
```

✅ Which is exactly: [Part B, Part A]

---

## 🎯 Key Takeaways

### Core Concepts

1. **Modulo Operation**: `d = d % n` handles all edge cases
2. **Three Reversals**: Strategic reversals achieve rotation
3. **In-Place**: No extra space needed
4. **Optimal**: O(n) time, O(1) space

### Memory Trick

> **"Reverse parts separately, then reverse the whole - rotation complete!"**

### When to Use This Approach

- ✅ Need to rotate array left or right
- ✅ In-place modification required
- ✅ Optimal time and space needed
- ✅ Simple and intuitive solution

### Algorithm Pattern
```
Left Rotation by d:
1. Reverse(0, d-1)
2. Reverse(d, n-1)
3. Reverse(0, n-1)

Right Rotation by d:
1. Reverse(0, n-d-1)
2. Reverse(n-d, n-1)
3. Reverse(0, n-1)
```

---

## ⚠️ Common Mistakes

### Mistake 1: Not Handling d > n
```python
# ❌ Wrong - d can be larger than n
def rotateArr(arr, d):
    n = len(arr)
    # Missing: d = d % n
    reverse(0, d-1)  # Index out of bounds if d > n!
```

**Correct:**
```python
# ✅ Correct - Handle d > n
def rotateArr(arr, d):
    n = len(arr)
    d = d % n  # Essential step!
    # ... rest of code
```

**Why this matters:**
```
arr = [1, 2, 3], d = 7
Without d % n: Try to reverse(0, 6) → Index Error!
With d % n:    d = 7 % 3 = 1 → reverse(0, 0) ✅
```

---

### Mistake 2: Wrong Reversal Order
```python
# ❌ Wrong - Incorrect reversal sequence
reverse(0, n-1)    # Reverse entire first
reverse(0, d-1)    # Then reverse parts
reverse(d, n-1)

# This gives wrong result!
```

**Correct:**
```python
# ✅ Correct - Proper sequence
reverse(0, d-1)    # Reverse first part
reverse(d, n-1)    # Reverse second part
reverse(0, n-1)    # Reverse entire
```

---

### Mistake 3: Off-by-One Errors
```python
# ❌ Wrong - Incorrect indices
reverse(0, d)      # Should be d-1
reverse(d+1, n-1)  # Should be d
reverse(0, n)      # Should be n-1
```

**Correct:**
```python
# ✅ Correct - Proper indices
reverse(0, d-1)    # First d elements
reverse(d, n-1)    # Remaining elements
reverse(0, n-1)    # Entire array
```

---

### Mistake 4: Forgetting Edge Cases
```python
# ❌ Wrong - Doesn't handle special cases
def rotateArr(arr, d):
    # What if d = 0?
    # What if d = n?
    # What if arr is empty?
    reverse(0, d-1)
    reverse(d, n-1)
    reverse(0, n-1)
```

**Correct:**
```python
# ✅ Correct - Handles all cases
def rotateArr(arr, d):
    n = len(arr)
    if n == 0:  # Empty array
        return
    d = d % n   # Handles d=0, d=n, d>n
    if d == 0:  # No rotation needed
        return
    # ... rest of code
```

---

### Mistake 5: Using Extra Space
```python
# ❌ Wrong - Uses extra array
def rotateArr(arr, d):
    n = len(arr)
    temp = arr[:d]           # Extra O(d) space
    arr[:n-d] = arr[d:]
    arr[n-d:] = temp
```

**Correct:**
```python
# ✅ Correct - No extra space
def rotateArr(arr, d):
    n = len(arr)
    d = d % n
    # Use reversal algorithm (O(1) space)
```

---

## 🔗 Practice Problems

### Similar Problems

1. **Rotate Array Right** - Rotate in opposite direction
2. **Rotate String** - Same concept for strings
3. **Cyclic Rotation** - Rotate by 1 position k times
4. **Reverse Array in Groups** - Combine reversal concepts

### LeetCode Problems

- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [796. Rotate String](https://leetcode.com/problems/rotate-string/)
- [61. Rotate List](https://leetcode.com/problems/rotate-list/)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

### Variations to Try

#### 1. Rotate Right by d Positions
```python
def rotateRight(arr, d):
    """Rotate array right by d positions"""
    n = len(arr)
    d = d % n
    
    def reverse(i, j):
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    # For right rotation, adjust the sequence
    reverse(0, n - d - 1)   # Reverse first n-d elements
    reverse(n - d, n - 1)   # Reverse last d elements
    reverse(0, n - 1)       # Reverse entire array
```

#### 2. Check if Array is Rotation of Another
```python
def isRotation(arr1, arr2):
    """Check if arr2 is rotation of arr1"""
    if len(arr1) != len(arr2):
        return False
    
    # Concatenate arr1 with itself
    temp = arr1 + arr1
    
    # Check if arr2 is substring
    return isSubarray(temp, arr2)
```

#### 3. Minimum Rotations to Make Arrays Equal
```python
def minRotations(arr1, arr2):
    """Find minimum rotations to make arrays equal"""
    n = len(arr1)
    for d in range(n):
        # Rotate arr1 by d positions
        if rotateAndCompare(arr1, arr2, d):
            return d
    return -1  # Not possible
```

---

## 🧪 Test Cases
```python
# Test Case 1: Standard rotation
arr1 = [1, 2, 3, 4, 5]
rotateArr(arr1, 2)
assert arr1 == [3, 4, 5, 1, 2]

# Test Case 2: d greater than n
arr2 = [1, 2, 3, 4, 5]
rotateArr(arr2, 7)  # 7 % 5 = 2
assert arr2 == [3, 4, 5, 1, 2]

# Test Case 3: d equals n
arr3 = [1, 2, 3, 4]
rotateArr(arr3, 4)  # 4 % 4 = 0
assert arr3 == [1, 2, 3, 4]

# Test Case 4: d = 0
arr4 = [1, 2, 3]
rotateArr(arr4, 0)
assert arr4 == [1, 2, 3]

# Test Case 5: Single element
arr5 = [42]
rotateArr(arr5, 100)
assert arr5 == [42]

# Test Case 6: Two elements
arr6 = [1, 2]
rotateArr(arr6, 1)
assert arr6 == [2, 1]

# Test Case 7: Rotate by 1
arr7 = [10, 20, 30, 40, 50]
rotateArr(arr7, 1)
assert arr7 == [20, 30, 40, 50, 10]

# Test Case 8: Rotate by n-1
arr8 = [1, 2, 3, 4, 5]
rotateArr(arr8, 4)  # Move 4 left = move 1 right
assert arr8 == [5, 1, 2, 3, 4]

# Test Case 9: Large d value
arr9 = [1, 2, 3]
rotateArr(arr9, 1000000)  # 1000000 % 3 = 1
assert arr9 == [2, 3, 1]

# Test Case 10: Negative numbers
arr10 = [-1, -2, -3, -4, -5]
rotateArr(arr10, 2)
assert arr10 == [-3, -4, -5, -1, -2]

# Test Case 11: With zeros
arr11 = [0, 1, 0, 2, 0, 3]
rotateArr(arr11, 3)
assert arr11 == [2, 0, 3, 0, 1, 0]

# Test Case 12: All same elements
arr12 = [5, 5, 5, 5]
rotateArr(arr12, 2)
assert arr12 == [5, 5, 5, 5]
```

---

## ⭐ Quick Reference Card
```
╔════════════════════════════════════════════════╗
║      ROTATE ARRAY - QUICK REFERENCE            ║
╠════════════════════════════════════════════════╣
║ Time Complexity:    O(n)                       ║
║ Space Complexity:   O(1)                       ║
║ Approach:           Reversal Algorithm         ║
║ In-Place:           Yes                        ║
║                                                ║
║ Key Steps (Left Rotation by d):                ║
║ 1. d = d % n         (Handle edge cases)       ║
║ 2. Reverse(0, d-1)   (Reverse first part)      ║
║ 3. Reverse(d, n-1)   (Reverse second part)     ║
║ 4. Reverse(0, n-1)   (Reverse entire)          ║
║                                                ║
║ Why It Works:                                  ║
║ [A, B | C, D, E]  →  [B, A | E, D, C]          ║
║                   →  [C, D, E, A, B]           ║
║                                                ║
║ Common Pitfalls:                               ║
║ ❌ Forgetting d = d % n                        ║ 
║ ❌ Wrong reversal order                        ║
║ ❌ Off-by-one in indices                       ║
╚════════════════════════════════════════════════╝
```

---
## 🔄 Algorithm Variations Comparison

| Approach | Time | Space | Difficulty | Best For |
|----------|------|-------|------------|----------|
| **Reversal** ⭐ | O(n) | O(1) | Easy | Most cases |
| Temp Array | O(n) | O(n) | Very Easy | Learning |
| One-by-One | O(n×d) | O(1) | Easy | Small d |
| Juggling | O(n) | O(1) | Hard | Interviews |
| Block Swap | O(n) | O(1) | Hard | Theory |
---


```
### Common Interview Questions
```
```
**Q: Why use reversal algorithm over others?**
```
A: It's optimal (O(n) time, O(1) space), easy to understand 
   and implement, and works perfectly for both left and 
   right rotations with minor modifications.
```

**Q: How does d = d % n help?**
```
A: It handles three cases elegantly:
   1. d > n: Eliminates full rotations
   2. d = n: Results in 0 (no rotation)
   3. d < n: No change (optimization not needed)
```

**Q: Can you explain why three reversals work?**
```
A: Think of it as rearranging two parts:
   Original: [Part A, Part B]
   Goal: [Part B, Part A]
   
   Reversing each part then reversing the whole achieves 
   this transformation elegantly.
```

**Q: What if we want right rotation instead?**
```
A: Two options:
   1. Left rotate by (n - d) positions
   2. Adjust reversal sequence:
      - Reverse(0, n-d-1)
      - Reverse(n-d, n-1)
      - Reverse(0, n-1)
```

**Q: Time complexity proof?**
```
A: Three operations:
   - Reverse d elements: O(d)
   - Reverse (n-d) elements: O(n-d)
   - Reverse n elements: O(n)
   Total: O(d) + O(n-d) + O(n) = O(2n) = O(n)

```
Last Updated: January 2026
Version: 1.0.0
Algorithm Difficulty: Medium ⭐⭐
Topics: Arrays, Two Pointers, Reversal Algorithm, In-Place Operations

This comprehensive README provides everything needed to understand the array rotation algorithm using the reversal technique, including detailed dry runs, visual representations, edge case handling, common mistakes, and interview preparation tips.
```

