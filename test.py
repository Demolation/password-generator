a=input("Enter the first number: ")
b=input("Enter the second number: ")
print()
a=float(a)
b=float(b)

if a > b:
    print("The first number is greater than the second number.")
elif a == b:
    print("The first number is the same as the second number.")
else:
    print("The second number is greater than the first number.")

print()

sum=float(a + b)
multiple=float(a * b)
division=float(a/b)

print("The sum of all of them is ", sum)
print("The multiplication of all the numbers is ", multiple)
print("The division of all numbers is ", division)
print()

