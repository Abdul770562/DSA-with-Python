class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  #handle large array size d>n, and also it have no efect 
                   #if the d < n

        def reverse(l, r):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        # Step 1
        reverse(0, d - 1)

        # Step 2
        reverse(d, n - 1)

        # Step 3
        reverse(0, n - 1)
