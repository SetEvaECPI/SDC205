from datetime import datetime

print("seteva7933 Spreadsheet Automation Menu")
print("1. Open Spreadsheet")
print("2. Edit Spreadsheet")
print("3. Save Spreadsheet")
print("4. Exit Program")

# The next line retrieves the inputted option and stores into the variable called option.
option = input("Enter your option number: ")

print("\nYou selected option", option)
print("The time and date is", str(datetime.now()))