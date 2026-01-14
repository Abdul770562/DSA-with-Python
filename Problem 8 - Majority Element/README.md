# Majority Element II (n/3 Times) - Boyer-Moore Voting Algorithm

A comprehensive guide to understanding and implementing the **Boyer-Moore Voting Algorithm** for finding elements that appear more than ⌊n/3⌋ times, with detailed explanations, dry runs, and visual examples.

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

Given an array `arr[]` of `n` integers, find all elements that appear **more than ⌊n/3⌋ times**.

### Requirements

✅ Find elements appearing > n/3 times  
✅ Return sorted array of majority elements  
✅ Handle negative numbers  
✅ Optimal O(n) time complexity  
✅ O(1) space complexity (excluding output)  

### Key Insight

**Mathematical Fact**: At most **2 elements** can appear more than n/3 times.

**Proof**:
```
If 3 elements each appear > n/3 times:
Total count > 3 × (n/3) = n
This is impossible! Array has only n elements.

Therefore, maximum 2 elements can satisfy this condition.
```

---

## 💡 Examples

### Example 1: Two Majority Elements
```
Input:  arr = [2, 2, 3, 1, 3, 2, 1, 1]
Output: [1, 2]

Explanation: 
n = 8
n/3 = 8/3 = 2 (floor)

Frequency count:
1 appears 3 times (3 > 2) ✅
2 appears 3 times (3 > 2) ✅
3 appears 2 times (2 = 2) ❌

Result: [1, 2] (sorted)
```

### Example 2: Single Majority Element
```
Input:  arr = [-5, 3, -5]
Output: [-5]

Explanation:
n = 3
n/3 = 3/3 = 1 (floor)

Frequency count:
-5 appears 2 times (2 > 1) ✅
3 appears 1 time (1 = 1) ❌

Result: [-5]
```

### Example 3: No Majority Element
```
Input:  arr = [3, 2, 2, 4, 1, 4]
Output: []

Explanation:
n = 6
n/3 = 6/3 = 2 (floor)

Frequency count:
All elements appear ≤ 2 times
No element appears > 2 times

Result: [] (empty)
```

### Example 4: Single Element
```
Input:  arr = [5]
Output: [5]

Explanation:
n = 1
n/3 = 1/3 = 0 (floor)

5 appears 1 time (1 > 0) ✅

Result: [5]
```

### Example 5: All Same Elements
```
Input:  arr = [7, 7, 7, 7, 7]
Output: [7]

Explanation:
n = 5
n/3 = 5/3 = 1 (floor)

7 appears 5 times (5 > 1) ✅

Result: [7]
```

---

## 🚫 Constraints

- `1 <= arr.size() <= 10^6`
- `-10^5 <= arr[i] <= 10^5`
- Array can have negative numbers
- Array can have duplicates
- Return sorted array

---

## 🧠 Approach

### Boyer-Moore Voting Algorithm (Extended)

The classic Boyer-Moore algorithm finds majority element (> n/2). We extend it to find elements appearing > n/3 times.

### Core Idea

Since at most **2 elements** can appear > n/3 times, we:
1. **Find 2 candidates** using modified voting
2. **Verify candidates** by counting their occurrences

### Two-Phase Approach
```
Phase 1: VOTING (Find potential candidates)
- Maintain 2 candidates and their counts
- Use voting mechanism to narrow down candidates

Phase 2: VERIFICATION (Confirm candidates)
- Count actual occurrences of candidates
- Keep only those appearing > n/3 times
```

### Why This Works

**Voting Logic**:
- If element matches a candidate, increment its count
- If counts are zero, replace candidate
- If element matches neither candidate, decrement both counts
- This ensures true majority elements survive

**Key Insight**: 
```
If an element appears > n/3 times, it will definitely
be one of the 2 candidates after voting phase.
```

---

## 📝 Algorithm

