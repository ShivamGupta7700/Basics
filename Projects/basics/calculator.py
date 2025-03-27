progm = True
while progm:
    print('''
    Welcome to "JUST A SIMPLE CALCULATOR"
    ''')
    a, b = map(int, input('Enter the numbers > ').split())

    print('''
    1---> Add
    2---> Subtract
    3---> Multiply
    4---> Divide
    5---> EXIT
    ''')

    user_input = int(input('Enter the operation you want to do:> '))

    if user_input == 1:
        print("Result:", a + b)
    elif user_input == 2:
        print("Result:", a - b)
    elif user_input == 3:
        print("Result:", a * b)
    elif user_input == 4:
        print("Result:", a / b if b != 0 else "Cannot divide by zero!")
    elif user_input == 5:
        progm = False
        print("Exiting calculator")
    else:
        print("Invalid input! Please enter a number between 1-5.")
