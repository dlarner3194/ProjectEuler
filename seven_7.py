numArr = []

for num in range(1, 105001):
    if all(num % i != 0 for i in range(2,num)):
       numArr.append(num)
       print(numArr)

print(numArr[10001])