### Detailed Steps
```
Phase 1: Find Candidates
1. Initialize:
   - cand1, cand2 = None (two candidates)
   - count1, count2 = 0 (their counts)

2. For each element in array:
   a. If element == cand1:
      - Increment count1
   
   b. Else if element == cand2:
      - Increment count2
   
   c. Else if count1 == 0:
      - Set cand1 = element, count1 = 1
   
   d. Else if count2 == 0:
      - Set cand2 = element, count2 = 1
   
   e. Else (element doesn't match, both counts > 0):
      - Decrement both count1 and count2

Phase 2: Verify Candidates
3. For each candidate:
   - Count actual occurrences in array
   - If count > n/3: add to result

4. Sort and return result
```
---

## 💻 Implementation

### Python (Given Solution)
```python
class Solution:
    def findMajority(self, arr):
        """
        Find all elements appearing more than n/3 times
        
        Args:
            arr: List of integers
            
        Returns:
            Sorted list of majority elements
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        
        # Phase 1: Find potential candidates using voting
        cand1 = cand2 = None
        count1 = count2 = 0
        
        for num in arr:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify candidates
        result = []
        for c in [cand1, cand2]:
            if c is not None and arr.count(c) > n // 3:
                result.append(c)
        
        return sorted(result)
```

### Python (Optimized Verification)
```python
class Solution:
    def findMajority(self, arr):
        n = len(arr)
        
        # Phase 1: Voting
        cand1 = cand2 = None
        count1 = count2 = 0
        
        for num in arr:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Phase 2: Verify with single pass
        count1 = count2 = 0
        for num in arr:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        
        result = []
        threshold = n // 3
        if count1 > threshold:
            result.append(cand1)
        if count2 > threshold:
            result.append(cand2)
        
        return sorted(result)
```
---

## ⚡ Complexity Analysis

### Time Complexity: **O(n)**
```
Phase 1: Voting
- Single pass through array: O(n)
- Each operation is O(1)

Phase 2: Verification
- Count occurrences: O(n) for each candidate
- At most 2 candidates: 2 × O(n) = O(n)

Sorting result:
- At most 2 elements: O(2 log 2) = O(1)

Total: O(n) + O(n) + O(1) = O(n)
```

**Why O(n)?**
- Two passes through array (voting + verification)
- Constant time operations per element
- Result has at most 2 elements (constant sort time)

### Space Complexity: **O(1)**
```
Variables used:
- cand1, cand2: 2 variables
- count1, count2: 2 variables
- result: At most 2 elements (output, not counted)

Total: O(1) constant space
```

**Why O(1)?**
- Only fixed number of variables
- No extra data structures
- Result array size bounded by 2

### Comparison with Alternative Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| **Boyer-Moore** ⭐ | O(n) | O(1) | Optimal |
| HashMap frequency | O(n) | O(n) | Simple but uses space |
| Sorting + count | O(n log n) | O(1) | Slower |
| Brute force | O(n²) | O(1) | Very slow |

---

## 🔍 Detailed Dry Run

### Input Array
```
arr = [2, 2, 3, 1, 3, 2, 1, 1]
n = 8
threshold = n/3 = 8/3 = 2 (floor)
```

### Initial State
```
cand1 = None
cand2 = None
count1 = 0
count2 = 0
```

---

## 🎬 Phase 1: Voting Process

### **Iteration 0: num = 2**
```
num = 2
cand1 = None, count1 = 0
cand2 = None, count2 = 0

Check conditions:
1. num == cand1? → 2 == None? → False
2. num == cand2? → 2 == None? → False
3. count1 == 0? → 0 == 0? → True ✅

Action: Set cand1 = 2, count1 = 1

State after:
cand1 = 2, count1 = 1
cand2 = None, count2 = 0
```

---

### **Iteration 1: num = 2**
```
num = 2
cand1 = 2, count1 = 1
cand2 = None, count2 = 0

Check conditions:
1. num == cand1? → 2 == 2? → True ✅

Action: count1 += 1

State after:
cand1 = 2, count1 = 2
cand2 = None, count2 = 0
```

---

### **Iteration 2: num = 3**
```
num = 3
cand1 = 2, count1 = 2
cand2 = None, count2 = 0

Check conditions:
1. num == cand1? → 3 == 2? → False
2. num == cand2? → 3 == None? → False
3. count1 == 0? → 2 == 0? → False
4. count2 == 0? → 0 == 0? → True ✅

Action: Set cand2 = 3, count2 = 1

State after:
cand1 = 2, count1 = 2
cand2 = 3, count2 = 1
```

