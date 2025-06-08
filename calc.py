number1 = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /, ** , //): ")
number2 = int(input("Enter second number: "))
equation = f"{number1} {operation} {number2}"
print(f"{number1} {operation} {number2} = {eval(equation)}")