count_pass = 0
count_fail = 0
n = 15

for i in range (15):
    score = int(input("Enter score: "))
    if score > 45:
        count_pass += 1
    else:
        count_fail += 1

print(f"{count_pass} students passed, while {count_fail} students failed")
