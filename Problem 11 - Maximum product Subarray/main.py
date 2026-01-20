class Solution:
    def maxProduct(self, arr):
        n = len(arr)

        max_end = arr[0]
        min_end = arr[0]
        result = arr[0]

        for i in range(1, n):
            x = arr[i]

            temp = max_end  

            max_end = max(x, x * max_end, x * min_end)
            min_end = min(x, x * temp, x * min_end)

            result = max(result, max_end)

        return result
