print("Welcome to my Calculator")
operator = input("Choose the operator from [+, -, *, /]: ")

if (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
    num1 = float(input("Enter a number one: "))
    num2 = float(input("Enter a number two: "))
    if (operator == "+"):
        sum = num1 + num2
        print("The 'Addition' of", num1, "and", num2, "is:", sum)
    elif (operator == "-"):
        sub = num1 + num2
        print("The 'Subtraction' of", num1, "and", num2, "is:", sub)
    elif (operator == "*"):
        mul = num1 * num2
        print("The 'Multiplication' of", num1, "and", num2, "is:", mul)
    elif (operator == "/"):
        div = num1 / num2
        print("The 'Division' of", num1, "and", num2, "is:", div)
else:
    print("The", operator, "is invalid")