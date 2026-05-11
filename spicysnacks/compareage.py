"""
PSEUDOCODE:
Prompt user for father's age
Prompt user for child's age
Subtract child's age from father's age

If difference < 13:
    display check father's age
else if child's age is less than difference:
    difference - child's age = double_point
    display double_point years ago
else:
    child's age - difference = double_point
    display (son_age - double_point) years from now


Scribblings:
#print(
#    f"The father will be twice as old as his son {diff - son_age} from now."
#    if son_age < diff
#    else "The father is/will be twice as old as his son this year."
#    if son_age == diff
#    else f"The father was twice as old as his son {son_age - diff} years ago."
#)
"""


pater_age = int(input("Father's current age (years): "))
son_age = int(input("Son's current age (years): "))

diff = pater_age - son_age

if diff < 13:
    message = "Confirm father/son's age"
    print(message)

else:
    message = (
        f"The father will be twice as old as his {diff - son_age} years from now."
        if son_age < diff
        else (
            "The father is/will be twice as old as is son this year."
            if son_age == diff
            else f"The father was twice as old as his son {son_age - diff} years ago"
        )
    )

    print(message)


