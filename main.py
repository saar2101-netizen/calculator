from operations import add, subtract, multiply, divide
from advanced import power, square_root, factorial
from ui import get_number,show_menu
from history import add_to_history, show_history, clear_history


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
                result = add(num1, num2)
                print(f"The result is {result}")
                add_to_history(f"{num1} + {num2}", result)
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"The result is {result}")
                add_to_history(f"{num1} - {num2}", result)
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"The result is {result}")
                add_to_history(f"{num1} * {num2}", result)
            elif choice == "4":
                result = divide(num1, num2)
                print(f"The result is {result}")
                add_to_history(f"{num1} / {num2}", result)
            elif choice == "5":
                result = power(num1, num2)
                print(f"The result is {result}")
                add_to_history(f"{num1} ** {num2}", result)

        elif choice == "6":
            num = get_number("Please enter the number: ")
            result = square_root(num)
            print(f"The result is {result}")
            add_to_history(f"{num} ** 0.5", result)

        elif choice == "7":
            num = get_number("Please enter a number: ")
            print(f"The result is {factorial(num)}")
            add_to_history(f"{num}", factorial(num))

        elif choice == "8":
            show_history()

        elif choice == "9":
            clear_history()

        else:
            print("ERROR: choice not valid!")

if __name__ == "__main__":
    main()