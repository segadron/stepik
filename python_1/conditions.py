A = int(input())
B = int(input())
H = int(input())
if H < A:
    print('Недосып')
elif H <= B:
    print('Это нормально')
else:
    print('Пересып')