---

### **Iteration 3: num = 1**
```
num = 1
cand1 = 2, count1 = 2
cand2 = 3, count2 = 1

Check conditions:
1. num == cand1? → 1 == 2? → False
2. num == cand2? → 1 == 3? → False
3. count1 == 0? → 2 == 0? → False
4. count2 == 0? → 1 == 0? → False
5. Else → Decrement both ✅

Action: count1 -= 1, count2 -= 1

State after:
cand1 = 2, count1 = 1
cand2 = 3, count2 = 0

Meaning: Vote cancelled out
```

---

### **Iteration 4: num = 3**
```
num = 3
cand1 = 2, count1 = 1
cand2 = 3, count2 = 0

Check conditions:
1. num == cand1? → 3 == 2? → False
2. num == cand2? → 3 == 3? → True ✅

Action: count2 += 1

State after:
cand1 = 2, count1 = 1
cand2 = 3, count2 = 1
```

---

### **Iteration 5: num = 2**
```
num = 2
cand1 = 2, count1 = 1
cand2 = 3, count2 = 1

Check conditions:
1. num == cand1? → 2 == 2? → True ✅

Action: count1 += 1

State after:
cand1 = 2, count1 = 2
cand2 = 3, count2 = 1
```

---

### **Iteration 6: num = 1**
```
num = 1
cand1 = 2, count1 = 2
cand2 = 3, count2 = 1

Check conditions:
1. num == cand1? → 1 == 2? → False
2. num == cand2? → 1 == 3? → False
3. count1 == 0? → 2 == 0? → False
4. count2 == 0? → 1 == 0? → False
5. Else → Decrement both ✅

Action: count1 -= 1, count2 -= 1

State after:
cand1 = 2, count1 = 1
cand2 = 3, count2 = 0
```

---

### **Iteration 7: num = 1**
```
num = 1
cand1 = 2, count1 = 1
cand2 = 3, count2 = 0

Check conditions:
1. num == cand1? → 1 == 2? → False
2. num == cand2? → 1 == 3? → False
3. count1 == 0? → 1 == 0? → False
4. count2 == 0? → 0 == 0? → True ✅

Action: Set cand2 = 1, count2 = 1

State after:
cand1 = 2, count1 = 1
cand2 = 1, count2 = 1
```

---

### **Phase 1 Complete**
```
Final candidates:
cand1 = 2
cand2 = 1
```

---

## 🎬 Phase 2: Verification

### Count Actual Occurrences
```
Array: [2, 2, 3, 1, 3, 2, 1, 1]

Count occurrences of cand1 (2):
Positions: 0, 1, 5
Count: 3

Count occurrences of cand2 (1):
Positions: 3, 6, 7
Count: 3

Threshold: n/3 = 8/3 = 2
```

### Verify Against Threshold
```
cand1 = 2:
count = 3
3 > 2? → True ✅
Add to result: [2]

cand2 = 1:
count = 3
3 > 2? → True ✅
Add to result: [2, 1]
```

### Sort Result
```
Before: [2, 1]
After:  [1, 2]
```

---

### Final Result
```
result = [1, 2]
```

✅ **Both elements appear more than n/3 times!**

---

## 📊 Detailed Step Table

| Iteration | num | cand1 | count1 | cand2 | count2 | Action |
|-----------|-----|-------|--------|-------|--------|--------|
| 0 | 2 | None | 0 | None | 0 | Set cand1=2 |
| 1 | 2 | 2 | 1 | None | 0 | count1++ |
| 2 | 3 | 2 | 2 | None | 0 | Set cand2=3 |
| 3 | 1 | 2 | 2 | 3 | 1 | Both-- |
| 4 | 3 | 2 | 1 | 3 | 0 | count2++ |
| 5 | 2 | 2 | 1 | 3 | 1 | count1++ |
| 6 | 1 | 2 | 2 | 3 | 1 | Both-- |
| 7 | 1 | 2 | 1 | 3 | 0 | Set cand2=1 |

