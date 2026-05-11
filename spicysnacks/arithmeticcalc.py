"""
PSEUDOCODE:
Get user's inputs (number)
Get user's operator (user_input)
Match user_input with the various arithmetic operations
Display results
"""

number_one = int(input("Enter number: "))
number_two = int(input("Enter number: "))
user_input = input("Enter operator (+,-,*,/): ")

match user_input:
    case "+":
        result = number_one + number_two
    case "-":
        result = number_one - number_two
    case "*":
        result = number_one * number_two
    case "/":
        result = number_one / number_two
    case _:
        result = "Invalid operator"

print(result)



