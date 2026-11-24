num = int (input('enter a number:'))
fact = 1
sum = 0
for i in range (1, num + 1):
    fact *=i
for k in range (1, num + 1):
    sum += k
if fact % sum == 0:
    div = fact / sum
    print(f' Factorial is {fact} ,Sum is  {sum}. {fact} is divisible by  {sum} = {div}')  

else:
    print(f' Factorial is {fact} ,Sum is  {sum}. {fact} is not divisible by  {sum}')