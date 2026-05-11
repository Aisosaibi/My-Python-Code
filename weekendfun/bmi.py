weight = input("Enter weight: ")
height = input("Enter height: ")

bmi = weight/(height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9
    print("Overweight")
else:
    print("Obese")
