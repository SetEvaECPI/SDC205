from datetime import datetime

print("seteva7933 Spreadsheet Automation Menu")

menu_options = [
    "1. Open Spreadsheet",
    "2. Edit Spreadsheet",
    "3. Save Spreadsheet",
    "4. Exit Program"
]

for option in menu_options:
    print(option)

choice = input("Enter your option number: ")

if choice == "1" or choice == "2" or choice == "3" or choice == "4":
    print("\nYou selected option", choice)
    print("The time and date is", str(datetime.now()))
else:
    print("Error: Invalid choice selected.")