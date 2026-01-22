class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
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