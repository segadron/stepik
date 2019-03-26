n = int(input())
if (n % 10 == 0 or 5 <= n % 10 <= 9) or 11 <= n % 100 <= 19:
    print('{0} программистов'.format(n))
elif n % 10 in [2, 3, 4]:
    print('{0} программиста'.format(n))
else:
    print('{0} программист'.format(n))
