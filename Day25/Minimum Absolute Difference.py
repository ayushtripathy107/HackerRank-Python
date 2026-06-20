class Solution(object):
    def minimumAbsDifference(self, arr):
        # 1. Sort the array
        arr.sort()
        
        # 2. Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff
        
        # 3. Collect all pairs with that minimum difference
        result = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result
