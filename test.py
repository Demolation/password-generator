import math

def total_sqrt():
    print("The square root of the sum of the number is ", round(float(math.sqrt(a + b))) )
    print()
    

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

print(f"The sum of all of them is  {sum:.2f}")
print(f"The multiplication of all the numbers is {multiple:.2f}")
print(f"The division of all numbers is {division:.4f}")
total_sqrt()

print()

