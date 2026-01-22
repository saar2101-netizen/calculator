from operations import add, subtract, multiply, divide
from advanced import power, square_root, factorial
from ui import get_number,show_menu


print("Welcome to calculator")
print("==============================")

def main():
    while True:
        choice = show_menu()

        if choice == "0":
            print("Good bye")
            break

        if choice in ["1","2","3","4","5"]:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == "1":
                print(f"The result is {add(num1, num2)}")
            elif choice == "2":
                print(f"The result is {subtract(num1, num2)}")
            elif choice == "3":
                print(f"The result is {multiply(num1, num2)}")
            elif choice == "4":
                print(f"The result is {divide(num1, num2)}")
            elif choice == "5":
                print(f"The result is {power(num1, num2)}")

        elif choice == "6":
            num = get_number("Please enter the number: ")
            print(f"The result is {square_root(num)}")

        elif choice == "7":
            num = get_number("Please enter a number: ")
            print(f"The result is {factorial(num)}")

        else:
            print("ERROR: choice not valid!")

if __name__ == "__main__":
    main()