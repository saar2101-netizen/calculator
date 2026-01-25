"""
ui
=====
Contains user interface
"""
# User interface

def get_number(prompt):
# getting user num
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("ERROR: Please enter a number!")


def show_menu():
# shoeing the menu
    print("\n ===MENU===")
    print("1. Add")
    print("2. subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square root")
    print("7. factorial")
    print("8. show constants")
    print("---Geometry---")
    print("9. circle area")
    print("10. rectangle area")
    print("11. triangle area")
    print("---History---")
    print("12. show history")
    print("13. clear history")
    print("14. save history")
    print("15. load history")
    print("0. Exit")
    return input("Enter your choice: ")
