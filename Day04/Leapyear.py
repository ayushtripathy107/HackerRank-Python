def is_leap(year):
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if it's a century year
        if year % 100 == 0:
            # Century years must be divisible by 400
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            # Not a century year, but divisible by 4
            leap = True
    else:
        # Not divisible by 4
        leap = False
        
    return leap
    leap = False
    
    # Write your logic here
    return leap
