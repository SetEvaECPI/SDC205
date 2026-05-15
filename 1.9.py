name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

num1 = int(input("Enter the first whole number: "))
num2 = int(input("Enter the second whole number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("\nCalculation Results:")
print(f"Addition: {addition:.2f}")
print(f"Subtraction: {subtraction:.2f}")
print(f"Multiplication: {multiplication:.2f}")

if num1 > num2:
    print(f"\n{num1} is larger than {num2}.")
elif num1 < num2:
    print(f"\n{num1} is smaller than {num2}.")
else:
    print(f"\n{num1} and {num2} are equal.")

print("\nStudent Information:")
print(f"Name: {name}")
print(f"Student ID: {student_id}")