print('Enter "e" to exit')
while True:
    num1 = input('Enter 1st operand: ')
    num2 = input('Enter 2nd operand: ')
    operator = input('Enter operator: ')
    if num1.isdigit() and num2.isdigit():
        if operator == '+':
            print(f'Ans: {int(num1) + int(num2)}\n')
        elif operator == '-':
            print(f'Ans: {int(num1) - int(num2)}\n')
        elif operator == '*':
            print(f'Ans: {int(num1) * int(num2)}\n')
        elif operator == '/':
            if int(num2) < 1:
                print('Divisor cannot be less than 1\n')
            else:
                print(f'Ans: {round(int(num1) / int(num2),2)}\n')
        else:
            print('incorrect operator\n')
    elif num1 == 'e' or num2 == 'e':
        break
    else:
        print('Please only enter digits\n')
