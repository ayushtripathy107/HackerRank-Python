def merge_the_tools(string, k):
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        # Extract the substring t_i
        substring = string[i : i + k]
        
        # Remove duplicates while maintaining order
        # dict.fromkeys() preserves insertion order in Python 3.7+
        u = "".join(dict.fromkeys(substring))
        
        # Print the result for this chunk
        print(u)

# Example usage:
# merge_the_tools("AAABCA DDE", 3)
