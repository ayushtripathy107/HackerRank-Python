class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split() without arguments splits by any whitespace 
        # and discards empty strings from the result.
        words = s.split()
        
        if not words:
            return 0
            
        return len(words[-1])
