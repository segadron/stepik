a, b= int(input()), int(input())
d = a * b
while a and b:
    if a > b:
        a = a % b
    else:
        b = b % a
print(int(d / (a + b)))
