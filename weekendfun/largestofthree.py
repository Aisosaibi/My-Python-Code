a = int(input("Input first integer: "))
b = int(input("Input second integer: "))
c = int(input("Input third integer: "))

#largest = (
#    a if a > b and a > c
#    else b if b > c
#    else c
#)

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print(largest)


