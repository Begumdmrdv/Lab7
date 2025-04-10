import math_utils

def main():
    try:
        x = float(input("Please, enter the first number: "))
        y = float(input("Please, enter the second number: "))
        operator = input("Please, enter an operator (+, -, *, /, **, %): ").strip()

        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod
        }

        if operator in operations:
            result = operations[operator](x, y)
            print(f"Result: {result}")
        else:
            print("Error: Invalid operator.")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run
if __name__ == "__main__":
    main()