**After Phase 1**: cand1=2, cand2=1

**Verification**:
- Count(2) = 3 > 2 ✅
- Count(1) = 3 > 2 ✅

**Result**: [1, 2]

---

## 🎨 Visual Representation

### Voting Process Visualization
```
Array: [2, 2, 3, 1, 3, 2, 1, 1]

Step 0: [2]
        cand1=2(1), cand2=None(0)

Step 1: [2, 2]
        cand1=2(2), cand2=None(0)

Step 2: [2, 2, 3]
        cand1=2(2), cand2=3(1)

Step 3: [2, 2, 3, 1]  ← Cancel votes!
        cand1=2(1), cand2=3(0)
        
Step 4: [2, 2, 3, 1, 3]
        cand1=2(1), cand2=3(1)

Step 5: [2, 2, 3, 1, 3, 2]
        cand1=2(2), cand2=3(1)

Step 6: [2, 2, 3, 1, 3, 2, 1]  ← Cancel votes!
        cand1=2(1), cand2=3(0)

Step 7: [2, 2, 3, 1, 3, 2, 1, 1]
        cand1=2(1), cand2=1(1)

Final Candidates: 2 and 1
Verify: Both appear 3 times (> 2)
Result: [1, 2] ✅
```

### Frequency Distribution
```
Element: 1   2   3
Count:   3   3   2
         ✅  ✅  ❌
         >2  >2  =2

Threshold = 2
Elements > threshold: 1, 2
```

---

## 🎯 Key Takeaways

### Core Concepts

1. **Boyer-Moore Extended**: Modified for n/3 instead of n/2
2. **At Most 2 Candidates**: Mathematical constraint
3. **Two-Phase Process**: Voting + Verification
4. **Voting Mechanism**: Increment match, decrement mismatch
5. **Verification Required**: Candidates are potential, not confirmed

### Memory Trick

> **"Two candidates, vote and verify - find the n/3 majority!"**

### Algorithm Pattern
```
Pattern: Modified Boyer-Moore Voting
Common in: Majority element problems, frequency analysis

Template:
1. Find k candidates (k = floor(n/(threshold+1)))
2. Vote using increment/decrement mechanism
3. Verify each candidate's actual count
4. Return those exceeding threshold
```

### When to Use This Approach

- ✅ Finding elements with frequency > n/k
- ✅ Space-optimal solution required
- ✅ Linear time needed
- ✅ Majority element variations

---

## ⚠️ Common Mistakes

### Mistake 1: Not Verifying Candidates
```python
# ❌ Wrong - Assuming candidates are always majority
def findMajority(arr):
    # ... voting phase ...
    return sorted([cand1, cand2])  # Wrong!

# Problem: Candidates are only POTENTIAL majorities
# Example: [1, 2, 3] → candidates might be 1 and 2
# But neither appears > 1 time (n/3 = 1)
```

**Correct:**
```python
# ✅ Correct - Always verify
result = []
for c in [cand1, cand2]:
    if c is not None and arr.count(c) > n // 3:
        result.append(c)
return sorted(result)
```

---

### Mistake 2: Wrong Order of Conditions
```python
# ❌ Wrong - Checking count==0 before matching
for num in arr:
    if count1 == 0:  # Wrong order!
        cand1 = num
        count1 = 1
    elif num == cand1:
        count1 += 1
    # ...

# Problem: Even if num matches cand1, we replace it!
```

**Correct:**
```python
# ✅ Correct - Check matches first
for num in arr:
    if num == cand1:
        count1 += 1
    elif num == cand2:
        count2 += 1
    elif count1 == 0:
        cand1 = num
        count1 = 1
    # ...
```

---

### Mistake 3: Not Handling None Values
```python
# ❌ Wrong - Comparing with None incorrectly
if num == cand1:  # Might match None!
    count1 += 1

# Problem: In Python, any value could be None
# This causes incorrect matching
```

**Correct:**
```python
# ✅ Correct - Check for None
if cand1 is not None and num == cand1:
    count1 += 1

# Or handle in verification:
for c in [cand1, cand2]:
    if c is not None and arr.count(c) > n // 3:
        result.append(c)
```

