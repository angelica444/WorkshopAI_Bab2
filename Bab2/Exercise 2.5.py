import math

s = input("Input a list of float numbers: ")
numbers = list(map(float, s.split()))

for num in numbers:
    sin_val = math.sin(num)
    print(sin_val)