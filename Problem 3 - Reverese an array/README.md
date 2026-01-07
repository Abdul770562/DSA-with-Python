# Reverse Array - Algorithm Documentation

A comprehensive guide to understanding and implementing the "Reverse Array" algorithm with detailed explanations, dry runs, and visual examples.

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

Given an array of integers, reverse the array **in-place** without using extra space. The first element should become the last, the second element should become second last, and so on.

### Requirements

✅ Reverse the array elements  
✅ In-place modification (no extra array)  
✅ O(n) time complexity  
✅ O(1) space complexity  

---

## 💡 Examples

### Example 1
```
Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Explanation: 
- First element (1) becomes last
- Last element (5) becomes first
- All elements reversed
```

### Example 2
```
Input:  [10, 20, 30, 40]
Output: [40, 30, 20, 10]
```

### Example 3
```
Input:  [7]
Output: [7]

Explanation: Single element array remains unchanged
```

### Example 4
```
Input:  [5, 5]
Output: [5, 5]

Explanation: Two identical elements swapped
```

### Example 5
```
Input:  [1, 2, 3, 4, 5, 6]
Output: [6, 5, 4, 3, 2, 1]
```

---

## 🚫 Constraints

- Array can contain any integers (positive, negative, or zero)
- No extra array allowed (in-place operation)
- Array length: 1 ≤ n ≤ 10^6
- Array must be modified in-place

---

## 🧠 Approach

### Two-Pointer Technique

The algorithm uses a two-pointer approach with pointers moving from opposite ends:

1. **Left Pointer (`i`)**: Starts from the beginning (index 0)
2. **Right Pointer (`j`)**: Starts from the end (index n-1)

### Strategy
```
1. Place one pointer at start, one at end
2. Swap elements at both pointers
3. Move pointers toward center
4. Stop when pointers meet or cross
```

### Why This Works

- Each swap puts two elements in their final positions
- Pointers converge toward the center
- When pointers meet/cross, all elements are reversed
- Only n/2 swaps needed for n elements

---

## 📝 Algorithm

### Step-by-Step Process
```
1. Initialize two pointers:
   - i = 0 (left pointer at start)
   - j = n-1 (right pointer at end)

2. While i < j:
   - Swap arr[i] and arr[j]
   - Move i forward (i++)
   - Move j backward (j--)

3. Array is now reversed
```


---

## 💻 Implementation

### Python
```python
class Solution:
    def reverseArray(self, arr):
        """
        Reverse array in-place using two pointers
        
        Args:
            arr: List of integers
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        i = 0       # Left pointer
        j = n - 1   # Right pointer
        
        # Swap elements while pointers haven't crossed
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            i += 1  # Move left pointer forward
            j -= 1  # Move right pointer backward
```

---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**

- Loop runs approximately n/2 times
- Each iteration performs constant time operations (swap)
- Total: O(n/2) = O(n)

**Detailed Breakdown:**
```
For array of size n:
- Number of swaps = n/2
- Each swap = O(1)
- Total = n/2 × O(1) = O(n)
```

### Space Complexity: **O(1)**

- Only uses three variables: `n`, `i`, `j`
- No extra array or data structure
- In-place modification

### Why O(1) Space?
```
Variables used:
- n: stores array length (constant space)
- i: left pointer (constant space)
- j: right pointer (constant space)
- temp (in swap): temporary variable (constant space)

Total: O(1) constant space
```

### Comparison with Alternative Approaches

| Approach | Time | Space | In-Place | Note |
|----------|------|-------|----------|------|
| Two-Pointer (Our solution) | O(n) | O(1) | ✅ Yes | Optimal |
| Using Extra Array | O(n) | O(n) | ❌ No | Simple but uses space |
| Recursion | O(n) | O(n) | ✅ Yes | Call stack space |
| Stack | O(n) | O(n) | ❌ No | Push all, then pop |
| Python slice [::-1] | O(n) | O(n) | ❌ No | Creates new array |

---

## 🔍 Detailed Dry Run

### Input Array
```
arr = [1, 2, 3, 4, 5]
```

### Initial State
```
n = 5
i = 0
j = 4
```

---

### Iteration-by-Iteration Execution

