class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
            
        # The max value of a single subarray is the range of the whole array
        max_val = max(nums)
        min_val = min(nums)
        
        single_max_diff = max_val - min_val
        
        # Since we can pick the same subarray k times, we just multiply
        return single_max_diff * k
