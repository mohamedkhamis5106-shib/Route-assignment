numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
peak = []
print(len(numbers))
for i in range(1 , len(numbers)-1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        peak.append(numbers[i]) 
print("peak:", peak)