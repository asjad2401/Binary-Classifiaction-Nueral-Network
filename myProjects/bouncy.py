def is_increasing(number):
    return str(number) == ''.join(sorted(str(number)))

def is_decreasing(number):
    return str(number) == ''.join(sorted(str(number), reverse=True))

def is_neither_increasing_nor_decreasing(number):
    return not is_increasing(number) and not is_decreasing(number)

count = 0
for num in range(1000, 10000):
    if is_neither_increasing_nor_decreasing(num):
        count += 1

print(f"Count of 4-digit numbers that are neither increasing nor decreasing: {count}")
