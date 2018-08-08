# Problem 1
# all natural numebers 1-infinty 
# Find the sum of all the multiples of 3 or 5 below 1000.

import array

# first answer
arr = []

for i in xrange(1000):
    if i % 3 == 0 or i % 5 == 0:
        arr.append(i)

print(sum(arr))

print sum(number for number in xrange(1000) if not (number % 3 and number % 5))