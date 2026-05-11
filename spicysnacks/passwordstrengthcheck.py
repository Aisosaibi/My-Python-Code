"""
PSEUDOCODE:
Collect user input (password) and check strength

Prompt user for input (password)
Determine length of inputs (password_len)
if password_len < 1:
    Display "Invalid"
elif password_len < 6:
    Display "Weak"
elif password_len <= 10:
    Display "Medium"
else:
    Display "Strong" 
"""

password = input("Set your password: ")

password_len = len(password)

if password_len < 1:
    print("Invalid password")
elif password_len < 6:
    print("Weak password")
elif password_len <= 10:
    print("Medium password")
else:
    print("Strong password") 
