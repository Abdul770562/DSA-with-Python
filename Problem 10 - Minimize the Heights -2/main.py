class Solution:
    def getMinDiff(self, arr, k):
        # code here
        
        n = len(arr)
        
        if n==1:
            return 0
        
        arr.sort()
        
        result = arr[n-1] - arr[0]
        
        
        small = arr[0] + k
        large = arr[n-1] - k 
        
        
        for i in range(1,n):
            
            if arr[i] - k < 0:
                continue
            
            minimum = min(small, arr[i] - k)
            maximum = max(large, arr[i-1] + k)
            
            result = min(result, maximum-minimum)
            
        return result