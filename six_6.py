import math

sum = 0

for n in range(1, 101):
    x = n * n
    sum += x
print(sum)

otherSum = 0

for i in range(1, 101):
    otherSum += i
squaredSum = math.pow(otherSum, 2)

print(squaredSum)

print(squaredSum - sum)