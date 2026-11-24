students = {
    "names": ["Alice", "Bob", "Charlie", "David"],
    "grades": {
        "Alice": [75,56,98],
        "Bob": [92,99,67],
        "Charlie": [78,32,88],
        "David": [90,85,95]
    }
}
for name in students["names"]:
    grades = students["grades"][name]
    average = sum(grades) / len(grades)
    if average >= 90:
        print(f"{name}: Average {average:.2f} - Honor Roll")