while True:

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        print(f"{num1} + {num2} = {num1 + num2}")
        break
    except ValueError:
        print("Invalid")