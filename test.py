def add(n1, n2):
    return  n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1/n2

print("Please select the operation below\n" \
"1. Addition\n" \
"2. Subtraction\n" \
"3. Multiplication\n" \
"4. Divisions")
print("")



operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", sub),
    "3": ("Multiplication", mul),
    "4": ("Division", div)
}

sel = input("Please choose a number (1-4):")

n1 = float(input("Please input the first number: "))
n2 = float(input("Please input the second number: "))

for key in operations:
    if sel == key:
        name, func = operations[key]
        print(f"Your operation is {name}")
        print("Result:", func(n1, n2))
        break
else:
    print("Invalid choice")
