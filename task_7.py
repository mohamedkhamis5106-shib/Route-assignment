digit = input("Enter a multi-digit number: ")
while len(digit) > 1:
    total = 0
    
    for num in digit:
        total += int(num)

    digit = str(total)

print("Digital Root:", digit)

    

