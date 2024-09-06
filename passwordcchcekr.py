def has_digit(test_string):
    digits = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")  # List of digits
    
    # Step 2: Move digit checking logic into the function
    for char in test_string:
        if char in digits:
            return True  # Return True if any digit is found
    
    return False  # Return False if no digit is found

# Step 4: Call the function
test = input("Please enter a password: ")

# Step 5: Use the function result to make decisions
if has_digit(test):
    print("Password contains at least one digit.")
else:
    print("Password does not contain any digits.")