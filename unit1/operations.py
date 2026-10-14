def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

print("-----MENU-----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Please select the choice (1-4):"))
num1 = int(input("Please enter the first number:"))
num2 = int(input("Please enter the second number:"))

if choice == 1:
    print("Addition = ",addition(num1 , num2))

elif choice == 2:
    print("Subtraction = ",subtraction(num1 , num2))

elif choice == 3:
    print("Multiplication = ",multiplication(num1 , num2))

elif choice == 4:
    if (num2 != 0):
        print("Division = ",division(num1 , num2))
    else:
        print("Cannot divided by zero")

else:
    print("Invalid choice")