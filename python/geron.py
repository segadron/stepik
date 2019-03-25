import math

a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) // 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(S)
