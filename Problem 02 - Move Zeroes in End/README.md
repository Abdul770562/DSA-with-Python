# Move Zeros to End - Algorithm Documentation

A comprehensive guide to understanding and implementing the "Move Zeros to End" algorithm with detailed explanations, dry runs, and visual examples.

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

Given an array of non-negative integers, move all zeros to the end while maintaining the relative order of non-zero elements. The operation must be performed **in-place** without using extra space.

### Requirements

✅ Move all zeros to the end  
✅ Maintain order of non-zero elements  
✅ In-place modification (no extra array)  
✅ O(n) time complexity  

---

## 💡 Examples

### Example 1
```
Input:  [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]

Explanation: 
- Non-zero elements: 1, 2, 4, 3, 5 (order maintained)
- All zeros moved to end: 0, 0, 0
```

### Example 2
```
Input:  [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

### Example 3
```
Input:  [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]

Explanation: No zeros present, array remains unchanged
```

### Example 4
```
Input:  [0, 0, 0, 1]
Output: [1, 0, 0, 0]
```

---

## 🚫 Constraints

- Array contains **non-negative integers** only
- No extra array allowed (in-place operation)
- Relative order of non-zero elements must be preserved
- Array length: 1 ≤ n ≤ 10^5

---

## 🧠 Approach

### Two-Pointer Technique

The algorithm uses a two-pointer approach:

1. **Scan Pointer (`i`)**: Iterates through the entire array
2. **Position Pointer (`pos`)**: Tracks where the next non-zero element should be placed

### Strategy
```
Phase 1: Collect all non-zero elements at the front
Phase 2: Fill remaining positions with zeros
```

### Why This Works

- By processing elements left-to-right, we naturally preserve order
- Non-zero elements are compacted to the front
- The `pos` pointer automatically marks where zeros should start

---

## 📝 Algorithm

### Step-by-Step Process
```
1. Initialize pos = 0 (position for next non-zero element)

2. For each element in array:
   - If element != 0:
     * Place element at index pos
     * Increment pos

