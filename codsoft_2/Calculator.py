def calculator():g
    number1 = float(input("Enter number 1: "))
    number2 = float(input("Enter number 2: "))

    print()

    print("Select the operations from the following options:")
    print()
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Power(**)")
    print("6. Percentage(%)")

    print()

    operation = input("Enter the opearation[1, 2, 3, 4, 5, 6]: ")

    print()

    if operation == "1":
        result1 = number1 + number2
        print(f"Addition of Number 1 and Number 2: ", {result1})
    elif operation == "2":
        result2 = number1 - number2
        print(f"Subratction of Number 1 and Number 2: ", {result2})
    elif operation == "3":
        result3 = number1 * number2
        print(f"Multiplication of Number 1 and Number 2: ", {result3})
    elif operation == "4":
        if number2 == 0:
            print("Not Defined")
        else:
            result4 = number1 / number2
            print(f"Division of Number 1 and Number 2: ", {result4})
    elif operation == "5":
        result5 = number1 ** number2
        print(f"Number 2 as power of Number 1: ", {result5})
    elif operation == "6":
        if number2 == 0:
            print("not defined")
        else:
            result6 = (number1 / number2) * 100
        print(f"Percentage: ", {result6},"%")
    else:
        print("Enter a valid operation")
    

calculator()

print()




  