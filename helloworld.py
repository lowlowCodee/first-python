print("1. addition\n2. multiplication\n3. subtraction\n4. division")
operator = input("Choose an operator to do: ")
if int(operator) < 1 or int(operator) > 4:
    print("invalid operator")
else:
    
    num1 = input("Enter first number: ")

    num2 = input("Enter second number: ")

    result = 0


    
if int(operator) == 1:
    result = int(num1) + int(num2)
    print("The answer is: ", result)
elif int(operator) == 2: 
    result = float(num1) * float(num2)
    print("The answer is: ", result)
elif int(operator) == 3:
    result = int(num1) - int(num2)
    print("The answer is: ", result)
elif int(operator) == 4:
    if int(num2) == 0:
        print("cannot divide by zero!")
    else:
        result = int(num1) / int(num2)
        print("The answer is: ", result)



    