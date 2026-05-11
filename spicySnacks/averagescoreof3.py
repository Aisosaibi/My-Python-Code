"""
PSEUDOCODE:

Calculate the average of three scores and return grade

Loop thrice and prompt user for scores
Add scores together and sum in variable scores
Divide scores by 3

if scores <= 60:
    F
    if scores <= 70:
        D
        if scores <= 80:
            C
            if scores <= 90:
                B
                if scores <= 100:
                    A

"""
THRICE = 3;

for i in range(THRICE):
    scores = int(input("Enter scores: "))
    scores += scores

if scores < 60:
    print("Grade is F")
elif scores < 70:
    print("Grade is D")
elif scores < 80:
    print("Grade is C")
elif scores < 90:
    print("Grade is B")
elif scores <= 100:
    print("Grade is A")

