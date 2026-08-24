# WELCOME TO MY NOTES ON PYTHON

#                                                              • COMMANDS •


# print() command -> Lets you print / Display anything you want to the console. You can print strings, numbers, and even variables
# Note: Strings must be enclosed in quotation marks("..."), while numbers and variables do not require quotation marks.
# Note: You can also use the print() command to display multiple items at once, separated by commas. The print() command will automatically add a space between each item.
# > example of print() command:
print("Hello, World!")  # prints a string

# input() command -> Lets you take input from the user. You can store the input in a variable for later use.
# Note: The input() command always returns a string, so you may need to convert it to another data type if necessary.
# Note: You can also use the input() command to display a prompt message to the user, asking them to enter something.
# > example of input() command:
# takes input from the user and stores it in the variable 'name'
name = input("Enter your name: ")

#                                                            • Type Conversion(Casting) •

# int() command -> Converts a string or number to an integer.
# > example of int() command:
num_str = "10"
num_int = int(num_str)  # converts the string "10" to the integer 10

# bool() command -> Converts a value to a Boolean (True or False).
# Note: The bool() command will return True for any non-zero number or non-empty string, and False for zero or an empty string.
# > example of bool() command:
num = 5
is_true = bool(num)  # converts the number 5 to the Boolean True

# float() command -> Converts a string or number to a floating-point number.
# > example of float() command:
num_str = "10.5"
num_float = float(num_str)  # converts the string "10.5" to the float 10.5

# str() command -> Converts a value to a string.
# > example of str() command:
num = 10
num_str = str(num)  # converts the number 10 to the string "10"

# type() command -> Returns the data type of a variable.
# > example of type() command:
num = 10
print(type(num))  # prints the data type of the variable 'num'

# len() command -> Returns the length of a string or list.
# Note: The len() command can also be used to count the number of items in a list or tuple.
# Note: The len() command counts from 1, not 0. So if you have a string with 5 characters, len() will return 5, not 4. and if you put -1 in the len() command, it will return the length of the string minus 1. For example, if you have a string with 5 characters, len(string) - 1 will return 4.
# > example of len() command:
my_string = "Hello, World!"
print(len(my_string))  # prints the length of the string

#                                                             • Conditional Statements •

# if statement -> Lets you execute a block of code only if a certain condition is true.
# Note: The condition in the if statement must be a Boolean expression that evaluates to either True or False.
# > example of if statement:
x = 10
if x > 10:
    print("x is greater than 10")

# else statement -> Lets you execute a block of code if the condition in the if statement is false.
# > example of else statement:
x = 10
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

# elif statement -> Lets you execute a block of code if the condition in the if statement is false, and the condition in the elif statement is true.
    # Note: You can have multiple elif statements, but only one else statement.
# > example of if, elif, and else statements:
x = 10
if x > 10:
    print("x is greater than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is less than 10")

#                                                                • Ternary Operator •
# Ternary operator -> Lets you write a simple if-else statement in a single line of code.
    # Note: The syntax for the ternary operator is: <expression1> if <condition> else <expression2>
    # Note: The ternary operator can be used to assign a value to a variable based on a condition.
# > example of ternary operator:
x = 10
result = "x is greater than 10" if x > 10 else "x is not greater than 10"
print(result)

#                                                              • Basic Math Operators •
# + -> Adds two values together.
# - -> Subtracts the second value from the first value.
# * -> Multiplies two values together.
# / -> Divides the first value by the second value.
# % -> Returns the remainder of the division of the first value by the second value.
# ** -> Raises the first value to the power of the second value.

#                                                               • Comparison Operators •
# == -> Checks if two values are equal.
# != -> Checks if two values are not equal.
# < -> Checks if the first value is less than the second value.
# > -> Checks if the first value is greater than the second value.
# <= -> Checks if the first value is less than or equal to the second value.
# >= -> Checks if the first value is greater than or equal to the second value.

#                                                               • Assignment Operators •
# = -> Assigns a value to a variable.
# += -> Adds a value to a variable and assigns the result to the variable.
# -= -> Subtracts a value from a variable and assigns the result to the variable.
# *= -> Multiplies a value by a variable and assigns the result to the variable.
# /= -> Divides a variable by a value and assigns the result to the variable.

#                                                              • Logical Operators •
# and -> Returns True if both conditions are true.
# or -> Returns True if at least one condition is true.
# not -> Returns True if the condition is false, and vice versa.
# nand -> Returns True if at least one condition is false.
# nor -> Returns True if both conditions are false.
# xor -> Returns True if one condition is true and the other is false.
# nxor -> Returns True if both conditions are true or both conditions are false.

#                                                               • Membership Operators •
# in -> Checks if a value is present in a sequence.
# not in -> Checks if a value is not present in a sequence.

#                                                               • Identity Operators •
# is -> Checks if two variables refer to the same object.
# is not -> Checks if two variables do not refer to the same object.
# remember: The difference between the 'is' operator and the '==' operator is that the 'is' operator checks for object identity, while the '==' operator checks for value equality. In other words, the 'is' operator checks if two variables point to the same object in memory, while the '==' operator checks if two variables have the same value.

#                                                               • List Operators •
# 'def' -> Defines a function.
# > example of def command:


def my_function():
    pass


# list() -> Creates a list from a sequence of values.
    # > example of list() command:
my_list = list("Hello")  # creates a list of characters from the string "Hello"
# dictionary() -> Creates a dictionary from a sequence of key-value pairs.
# > example of dictionary() command: Creates a dictionary with key-value pairs
my_dict = dict([('a', 1), ('b', 2)])
# Note: {} is used to create an empty dictionary, while [] is used to create an empty list.
# range() -> Generates a sequence of numbers, which can be used to create lists or iterate over a sequence of numbers.
# > example of range() command:
my_list = list(range(1, 10))  # creates a list of numbers from 1 to 10
# sorted() -> Sorts a list in ascending order by default, but can also sort in descending order if specified.
# > example of sorted() command:
# sorts the list in descending order
sorted_list = sorted(my_list, reverse=True)

#                                                               • Bitwise Operators •
# & -> Performs a bitwise AND operation.
# | -> Performs a bitwise OR operation.
# ^ -> Performs a bitwise XOR operation.
# ~ -> Performs a bitwise NOT operation.
# << -> Performs a left shift operation.
# >> -> Performs a right shift operation.
