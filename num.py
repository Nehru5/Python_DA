# num1 = [1,2,3]
# num2 = [4,5,6]
# result = []
# for i in range(len(num1)):
#   result.append(num1[i]+num2[i])
  
# print(result)

# import numpy as np

# num1 = np.array([1,2,3])
# num2 = np.array([4,5,6])
# print(num1+num2)

import time

num1 = list(range(1000000))
num2 = list(range(1000000))
start = time.time()
result1 = []

for i in range(len(num1)):
  result1.append(num1[i]+num2[i])
  
end = time.time()
print(end-start)


import numpy

num3 = list(range(1000000))
num4 = list(range(1000000))

start = time.time()
result2 = num3+num4
end = time.time()
print(end-start)

