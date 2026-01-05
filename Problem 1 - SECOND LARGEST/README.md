# Find the Second Largest Element in an Array

Given an array of positive integers `arr[]`, return the second largest element from the array. If the second largest element doesn't exist then return `-1`.

Note: The second largest element must be different from the largest element.

## Examples

- Input: `arr = [12, 35, 1, 10, 34, 1]`  
  Output: `34`  
  Explanation: The largest element is `35` and the second largest element is `34`.

- Input: `arr = [10, 5, 10]`  
  Output: `5`  
  Explanation: The largest element is `10` and the second largest element is `5`.

- Input: `arr = [10, 10, 10]`  
  Output: `-1`  
  Explanation: All elements are equal to `10`, so a second largest (different) element does not exist.

---

## Goal

- Avoid sorting (which is unnecessary and slower).
- Scan the array only once (single pass).
- Keep track of:
  - the largest number found so far
  - the second largest number found so far

This yields an efficient solution: O(n) time and O(1) extra space.

---

## Python Solution

```python
class Solution:
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1

        largest = -1
        second_largest = -1

        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num != largest and num >= second_largest:
                second_largest = num

        return second_largest
```

---

## Step-by-step Explanation

1. Function definition:
   - `def getSecondLargest(self, arr):`
   - `arr` is the list of integers. `self` is present because this is written as a class method (typical for platforms like GFG/LeetCode).

2. Check array length:
   - If `len(arr) < 2`, return `-1` because a second largest value cannot exist.

3. Initialize:
   - `largest = -1`
   - `second_largest = -1`
   - Using `-1` is safe because the input is positive integers.

4. Loop through the array:
   - For every number `num` in `arr`:
     - If `num > largest`:
       - Update `second_largest = largest` (old largest becomes the second largest)
       - Update `largest = num`
     - Else if `num != largest and num >= second_largest`:
       - Update `second_largest = num` (consider as a candidate for second largest while ignoring duplicates of the largest)

5. Return result:
   - After the loop, return `second_largest`.
   - If no valid second largest was found, it remains `-1`.

---

## Complexity

| Metric          | Value              |
|-----------------|--------------------|
| Time Complexity | O(n) — single pass |
| Space Complexity| O(1) — constant    |

---

Source: From GFG - 360
