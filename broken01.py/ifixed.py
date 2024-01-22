from typing import Union
#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1: Union[float, str] = 0.0
calc2: Union[float, str] = 0.0
operation: str = ""
while calc1 != "q" and calc1 != "Q":
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    if calc1 == "q" or calc1 == "Q":
        break
    try:
        calc1 = float(calc1)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2 == "q" or calc2 == "Q":
        break
    try:
        calc2 = float(calc2)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
