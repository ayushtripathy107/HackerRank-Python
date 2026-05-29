def mask_password(password):
    password_length = len(password)
    return "*" * password_length

# Example Usage:
print(mask_password("secret123"))  # Output: *********
print(mask_password("AbC!"))       # Output: **** 
