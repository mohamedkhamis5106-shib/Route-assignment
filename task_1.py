word = str(input("Enter a word: "))
string =[]
nums = []
for i in word:
    if i.isalpha():
        string.append(i)
    elif i.isdigit():
        nums.append(i)
new_string = ''.join(string)
sum_nums = sum(int(i) for i in nums)
print(new_string)
print(sum_nums)
