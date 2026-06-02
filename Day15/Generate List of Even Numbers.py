def get_even_numbers(n):
    even_list = []
    
    # We use n + 1 so that the number 'n' is included in the check
    for i in range(0, n + 1, 2):
        even_list.append(i)
        
    return even_list

# Example Usage:
print(get_even_numbers(10))  # Output: [0, 2, 4, 6, 8, 10]