#### **Initial Setup**
```
Array: [1, 2, 3, 4, 5]
        ↑           ↑
        i=0       j=4
        
Condition: i < j → 0 < 4 → True ✅
```

---

#### **Iteration 1**

**Before Swap:**
```
Array: [1, 2, 3, 4, 5]
        ↑           ↑
        i=0       j=4
```

**Swap Operation:**
```python
arr[i], arr[j] = arr[j], arr[i]
arr[0], arr[4] = arr[4], arr[0]
arr[0], arr[4] = 5, 1
```

**After Swap:**
```
Array: [5, 2, 3, 4, 1]
        ↑           ↑
        i=0       j=4
```

**Update Pointers:**
```python
i = i + 1 → i = 1
j = j - 1 → j = 3
```

**State After Iteration 1:**
```
Array: [5, 2, 3, 4, 1]
           ↑     ↑
         i=1   j=3
         
Condition: i < j → 1 < 3 → True ✅
```

---

#### **Iteration 2**

**Before Swap:**
```
Array: [5, 2, 3, 4, 1]
           ↑     ↑
         i=1   j=3
```

**Swap Operation:**
```python
arr[1], arr[3] = arr[3], arr[1]
arr[1], arr[3] = 4, 2
```

**After Swap:**
```
Array: [5, 4, 3, 2, 1]
           ↑     ↑
         i=1   j=3
```

**Update Pointers:**
```python
i = i + 1 → i = 2
j = j - 1 → j = 2
```

**State After Iteration 2:**
```
Array: [5, 4, 3, 2, 1]
              ↑
            i=2
            j=2
            
Condition: i < j → 2 < 2 → False ❌
```

---

#### **Loop Terminates**
```
Final condition: i < j → 2 < 2 → False
Loop exits
```

**Why Stop Here?**
- When `i == j`, pointers meet at middle element
- Middle element (3) is already in correct position
- No need to swap an element with itself

---

### Final Output
```
Array: [5, 4, 3, 2, 1]
```

✅ Array successfully reversed!

---

## 🎨 Visual Representation

### Complete Visualization
```
Initial Array:
┌───┬───┬───┬───┬───┐
│ 1 │ 2 │ 3 │ 4 │ 5 │
└───┴───┴───┴───┴───┘
  ↑               ↑
  i=0           j=4

After Swap 1:
┌───┬───┬───┬───┬───┐
│ 5 │ 2 │ 3 │ 4 │ 1 │
└───┴───┴───┴───┴───┘
      ↑       ↑
    i=1     j=3

After Swap 2:
┌───┬───┬───┬───┬───┐
│ 5 │ 4 │ 3 │ 2 │ 1 │
└───┴───┴───┴───┴───┘
          ↑
        i=2, j=2
        (Pointers meet - STOP)

Final Reversed Array:
┌───┬───┬───┬───┬───┐
│ 5 │ 4 │ 3 │ 2 │ 1 │
└───┴───┴───┴───┴───┘
```

### Step-by-Step Pointer Movement
```
Step 0: [1, 2, 3, 4, 5]
         ↑           ↑
         i           j

Step 1: [5, 2, 3, 4, 1]
            ↑     ↑
            i     j

Step 2: [5, 4, 3, 2, 1]
               ↑
              i,j  (Stop!)
```

---

## 🎯 Dry Run with Even Length Array

### Input Array
```
arr = [10, 20, 30, 40, 50, 60]
```

### Initial State
```
n = 6
i = 0
j = 5
```

---

### Execution Steps

#### **Iteration 1**
```
Before: [10, 20, 30, 40, 50, 60]
         ↑                   ↑
         i=0               j=5

Swap: arr[0] ↔ arr[5]

After:  [60, 20, 30, 40, 50, 10]
             ↑           ↑
           i=1         j=4
```

#### **Iteration 2**
```
Before: [60, 20, 30, 40, 50, 10]
             ↑           ↑
           i=1         j=4

Swap: arr[1] ↔ arr[4]

After:  [60, 50, 30, 40, 20, 10]
                 ↑   ↑
               i=2 j=3
```

