class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        currSum = 0
        
        maxSum = float('-inf')
        
        for num in range(len(arr)):
            currSum += arr[num]
            maxSum = max(currSum, maxSum)
            
            if currSum < 0:
                currSum = 0
                
                
        return maxSum