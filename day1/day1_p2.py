with open ('input.txt') as f:
    data = f.readlines()
    data = [int(i.strip()) for i in data ]

def get_calculation(n):
    return max((n//3) - 2, 0)

def compute():
    total = 0
    for num in data:
        prev = int(num)
        while prev > 0:
            prev = get_calculation(prev)
            total += prev

    return total

print(compute())
