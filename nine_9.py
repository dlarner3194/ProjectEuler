import math as math
import numpy as np

for a in range(3, 997):
    for b in range(a + 1, 998):
        for c in range(b + 1, 999):
            if math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
                #print(a, b, c)
                if a + b + c == 1000:
                    print(a, b, c)
                    print(a*b*c)
# a = 3
# b = 4
# c = 5 

# while a + b + c != 1000:
#     for a in range(3, 998):
#         for b in range(4, 999):
#             if a < b:
#                 c = math.sqrt(math.pow(a,2) + math.pow(b,2))

# print(np.prod(a,b,c))