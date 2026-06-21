class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Filter alphanumeric characters and convert to lowercase
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        
        # Check if the filtered list is the same forwards and backwards
        return filtered_chars == filtered_chars[::-1]
