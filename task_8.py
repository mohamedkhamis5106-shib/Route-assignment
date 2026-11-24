numbers = [1, 1, 2, 3, 3, 3, 4]

result = []

for num in numbers:
    if not any(num == item[0] for item in result):
        result.append((num, numbers.count(num)))

print(result)