#### **Iteration 3**
```
Before: [60, 50, 30, 40, 20, 10]
                 ↑   ↑
               i=2 j=3

Swap: arr[2] ↔ arr[3]

After:  [60, 50, 40, 30, 20, 10]
                     ↑
                   i=3
                   j=2
                   
Condition: i < j → 3 < 2 → False ❌
Loop exits
```

### Final Output
```
[60, 50, 40, 30, 20, 10]
```

✅ Even-length array successfully reversed!

---

## 📊 Detailed Step Table

### For Array: [1, 2, 3, 4, 5]

| Step | i | j | i < j | arr[i] | arr[j] | Action | Array State |
|------|---|---|-------|--------|--------|--------|-------------|
| Init | 0 | 4 | ✅ True | 1 | 5 | - | [1, 2, 3, 4, 5] |
| 1 | 0 | 4 | ✅ True | 1 | 5 | Swap | [5, 2, 3, 4, 1] |
| 1 | 1 | 3 | ✅ True | - | - | Update | [5, 2, 3, 4, 1] |
| 2 | 1 | 3 | ✅ True | 2 | 4 | Swap | [5, 4, 3, 2, 1] |
| 2 | 2 | 2 | ❌ False | - | - | Update | [5, 4, 3, 2, 1] |
| End | 2 | 2 | ❌ False | - | - | Exit | [5, 4, 3, 2, 1] |

---

## 🎯 Key Takeaways

### Core Concepts

1. **Two-Pointer Pattern**: Converging pointers from opposite ends
2. **Symmetry**: Exploits the symmetric nature of reversal
3. **In-Place**: Direct element swapping without extra space
4. **Linear Time**: Single pass through half the array

### Memory Trick

> **"Meet in the middle by swapping from both ends"**

### When to Use This Approach

- ✅ Need to reverse any sequence
- ✅ In-place modification required
- ✅ Optimal time and space needed
- ✅ Simple and intuitive solution

### Why Two Pointers Work Here
```
Original:  [1, 2, 3, 4, 5]
            ↓           ↓
Target:    [5, 4, 3, 2, 1]

Each swap puts TWO elements in final position:
- Swap 1: Places 5 and 1 correctly
- Swap 2: Places 4 and 2 correctly
- Middle element (3) stays in place
```

---

## ⚠️ Common Mistakes

### Mistake 1: Wrong Loop Condition
```python
# ❌ Wrong - Uses i <= j instead of i < j
while i <= j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
    
# Problem: When i == j (middle element), it swaps with itself
# For odd-length arrays, this is unnecessary but harmless
# For even-length arrays, pointers cross and swap back!
```

**Correct:**
```python
# ✅ Correct - Stop when pointers meet or cross
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
```

---

### Mistake 2: Forgetting to Update Pointers
```python
# ❌ Wrong - Infinite loop!
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    # Missing: i += 1 and j -= 1
    # Result: Infinite loop, keeps swapping same elements
```

**Correct:**
```python
# ✅ Correct - Always update both pointers
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
```

---

### Mistake 3: Wrong Initial Values
```python
# ❌ Wrong - j starts at n instead of n-1
n = len(arr)
i = 0
j = n  # Wrong! Should be n-1

# Problem: Index out of bounds
# arr[5] doesn't exist for array of length 5
```

**Correct:**
```python
# ✅ Correct - j starts at last valid index
n = len(arr)
i = 0
j = n - 1  # Last index
```

---

### Mistake 4: Not Swapping In-Place
```python
# ❌ Wrong - Creates new list instead of in-place
def reverseArray(arr):
    return arr[::-1]  # Returns new list
    
# Problem: Not in-place, uses O(n) extra space
```

**Correct:**
```python
# ✅ Correct - Modifies original array
def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
```

---

### Mistake 5: Incorrect Swap Logic
```python
# ❌ Wrong - Incorrect swap (missing temp variable in some languages)
arr[i] = arr[j]
arr[j] = arr[i]

# Problem: arr[i] value is lost before assignment to arr[j]
# Both end up with same value (original arr[j])
```

**Correct (Python):**
```python
# ✅ Correct - Simultaneous assignment
arr[i], arr[j] = arr[j], arr[i]
```

**Correct (Other Languages):**
```python
# ✅ Correct - Using temp variable
temp = arr[i]
arr[i] = arr[j]
arr[j] = temp
```

