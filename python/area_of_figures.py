figure = str(input())
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c) / 2)
    s = (((p * (p - a) * (p - b) * (p - c))) ** 0.5)
    print(s)
elif figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(float(a * b))
else:
    s = float(3.14 * int(input()) ** 2)
    print(s)