3. Fill remaining positions (from pos to end) with 0
```



---

## 💻 Implementation

### Python
```python
class Solution:
    def pushZerosToEnd(self, arr):
        """
        Move all zeros to the end of array in-place
        
        Args:
            arr: List of non-negative integers
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        pos = 0  # Position to place next non-zero element
        
        # Step 1: Move non-zero elements to the front
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Step 2: Fill remaining positions with zero
        while pos < n:
            arr[pos] = 0
            pos += 1
```

---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**

- First loop: O(n) - traverse entire array once
- Second loop: O(n) - worst case, fill all positions
- Total: O(n) + O(n) = O(n)

### Space Complexity: **O(1)**

- Only uses two variables: `n` and `pos`
- No extra array or data structure
- In-place modification

### Comparison with Alternative Approaches

| Approach | Time | Space | In-Place |
|----------|------|-------|----------|
| Two-Pointer (Our solution) | O(n) | O(1) | ✅ Yes |
| Using Extra Array | O(n) | O(n) | ❌ No |
| Bubble Sort Variant | O(n²) | O(1) | ✅ Yes |
| Counting Sort | O(n) | O(1) | ✅ Yes |

---

## 🔍 Detailed Dry Run

### Input Array
```
arr = [1, 2, 0, 4, 3, 0, 5, 0]
```

### Initial State
```
n = 8
pos = 0
```

---

### Phase 1: Moving Non-Zero Elements

#### Iteration 1 (i=0)
```
arr[0] = 1 (non-zero)
→ arr[pos] = arr[0] = 1
→ pos = 1

Array: [1, 2, 0, 4, 3, 0, 5, 0]
       ↑
      pos=1
```

#### Iteration 2 (i=1)
```
arr[1] = 2 (non-zero)
→ arr[pos] = arr[1] = 2
→ pos = 2

Array: [1, 2, 0, 4, 3, 0, 5, 0]
          ↑
         pos=2
```

#### Iteration 3 (i=2)
```
arr[2] = 0 (zero - skip)
→ pos remains 2

Array: [1, 2, 0, 4, 3, 0, 5, 0]
          ↑
         pos=2
```

#### Iteration 4 (i=3)
```
arr[3] = 4 (non-zero)
→ arr[pos] = arr[3] = 4
→ pos = 3

Array: [1, 2, 4, 4, 3, 0, 5, 0]
             ↑
            pos=3
```

#### Iteration 5 (i=4)
```
arr[4] = 3 (non-zero)
→ arr[pos] = arr[4] = 3
→ pos = 4

Array: [1, 2, 4, 3, 3, 0, 5, 0]
                ↑
               pos=4
```

#### Iteration 6 (i=5)
```
arr[5] = 0 (zero - skip)
→ pos remains 4

Array: [1, 2, 4, 3, 3, 0, 5, 0]
                ↑
               pos=4
```

#### Iteration 7 (i=6)
```
arr[6] = 5 (non-zero)
→ arr[pos] = arr[6] = 5
→ pos = 5

Array: [1, 2, 4, 3, 5, 0, 5, 0]
                   ↑
                  pos=5
```

#### Iteration 8 (i=7)
```
arr[7] = 0 (zero - skip)
→ pos remains 5

Array: [1, 2, 4, 3, 5, 0, 5, 0]
                   ↑
                  pos=5
```

---

### Phase 2: Filling Zeros

#### State After Phase 1
```
Array: [1, 2, 4, 3, 5, 0, 5, 0]
pos = 5
All non-zeros are now in first 5 positions
```

#### Fill Iteration 1
```
arr[5] = 0
pos = 6

Array: [1, 2, 4, 3, 5, 0, 5, 0]
```

#### Fill Iteration 2
```
arr[6] = 0
pos = 7

Array: [1, 2, 4, 3, 5, 0, 0, 0]
```

#### Fill Iteration 3
```
arr[7] = 0
pos = 8

Array: [1, 2, 4, 3, 5, 0, 0, 0]
```

Loop ends (pos == n)

---

### Final Output
```
[1, 2, 4, 3, 5, 0, 0, 0]
```

✅ All non-zeros maintained order: 1, 2, 4, 3, 5  
✅ All zeros moved to end: 0, 0, 0

---

## 🎨 Visual Representation
```
Initial Array:
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 0 │ 4 │ 3 │ 0 │ 5 │ 0 │
└───┴───┴───┴───┴───┴───┴───┴───┘

After Phase 1 (Non-zero collection):
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 4 │ 3 │ 5 │ 0 │ 5 │ 0 │
└───┴───┴───┴───┴───┴───┴───┴───┘
                  ↑
                 pos

After Phase 2 (Zero filling):
┌───┬───┬───┬───┬───┬───┬───┬───┐
│ 1 │ 2 │ 4 │ 3 │ 5 │ 0 │ 0 │ 0 │
└───┴───┴───┴───┴───┴───┴───┴───┘
  Non-zero elements   All zeros
```

---

## 🎯 Key Takeaways

### Core Concepts

1. **Two-Pointer Pattern**: One pointer scans, another marks position
2. **Order Preservation**: Processing left-to-right maintains relative order
3. **In-Place**: No extra space needed, modify array directly
4. **Linear Time**: Single pass for collection, single pass for filling

### Memory Trick

> **"Collect non-zeros at front → Fill rest with zeros"**

### When to Use This Approach

- ✅ Need to move elements to one end
- ✅ Must maintain relative order
- ✅ In-place modification required
- ✅ Linear time complexity needed

---

## ⚠️ Common Mistakes

### Mistake 1: Using Swaps Unnecessarily
```python
# ❌ Wrong - Creates unnecessary swaps
for i in range(n):
    if arr[i] == 0:
        # Swap with next non-zero
        # This can disrupt order
```

### Mistake 2: Not Filling Remaining Positions
```python
# ❌ Wrong - Forgets to fill zeros
for i in range(n):
    if arr[i] != 0:
        arr[pos] = arr[i]
        pos += 1
# Missing: Fill rest with zeros!
```

### Mistake 3: Using Extra Space
```python
# ❌ Wrong - Uses extra array
non_zeros = [x for x in arr if x != 0]
zeros = [0] * (len(arr) - len(non_zeros))
return non_zeros + zeros  # Not in-place!
```

### Mistake 4: Incorrect Loop Conditions
```python
# ❌ Wrong - pos might go out of bounds
while pos <= n:  # Should be pos < n
    arr[pos] = 0
    pos += 1
```

---

## 🔗 Practice Problems

### Similar Problems

1. **Move All Negative Numbers to Beginning** (Same pattern)
2. **Segregate 0s and 1s** (Two-pointer approach)
3. **Sort Array by Parity** (Even numbers first)
4. **Remove Element** (In-place removal)

### LeetCode Problems

- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [27. Remove Element](https://leetcode.com/problems/remove-element/)
- [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

### Variations to Try

1. Move all negative numbers to the end
2. Move all even numbers to the beginning
3. Move all duplicates to the end
4. Partition array by given value

---

## 🧪 Test Cases
```python
# Test Case 1: Standard case
assert pushZerosToEnd([1, 2, 0, 4, 3, 0, 5, 0]) == [1, 2, 4, 3, 5, 0, 0, 0]

# Test Case 2: All zeros
assert pushZerosToEnd([0, 0, 0, 0]) == [0, 0, 0, 0]

# Test Case 3: No zeros
assert pushZerosToEnd([1, 2, 3, 4]) == [1, 2, 3, 4]

# Test Case 4: Single element
assert pushZerosToEnd([0]) == [0]
assert pushZerosToEnd([5]) == [5]

# Test Case 5: Zeros at beginning
assert pushZerosToEnd([0, 0, 1, 2, 3]) == [1, 2, 3, 0, 0]

# Test Case 6: Zeros at end
assert pushZerosToEnd([1, 2, 3, 0, 0]) == [1, 2, 3, 0, 0]
```

---

## 📚 Additional Resources

- [GeeksforGeeks - Move All Zeros to End](https://www.geeksforgeeks.org/move-zeroes-end-array/)
- [Two-Pointer Technique Explained](https://leetcode.com/articles/two-pointer-technique/)
- [In-Place Algorithms](https://en.wikipedia.org/wiki/In-place_algorithm)

---

## 📄 License

This documentation is free to use for educational purposes.

---

## 🤝 Contributing

Found an error or want to improve this guide? Feel free to:
- Open an issue
- Submit a pull request
- Suggest improvements

---

## ⭐ Quick Reference Card
```
╔══════════════════════════════════════════════╗
║       MOVE ZEROS TO END - QUICK REF          ║
╠══════════════════════════════════════════════╣
║ Time Complexity:    O(n)                     ║
║ Space Complexity:   O(1)                     ║
║ Approach:           Two-Pointer              ║
║ Stability:          Maintains order          ║
║                                              ║
║ Key Steps:                                   ║
║ 1. pos = 0                                   ║
║ 2. For each non-zero: arr[pos++] = element  ║
║ 3. Fill rest with zeros                      ║
╚══════════════════════════════════════════════╝
```

---

**Last Updated**: January 2026  
**Version**: 1.0.0
