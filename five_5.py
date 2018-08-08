# tell is a number is div by 1 to 20
def isDiv(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True
# starting number 1, check if div by 1 to 20
num = 1
while True:
    if isDiv(num):
        break
    num += 1 # increment number

# if found, stop
print(num)