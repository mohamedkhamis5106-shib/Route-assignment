total = int(input("Enter the total price: "))
member = input("Are you a member? (yes/no): ").strip().lower()
final_price = total
final_price2 = total
if total == 50:
    print ("no discount applied")
elif total > 50 and total <= 100:
    discount = total * 0.10
    final_price = float(total - discount)
    
elif total > 100:
    discount = total * 0.20
    final_price = float(total - discount)
    

if member == "yes":
    discount2 = final_price * 0.05
    final_price2 = float(final_price - discount2)

if member == "no":
    final_price2 = float(final_price)

print(f"Final total: {final_price2:.2f} (note: total {total:.2f} - {discount:.2f}% = {final_price:.2f} ; then {final_price:.2f} - {discount2:.2f}% = {final_price2:.2f})")