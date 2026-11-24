items = {
    'apple' : 0.5,
    'milk' : 1.5,
    'bread' : 2.0
}
cart = []
while True :
    action = input("Add , Remove , Done:").strip().lower()
    if action == 'done':
        break
    item = input("Enter item: ").strip().lower()

    if action == "add":
        if item in items:
            cart.append(item)
        else:
            print("Error: Item not found in store.")

    elif action == "remove":
        if item in cart:
            cart.remove(item)
        else:
            print("Item not in cart.")

total = 0

for item in cart:
    total += items[item]

print(f"Total Bill: ${total}")
