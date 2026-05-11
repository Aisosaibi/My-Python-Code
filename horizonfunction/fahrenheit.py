"""
PSEUDOCODE:

Convert temperature to the opposite unit

Prompt user for temperature
// Prompt user for unit?
Find the unit in string ()

prompt user to set threshold
find the unit in the string
represent threshold in both units

validate the input (via len)

if F, then
C = (F -32) * 5/9
if C, then
F = (C * 9/5) + 32

if temperature is below relevant threshold:
    return "Cold advisory"
if temperature >= relevant threshold
    return "Heat alert"

"""

def converttemp():
    user_temp = input("Enter temperature [°C or °F] (e.g. 10 C): ")
    threshold = input("Set threshold [°C or °F] (e.g. 30 C): ")

    if len(user_temp.split()) != 2:
        return "Invalid temperature input! Use format: 10 C"
    if len(threshold.split()) != 2:
        return "Invalid threshold input! Use format: 30 F"

    value_user, unit_user = user_temp.split()
    value_user = float(value_user)
    unit_user = unit_user.upper()

    value_threshold, unit_threshold = threshold.split()
    value_threshold = float(value_threshold)
    unit_threshold = unit_threshold.upper()

    if unit_user == "F":
        value_user = (value_user - 32) * 5/9
    elif unit_user == "C":
        pass  # already in Celsius
    else:
        return "Invalid unit for temperature!"

    if unit_threshold == "F":
        value_threshold = (value_threshold - 32) * 5/9
    elif unit_threshold == "C":
        pass  # already in Celsius
    else:
        return "Invalid unit for threshold!"

    # Now compare
    if value_user < value_threshold:
        return "Cold advisory"
    else:
        return "Heat alert"

print(converttemp())
