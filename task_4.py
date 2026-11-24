list_1 = input("Enter names separated by commas: ").split(",")
list_2 = input("Enter names separated by commas: ").split(",")  

common_names = []
for name in list_1:
    if name in list_2:
        common_names.append(name)
print("Common names:", ", ".join(common_names))
