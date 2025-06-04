num1 = float(input("Enter the first number: "))
... num2 = float(input("Enter the second number: "))
... operators = input("Choose the operatiion to perform (+, -, *, /): ")
... match operators:
...     case "+":
...         result = num1 + num2
...         print(f"The result is {result}. ")
...     case "-":
...         result = num1 - num2
...         print(f"The result is {result}. ")
...     case "*":
...         result = num1 * num2
...         print(f"The result is {result}. ")
...     case "/":
...         if num2 != 0:
...             result =num1 / num2
...             print(f"The result is {result}. ")
...         else:
...             print("Error: Cannot divide by zero.")
...     case _:
...         print("Error: Invalid operation, please choose either of +, _, *, or /.")