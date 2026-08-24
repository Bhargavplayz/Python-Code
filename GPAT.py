"""G-PAT: Greatest Printer Of All Time.
This module provides a simple text-based interface for, calculating, displaying names, or rolling dice."""
print("----------------------------------------------------------------------------------------------------------")
print("Hello, Welcome to The Greatest Printer Of All Time (G-PAT).")
print("You can get the display of whatever you want to print.")
print("You can use this as a basic Calculator, a Proper Name Display, or Even a Randomized Dice Roller.")
print("----------------------------------------------------------------------------------------------------------")
print("Current types in G-PAT are •~ Calculator ~•, •~ Name display ~• , •~ Dice Roller ~•\n")


def user_calculator():

    while True:
        user_num1 = input("Type in your 1st Number: ")
        try:
            user_num1 = int(user_num1)
            break
        except ValueError:
            print("Invalid. Please Enter a Number.")

    while True:
        user_num2 = input("Type in your 2nd Number: ")
        try:
            user_num2 = int(user_num2)
            break
        except ValueError:
            print("Invalid. Please Enter a Number")

    print(
        "------------------------------------------------------------------------------\n"
        "And Finally.")

    while True:
        user_function = input("Type '+' for Addition\n"
                              "Type '-' for Subtractions\n"
                              "Type '*' for Multiplication\n"
                              "Type '/' for Division\n"
                              ": ")
        if user_function in ["+", "-", "*", "/"]:
            if user_function == "+":
                user_action = "ADD"
                user_ans = user_num1 + user_num2
            elif user_function == "-":
                user_action = "SUBTRACT"
                user_ans = user_num1 - user_num2
            elif user_function == "*":
                user_action = "MULTIPLY"
                user_ans = user_num1 * user_num2
            elif user_function == "/":
                user_action = "DIVIDE"
                if user_num2 != 0:
                    user_ans = user_num1 / user_num2
                else:
                    user_ans = "Undefined! (Cannot divide by 0)"

            break
        else:
            print("Invalid. Please enter a proper function.")
    print(
        f"So Your Numbers are {user_num1} and {user_num2} and you want to {user_action} them Both.")
    print(
        f"Your Answer for {user_num1} {user_function} {user_num2} is {user_ans} ")
    return


def user_name_display():
    while True:
        user_first_name = input("Enter your First Name: ").strip().capitalize()
        if user_first_name.isalpha():
            break
        else:
            print("Name Only Consists of Alphabets (no spaces)")
    print("----------------------------------------------------------------------------------------------------------\n")
    while True:
        user_surname = input(
            "Enter your Surname/Family Name: ").strip().capitalize()
        if user_surname.isalpha():
            break
        else:
            print("Name Only Consists of Alphabets (no spaces)")
    print("----------------------------------------------------------------------------------------------------------")
    while True:
        Middle_nameQ = input(
            "Do you have a Middle(Extra) Name? [Type Y for Yes/ N for No]: ").upper().strip()
        if Middle_nameQ in ["Y", "N"]:
            break
    print("----------------------------------------------------------------------------------------------------------\n")
    if Middle_nameQ == "Y":
        while True:
            user_middle_name = input("Type in your Middle Name: ").capitalize()
            if user_middle_name.replace(" ", "").isalpha():
                break
            else:
                print(
                    "Name Only Consists of Alphabets (spaces, if you have more than one)")
    elif Middle_nameQ == "N":
        user_middle_name = ""
    print("----------------------------------------------------------------------------------------------------------\n")
    while True:
        name_surstyle = input("Which Style Do you want to View your Name in?\n"
                              "\n"
                              "Asian: >Surname< THEN >First Name<\n"
                              "---------------- OR ----------------\n"
                              "Other: >First Name< THEN >Surname<\n"
                              "[Type 'Asian' / 'Other' for the Format]: ").capitalize().strip()
        if name_surstyle in ["Asian", "Other"]:
            break
        else:
            print("Invalid...\n")
    print("----------------------------------------------------------------------------------------------------------\n")

    def get_midstyle():
        while True:
            name_middle_style = str(input("In Which Position Do you want to View your Middle Name as?\n"
                                          "\n"
                                          "1: >Middle Name< THEN >First Name<\n"
                                          "---------------- OR ----------------\n"
                                          "2: >First Name< THEN >Middle Name<\n"
                                          "[Type '1' / '2' for the Format]: ")).strip()
            if name_middle_style in ["1", "2"]:
                return name_middle_style
            else:
                print("Invalid...\n")

    if Middle_nameQ == "Y":
        name_middle_style = get_midstyle()
        print("----------------------------------------------------------------------------------------------------------\n")
        if name_surstyle == "Asian" and name_middle_style == "1":
            print(
                f"Hello! {user_surname}. {user_middle_name} {user_first_name}. ")
        elif name_surstyle == "Asian" and name_middle_style == "2":
            print(
                f"Hello! {user_surname}. {user_first_name} {user_middle_name}. ")
        elif name_surstyle == "Other" and name_middle_style == "1":
            print(
                f"Hello! {user_middle_name} {user_first_name} .{user_surname}. ")
        elif name_surstyle == "Other" and name_middle_style == "2":
            print(
                f"Hello! {user_first_name} {user_middle_name} .{user_surname}. ")

    elif Middle_nameQ == "N":
        print("----------------------------------------------------------------------------------------------------------")
        if name_surstyle == "Asian":
            print(
                f"Hello! {user_surname}. {user_first_name}. ")

        elif name_surstyle == "Other":
            print(
                f"Hello! {user_first_name} .{user_surname}. ")


while True:
    user_type = input(
        "Please enter the type you want to use G-PAT for: ").lower().strip()
    if user_type in ["calculator", "name display", "dice roller"]:
        break
    else:
        print("Invalid input. Please enter a valid type (Calculator, Name Display, Dice Roller).")

print(f"\nYou Selected {user_type}.")
print("----------------------------------------------------------------------------------------------------------\n")
if user_type == "calculator":
    user_calculator()
elif user_type == "name display":
    user_name_display()
