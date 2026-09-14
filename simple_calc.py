choice = input("Choose operator (+/-/*/): ")

if choice in ('+', '-', '*', '/'):
    num1 = float(input('First Number: '))
    num2 = float(input('Second Number: '))

    if choice == '+':
        print(num1, '+', num2, '=', num1 + num2)
    elif choice == '-':
        print(num1, '-', num2, '=', num1 - num2)
    elif choice == '*':
        print(num1, '*', num2, '=', num1 * num2)
    elif choice == '/':
        if num2 == 0:
            print('Cannot divide by zero')
        else:
            print(num1, '/', num2, '=', num1 / num2)
else:
    print('Invalid operator')