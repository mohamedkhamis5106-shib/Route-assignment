string = input("Enter Your string: ").strip().lower()
v = "aeiou"
vowels = {}
for i in range(len(string)):
    char = string[i]
    if char in v:
        if char not in vowels:
            vowels[char] = [i]
        else:
            vowels[char].append(i)
print(vowels)