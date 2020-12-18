import math
with open ('input.txt') as f:
    data = f.readlines()
    data = [int(i.strip()) for i in data ]

def get_calculation(n):
     return math.floor((n/3)) - 2

summations = []

for i in data:
    summations.append(get_calculation(i))

print(sum(summations))

