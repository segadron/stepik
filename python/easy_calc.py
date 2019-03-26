a = float(input())
b = float(input())
operation = str(input())
if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '/' and b != 0:
    print(a / b)
elif operation == '*':
    print(a * b)
elif operation == 'mod' and b != 0:
    print(a % b)
elif operation == 'pow':
    print(pow(a, b))
elif operation == 'div' and b != 0:
    print(a // b)
else:
    print('Деление на 0!')
