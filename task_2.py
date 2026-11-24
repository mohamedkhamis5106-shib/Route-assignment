password = input("Enter your password: ")
special_characters = ["!", "@", "#", "$"]

valid = True

if len(password) < 8:
    print("Password must be at least 8 characters long.")
    valid = False

if len(password) > 16:
    print("Password must not exceed 16 characters.")
    valid = False

if not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
    valid = False

if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
    valid = False

if not any(char in special_characters for char in password):
    print("Password must contain at least one special character.")
    valid = False

if valid:
    print("Password is valid.")