class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            # If character is already in the window, move the start pointer
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            
            # Update the last seen index of the character
            char_map[s[end]] = end
            # Calculate the window size and update max_length
            max_length = max(max_length, end - start + 1)
            
        return max_length
