class Solution:
    def pushZerosToEnd(self, arr):
        
        n = len(arr)
        pos = 0   # Position to place next non-zero element
        
        # Step 1: Move non-zero elements to the front
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Step 2: Fill remaining positions with zero
        while pos < n:
            arr[pos] = 0
            pos += 1
