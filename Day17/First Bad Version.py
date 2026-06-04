class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        
        while left < right:
            # Calculate mid point to avoid potential overflow
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # This could be the first bad version, 
                # so we look at everything before it (including mid)
                right = mid
            else:
                # This version is good, so the first bad one is after mid
                left = mid + 1
        
        # When left == right, we've found the first bad version
        return left
