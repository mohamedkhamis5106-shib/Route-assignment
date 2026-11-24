data = {
    "A" : 1,
    "B": 2,
    "c":1
}
flipped = {}

for key, value in data.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)

print(flipped)