---

## 🔗 Practice Problems

### Similar Problems

1. **Rotate Array** - Extension of reversal technique
2. **Reverse String** - Same algorithm, different data type
3. **Palindrome Check** - Uses similar two-pointer approach
4. **Reverse Array in Groups** - Reverse subarrays

### LeetCode Problems

- [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- [541. Reverse String II](https://leetcode.com/problems/reverse-string-ii/)

### Variations to Try

#### 1. Reverse Specific Range
```python
def reverseRange(arr, start, end):
    """Reverse array from index start to end"""
    i = start
    j = end
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
```

#### 2. Reverse Array in Groups
```python
def reverseInGroups(arr, k):
    """Reverse array in groups of size k"""
    n = len(arr)
    for i in range(0, n, k):
        left = i
        right = min(i + k - 1, n - 1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
```

#### 3. Check if Array is Palindrome
```python
def isPalindrome(arr):
    """Check if array reads same forwards and backwards"""
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] != arr[j]:
            return False
        i += 1
        j -= 1
    return True
```

---

## 🧪 Test Cases
```python
# Test Case 1: Odd length array
arr1 = [1, 2, 3, 4, 5]
reverseArray(arr1)
assert arr1 == [5, 4, 3, 2, 1]

# Test Case 2: Even length array
arr2 = [10, 20, 30, 40]
reverseArray(arr2)
assert arr2 == [40, 30, 20, 10]

# Test Case 3: Single element
arr3 = [42]
reverseArray(arr3)
assert arr3 == [42]

# Test Case 4: Two elements
arr4 = [1, 2]
reverseArray(arr4)
assert arr4 == [2, 1]

# Test Case 5: All same elements
arr5 = [5, 5, 5, 5]
reverseArray(arr5)
assert arr5 == [5, 5, 5, 5]

# Test Case 6: Negative numbers
arr6 = [-1, -2, -3, -4]
reverseArray(arr6)
assert arr6 == [-4, -3, -2, -1]

# Test Case 7: Mixed positive and negative
arr7 = [1, -2, 3, -4, 5]
reverseArray(arr7)
assert arr7 == [5, -4, 3, -2, 1]

# Test Case 8: With zeros
arr8 = [0, 1, 0, 2, 0]
reverseArray(arr8)
assert arr8 == [0, 2, 0, 1, 0]

# Test Case 9: Large array
arr9 = list(range(1, 101))  # [1, 2, ..., 100]
reverseArray(arr9)
assert arr9 == list(range(100, 0, -1))  # [100, 99, ..., 1]

# Test Case 10: Already reversed (palindrome)
arr10 = [1, 2, 3, 2, 1]
reverseArray(arr10)
assert arr10 == [1, 2, 3, 2, 1]
```

---

## 🎓 Edge Cases to Consider

### 1. Empty Array
```python
arr = []
# Length is 0, so i=0, j=-1
# Loop condition i < j → 0 < -1 → False
# Nothing happens (correct behavior)
```

### 2. Single Element
```python
arr = [5]
# i=0, j=0
# Loop condition i < j → 0 < 0 → False
# No swap needed (correct)
```

### 3. Two Elements
```python
arr = [1, 2]
# i=0, j=1
# One swap: [2, 1]
# Then i=1, j=0
# Loop exits (correct)
```

### 4. Very Large Array
```python
arr = [1] * 10**6
# Still O(n) time
# Still O(1) space
# Algorithm scales well
```

---

## 📚 Additional Resources

- [GeeksforGeeks - Reverse an Array](https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/)
- [Two-Pointer Technique](https://leetcode.com/articles/two-pointer-technique/)
- [In-Place Algorithms](https://en.wikipedia.org/wiki/In-place_algorithm)
- [Array Manipulation Techniques](https://www.geeksforgeeks.org/array-data-structure/)

---

## 💡 Pro Tips

### 1. Python Swap Shortcut
```python
# Python allows simultaneous assignment
arr[i], arr[j] = arr[j], arr[i]

# Equivalent to:
temp = arr[i]
arr[i] = arr[j]
arr[j] = temp
```

### 2. Using Built-in Functions
```python
# Python built-in (creates new list)
reversed_arr = arr[::-1]

# In-place with built-in
arr.reverse()

# But for learning, implement manually!
```

### 3. Recursion Approach (Alternative)
```python
def reverseRecursive(arr, i, j):
    if i >= j:
        return
    arr[i], arr[j] = arr[j], arr[i]
    reverseRecursive(arr, i + 1, j - 1)

# Call: reverseRecursive(arr, 0, len(arr) - 1)
# Note: Uses O(n) call stack space
```

---

## ⭐ Quick Reference Card
```
╔════════════════════════════════════════════════╗
║       REVERSE ARRAY - QUICK REFERENCE          ║
╠════════════════════════════════════════════════╣
║ Time Complexity:    O(n)                       ║
║ Space Complexity:   O(1)                       ║
║ Approach:           Two-Pointer (converging)   ║
║ In-Place:           Yes                        ║
║ Stable:             N/A                        ║
║                                                ║
║ Key Steps:                                     ║
║ 1. i = 0, j = n-1                              ║
║ 2. While i < j:                                ║
║    - Swap arr[i] and arr[j]                    ║
║    - i++, j--                                  ║
║                                                ║
║ Common Pitfalls:                               ║
║ ❌ Using i <= j instead of i < j               ║
║ ❌ Forgetting to update pointers               ║
║ ❌ Wrong initial value for j                   ║
╚════════════════════════════════════════════════╝
```

---

## 🔄 Algorithm Variations Comparison

| Variation | Time | Space | Note |
|-----------|------|-------|------|
| Two-Pointer | O(n) | O(1) | Optimal ⭐ |
| Recursion | O(n) | O(n) | Call stack |
| Extra Array | O(n) | O(n) | Simple |
| Stack | O(n) | O(n) | Push/Pop |
| Built-in reverse() | O(n) | O(1) | Language specific |
| Slicing [::-1] | O(n) | O(n) | Python only |

---

## 📝 Interview Tips

### What Interviewers Look For

1. ✅ **Understanding of two-pointer technique**
2. ✅ **Correct loop termination condition**
3. ✅ **In-place modification**
4. ✅ **Handling edge cases**
5. ✅ **Clean, readable code**

### Common Interview Questions

**Q: Why use `i < j` and not `i <= j`?**
```
A: When i == j, we're at the middle element. No need to swap 
   an element with itself. Using <= would cause unnecessary 
   operation and for even-length arrays, pointers would cross 
   and swap back incorrectly.
```

**Q: Can you do it without extra space?**
```
A: Yes, the two-pointer approach uses only O(1) extra space 
   (just i, j, and n variables). We modify array in-place.
```

**Q: What's the time complexity and why?**
```
A: O(n) because we traverse half the array (n/2 swaps), 
   and each swap is O(1). So n/2 × O(1) = O(n).
```

**Q: How do you handle empty or single-element arrays?**
```
A: The loop condition i < j naturally handles these:
   - Empty: i=0, j=-1 → 0 < -1 is False → No iterations
   - Single: i=0, j=0 → 0 < 0 is False → No iterations
```

---

## 🎬 Animated Concept
```
Frame 1:  [1, 2, 3, 4, 5]
           ↓           ↓
          i=0        j=4
          
Frame 2:  [5, 2, 3, 4, 1]  (After swap)
              ↓     ↓
            i=1   j=3
            
Frame 3:  [5, 4, 3, 2, 1]  (After swap)
                 ↓
               i=2, j=2
               
          COMPLETE! ✅
```

---

## 📄 License

This documentation is free to use for educational purposes.

---

## 🤝 Contributing

Found an error or want to improve this guide?
- Open an issue
- Submit a pull request
- Suggest improvements

---

## 📧 Feedback

Have questions or suggestions? Feel free to reach out or leave feedback!

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Algorithm Difficulty**: Easy ⭐  
**Topic**: Arrays, Two Pointers

---

## 🎉 Congratulations!

You now understand the **Reverse Array** algorithm completely. Practice implementing it in different languages and try the variations mentioned above!

**Remember**: 
> "Two pointers from opposite ends, meeting in the middle - the essence of elegant reversal!" 🚀
