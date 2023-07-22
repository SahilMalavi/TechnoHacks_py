
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return ("Cannot divide by zero.")


def main():
    print("---------------------------------------------")
    print("\nWhat operation would you like to perform?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    try:
        operation =int(input("\nEnter your choice: "))
        if(operation<5):
            num1 = int(input("\nEnter the first number: "))
            num2 = int(input("Enter the second number: "))
            print()

            if operation == 1:
                print("•Result:",num1, "+", num2, "=", add(num1, num2))
            elif operation == 2:
                print("•Result:",num1, "-", num2, "=", subtract(num1, num2))
            elif operation == 3:
                print("•Result:",num1, "*", num2, "=", multiply(num1, num2))
            elif operation == 4:
                print("•Result:",num1, "/", num2, "=", divide(num1, num2))
            else:
                print("!Invalid operation.\n")
        else:
            print("Choice must be between 1 to 4\n")
            main()
    except:
        print("Please enter numeric values only...!\n")
        main()

while True:
    if __name__ == "__main__":
        main()
