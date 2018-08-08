# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?
# check = True
# num = 600851475143
# small_div = 2

# while check:
#     while num % small_div == 0:
#         largest_factor = num / small_div
#         check = False 
#         i =largest_factor
#         while i in range(2, largest_factor):
#             if largest_factor % i == 0:
#                 check = True
#         small_div += 1
#     else:
#         small_div += 1

# print(largest_factor)

def find_prime(n, factor):
    i = factor
    while i * i < n:
        while n % i == 0:
            n = n / i
        i += 1
    return n

print(find_prime(36, 2))