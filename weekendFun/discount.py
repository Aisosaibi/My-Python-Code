total_bill = int(input("Enter total bill: "))
is_member = input("Is a member (yes/no): ").strip().lower()

if total_bill >= 1000 and is_member == "yes":
    total_bill *= 0.9
    print(f"Total bill is {total_bill}; 10% discount")
elif total_bill >= 1000 and is_member == "no":
    total_bill *= 0.95
    print(f"Total bill is {total_bill}; 5% discount")
else:
    print(f"Total bill is {total_bill}; no discount")
