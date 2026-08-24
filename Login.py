import sys


while True:
    name = input("Enter a name: ")
    if name.isalpha():
        break
    else:
        print("Invalid name. Please enter a valid name.")

print(f"Hello, {name}! Welcome to the program. Please type in your Details to continue.")


while True:
    phone = input("Enter your phone number: ")
    if phone.isdigit() and len(phone) == 10:
        break
    else:
        print("Invalid phone number. Please enter a 10-digit phone number.")

print(f"Thank you, {name}! Your phone number has been recorded.")


while True:
    age = input("Enter your age: ")
    if age.isdigit() and int(age) >= 100:
        print("How are you even alive? and What are you Doing here?!")
        sys.exit()
    elif age.isdigit() and int(age) >= 18:
        print("You are eligible to continue.")
        break
    elif age.isdigit() and int(age) < 18:
        print("You are not eligible to continue.")
        sys.exit()
    else:
        print("Invalid input. Please enter a valid age.")


while True:
    email = input("Enter your email address: ")
    if "@" in email and "." in email:
        print(f"Thank you, {name}! Your email address has been recorded.")
        break
    else:
        print("Invalid email address. Please enter a valid email address.")