---

### Mistake 4: Wrong Threshold
```python
# ❌ Wrong - Using >= instead of >
if arr.count(c) >= n // 3:  # Wrong!
    result.append(c)

# Problem: We need STRICTLY greater than n/3
# Example: n=6, n//3=2
# Element appearing 2 times should NOT be included
```

**Correct:**
```python
# ✅ Correct - Strictly greater than
if arr.count(c) > n // 3:
    result.append(c)
```

---

### Mistake 5: Forgetting to Sort
```python
# ❌ Wrong - Not sorting result
def findMajority(arr):
    # ... voting and verification ...
    return result  # Might be unsorted!

# Problem: Problem requires sorted output
```

**Correct:**
```python
# ✅ Correct - Always sort before returning
return sorted(result)
```

---

## 🔗 Practice Problems

### Similar Problems on LeetCode

- [169. Majority Element](https://leetcode.com/problems/majority-element/) - Find element > n/2
- [229. Majority Element II](https://leetcode.com/problems/majority-element-ii/) - Exact same problem
- [1157. Online Majority Element In Subarray](https://leetcode.com/problems/online-majority-element-in-subarray/)
- [2404. Most Frequent Even Element](https://leetcode.com/problems/most-frequent-even-element/)

### GeeksforGeeks Problems

- [Majority Element](https://www.geeksforgeeks.org/majority-element/)
- [Majority Element II](https://www.geeksforgeeks.org/majority-element-ii/)
- [N/3 Repeat Number](https://www.geeksforgeeks.org/n3-repeat-number/)

---

## 📝 Interview Tips

### What Interviewers Look For

1. ✅ **Understanding of Boyer-Moore algorithm**
2. ✅ **Why at most 2 elements can exist**
3. ✅ **Importance of verification phase**
4. ✅ **Optimal O(n) time, O(1) space solution**
5. ✅ **Handling edge cases**

### Common Interview Questions

**Q: Why can at most 2 elements appear > n/3 times?**
```
A: If 3 elements each appeared > n/3 times, total would be:
3 × (n/3) = n elements just for those 3
But array has only n total elements!
Contradiction. Therefore, at most 2 elements possible.
```

**Q: Why do we need verification phase?**
```
A: Voting phase finds POTENTIAL candidates, not guaranteed.
Candidates survive the voting, but might not actually
appear > n/3 times. Verification confirms they do.
Example: [1, 2, 3] → candidates might be 1, 2
But neither appears > 1 time (n/3 = 1)
```

**Q: What if we want elements appearing > n/4 times?**
```
A: We'd need 3 candidates (since at most 3 elements can
appear > n/4 times). Same algorithm, just maintain
3 candidate-count pairs instead of 2.
General: For > n/k, need (k-1) candidates.
```

**Q: Time and space complexity?**
```
A: Time: O(n) - two passes (voting + verification)
Space: O(1) - only 4 variables (2 candidates, 2 counts)
Result array has at most 2 elements (constant)
```

**Q: Can you solve without verification phase?**
```
A: No, verification is essential. Voting gives potential
candidates, not confirmed majorities. Without
verification, we'd return incorrect results.
```
---

## 🎉 Congratulations!

You now completely understand the **Boyer-Moore Voting Algorithm for n/3 Majority**!

**Remember**: 
> "Two candidates, vote and verify - the key to finding n/3 majorities!" 🗳️✨

---

## 📄 License

This documentation is free to use for educational purposes.

---

**Last Updated**: January 2026  
**Version**: 1.0.0  
**Algorithm Difficulty**: Medium ⭐⭐  
**Topics**: Arrays, Voting Algorithm, Boyer-Moore, Frequency Analysis  
**Companies**: Google, Amazon, Microsoft, Facebook, Apple, Adobe

---

**Historical Note**:
> The Boyer-Moore majority vote algorithm was invented by Robert S. Boyer and J Strother Moore in 1981. This elegant algorithm solves a seemingly difficult problem with remarkable simplicity and efficiency.
