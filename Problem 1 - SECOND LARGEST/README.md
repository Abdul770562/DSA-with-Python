🧩 Problem Understanding


Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.


Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.



Explanation:
We are given an array of positive integers.

Our task is to:

Find the second largest element

The second largest must be different from the largest

If it does not exist, return -1

Example
Input:  [12, 35, 1, 10, 34, 1]
Largest = 35
Second Largest = 34
Output = 34

🚀 Goal of the Solution

We want to:

Avoid sorting (sorting is slower and unnecessary)

Scan the array only once

Keep track of:

the largest number

the second largest number

This gives us the most efficient solution.

🧠 Code (For Reference)
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

🔍 Step-by-Step Explanation
1️⃣ Function Definition
def getSecondLargest(self, arr):


This function receives:

arr → a list of integers

self is used because this method belongs to a class (required in platforms like GFG / LeetCode)

2️⃣ Checking Array Length
if len(arr) < 2:
    return -1

What does len(arr) do?

len() returns the number of elements in the list

Example:

len([5, 10, 20]) → 3
len([10]) → 1

Why this check?

To have a second largest, we need at least 2 elements

If not, the answer is impossible → return -1

3️⃣ Initializing Variables
largest = -1
second_largest = -1


These variables store:

largest → the biggest number found so far

second_largest → the second biggest number found so far

Since the array contains positive integers, starting with -1 is safe.

4️⃣ Looping Through the Array
for num in arr:

What this loop does:

Goes one by one through every element in the array

num represents the current element

Example:

arr = [12, 35, 1]
num = 12 → then 35 → then 1

5️⃣ Updating Largest and Second Largest
Case 1: New Largest Found
if num > largest:
    second_largest = largest
    largest = num


What’s happening here?

If the current number is greater than the existing largest

The old largest becomes the second largest

The current number becomes the new largest

Example:

largest = 20
num = 35

second_largest = 20
largest = 35

Case 2: Possible Second Largest
elif num != largest and num >= second_largest:
    second_largest = num


This condition ensures:

We ignore duplicates of the largest

We only update second_largest if:

num is smaller than largest

but larger than the current second_largest

Example:

largest = 35
second_largest = 12
num = 34 → valid second largest

6️⃣ Final Result
return second_largest


After the loop finishes

second_largest contains the answer

If no valid second largest was found → it remains -1

⏱️ Time & Space Complexity
Metric	Value
Time Complexity	O(n) (single loop)
Space Complexity	O(1) (no extra memory)


From GFG - 360