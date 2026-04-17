"""
Prompt user for password
Find out the length of password
If length is < 8: very weak 
Elif length is == 8: weak 
If length is > 8: weak 
If length is < 8: weak    
"""


password = input("Enter password: ")
password_length = len(password)

if password_length > 8:
    if password_length < 16:
        print("Strong password!")
    else:
        print("Very strong password!")

elif password_length < 8:
    print("Very weak password")

else:
    print("Weak password")
