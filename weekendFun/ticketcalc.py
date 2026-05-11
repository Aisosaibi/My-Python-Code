age = int(input("Enter age: "))

if age < 5:
    print("Free")
elif age < 12:
    print("$5")
elif age < 65:
    print("$12")
else:
    print("$8")
