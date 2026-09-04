# 1. WHAT IS A FUNCTION?

# A function is a reusable block of code
# that performs a specific task.

# Instead of writing the same code again and again,
# we can write it once inside a function
# and call the function whenever we need it.


# 2. WHY DO WE USE FUNCTIONS?

# Functions help us:

# Reuse code.
# Avoid repetition.
# Make programs easier to read.
# Make programs easier to debug.
# Divide large programs into smaller parts.
# Organize code better.


# 3. CREATING A FUNCTION

# We use the def keyword to create a function.

def greet():
    print("Hello")


# This creates the function.
# The function does not run until we call it.


# 4. CALLING A FUNCTION

def greet():
    print("Hello")


greet()

# Output:
# Hello


# Function call syntax:

# function_name()


# 5. BASIC FUNCTION STRUCTURE

def my_function():
    print("This is a function")


my_function()


# General syntax:

# def function_name():
#     code
#     code


# Everything inside the function
# must be indented.


# 6. INDENTATION IN FUNCTIONS

def greet():
    print("Hello")
    print("Welcome to Python")


greet()


# Both print statements belong to the function
# because they are indented.


# This line is outside the function.

print("Program finished")


# 7. FUNCTION WITH A PARAMETER

# A parameter is a variable written
# inside the function definition.

def greet(name):
    print("Hello", name)


greet("Alice")

# Output:
# Hello Alice


# Here:
# name = parameter
# "Alice" = argument


# 8. PARAMETER VS ARGUMENT

def greet(name):
    print("Hello", name)


greet("Bob")


# Parameter:
# name

# Argument:
# "Bob"


# Parameter is written when defining the function.

# Argument is the actual value passed
# when calling the function.


# 9. FUNCTION WITH MULTIPLE PARAMETERS

def introduce(name, age):
    print("Name:", name)
    print("Age:", age)


introduce("Alice", 20)

# Output:
# Name: Alice
# Age: 20


# 10. POSITIONAL ARGUMENTS

# By default, Python matches arguments
# according to their position.

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student("Alice", 20, "CSE")


# Here:

# "Alice" goes to name
# 20 goes to age
# "CSE" goes to course


# Order matters with positional arguments.


# 11. POSITIONAL ARGUMENT ORDER

def subtract(a, b):
    print(a - b)


subtract(10, 5)

# Output:
# 5


subtract(5, 10)

# Output:
# -5


# Changing the argument order
# can change the result.


# 12. KEYWORD ARGUMENTS

# Keyword arguments use the parameter name
# while calling the function.

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student(
    name="Alice",
    age=20,
    course="CSE"
)


# 13. KEYWORD ARGUMENTS CAN CHANGE ORDER

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student(
    course="CSE",
    name="Alice",
    age=20
)


# Python knows which value belongs
# to which parameter because we used names.


# 14. POSITIONAL AND KEYWORD ARGUMENTS TOGETHER

def student(name, age, course):
    print(name, age, course)


student("Alice", age=20, course="CSE")


# Positional arguments should normally come
# before keyword arguments.


# Invalid:

# student(name="Alice", 20, "CSE")

# This would give SyntaxError.


# 15. DEFAULT PARAMETERS

# A parameter can have a default value.

def greet(name="User"):
    print("Hello", name)


greet("Alice")

# Hello Alice


greet()

# Hello User


# If no argument is given,
# Python uses the default value.


# 16. MULTIPLE DEFAULT PARAMETERS

def student(name="Unknown", age=0, course="Not Assigned"):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student()

student("Alice")

student("Alice", 20)

student("Alice", 20, "CSE")


# 17. REQUIRED AND DEFAULT PARAMETERS

def student(name, age=18):
    print(name, age)


student("Alice")

# Alice 18


student("Bob", 20)

# Bob 20


# name is required.
# age has a default value.


# 18. DEFAULT PARAMETERS SHOULD COME AFTER REQUIRED PARAMETERS

# Correct:

def student(name, age=18):
    print(name, age)


# Incorrect:

# def student(age=18, name):
#     print(name, age)


# Python would give SyntaxError.


# 19. RETURN STATEMENT

# return sends a value back
# from the function.

def add(a, b):
    return a + b


result = add(10, 20)

print(result)

# Output:
# 30


# 20. print() VS return

def add_with_print(a, b):
    print(a + b)


add_with_print(10, 20)


def add_with_return(a, b):
    return a + b


result = add_with_return(10, 20)

print(result)


# print() displays something.

# return sends a value back
# so we can store or use it later.


# 21. USING A RETURNED VALUE

def add(a, b):
    return a + b


answer = add(5, 10)

print(answer)

print(answer * 2)

# Output:
# 15
# 30


# 22. RETURN CAN BE USED DIRECTLY

def multiply(a, b):
    return a * b


print(multiply(4, 5))

# Output:
# 20


# 23. FUNCTION WITHOUT return

def greet():
    print("Hello")


result = greet()

print(result)

# Output:
# Hello
# None


# If a function does not explicitly return something,
# Python automatically returns None.


# 24. RETURNING None EXPLICITLY

def do_nothing():
    return None


result = do_nothing()

print(result)

# None


# 25. return STOPS THE FUNCTION

def check_number(number):
    if number > 0:
        return "Positive"

    return "Zero or Negative"


print(check_number(10))

# Positive


# Once Python reaches return,
# the function stops running.


# 26. CODE AFTER return DOES NOT RUN

def example():
    print("Before return")

    return

    # This line will never execute.
    print("After return")


example()


# 27. RETURNING MULTIPLE VALUES

def get_student():
    return "Alice", 20, "CSE"


student = get_student()

print(student)

# Output:
# ('Alice', 20, 'CSE')


# Python packs multiple returned values
# into a tuple.


# 28. UNPACKING MULTIPLE RETURN VALUES

def get_student():
    return "Alice", 20


name, age = get_student()

print(name)

print(age)

# Output:
# Alice
# 20


# 29. FUNCTION RETURNING BOOLEAN

def is_adult(age):
    return age >= 18


print(is_adult(20))

# True


print(is_adult(15))

# False


# 30. FUNCTION RETURNING STRING

def get_grade(marks):
    if marks >= 90:
        return "A"

    if marks >= 80:
        return "B"

    if marks >= 70:
        return "C"

    return "D"


print(get_grade(95))

# A


# 31. FUNCTION RETURNING LIST

def get_numbers():
    return [1, 2, 3, 4, 5]


numbers = get_numbers()

print(numbers)


# 32. FUNCTION RETURNING TUPLE

def get_coordinates():
    return (10, 20)


coordinates = get_coordinates()

print(coordinates)


# 33. FUNCTION RETURNING DICTIONARY

def create_student():
    return {
        "name": "Alice",
        "age": 20,
        "course": "CSE"
    }


student = create_student()

print(student)


# 34. FUNCTION RETURNING SET

def get_unique_numbers():
    return {1, 2, 3}


numbers = get_unique_numbers()

print(numbers)


# 35. PASSING A LIST TO A FUNCTION

def show_numbers(numbers):
    for number in numbers:
        print(number)


my_numbers = [10, 20, 30]

show_numbers(my_numbers)


# 36. PASSING A TUPLE TO A FUNCTION

def show_values(values):
    for value in values:
        print(value)


data = (10, 20, 30)

show_values(data)


# 37. PASSING A DICTIONARY TO A FUNCTION

def show_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])


student_data = {
    "name": "Alice",
    "age": 20
}

show_student(student_data)


# 38. PASSING A SET TO A FUNCTION

def show_items(items):
    for item in items:
        print(item)


items = {"apple", "banana", "mango"}

show_items(items)


# 39. FUNCTIONS CAN MODIFY MUTABLE OBJECTS

def add_item(items):
    items.append("mango")


fruits = ["apple", "banana"]

add_item(fruits)

print(fruits)

# Output:
# ['apple', 'banana', 'mango']


# Lists are mutable.
# The function changed the original list.


# 40. REASSIGNING A PARAMETER IS DIFFERENT

def change_number(number):
    number = 100
    print("Inside function:", number)


number = 10

change_number(number)

print("Outside function:", number)

# Output:
# Inside function: 100
# Outside function: 10


# Reassigning the parameter does not
# replace the outside variable.


# 41. LOCAL VARIABLES

# A variable created inside a function
# is called a local variable.

def example():
    message = "Hello"
    print(message)


example()


# message exists only inside the function.


# This would give NameError:

# print(message)


# 42. GLOBAL VARIABLES

# A variable created outside functions
# is usually called a global variable.

message = "Hello"


def show_message():
    print(message)


show_message()

# Output:
# Hello


# A function can read a global variable.


# 43. LOCAL AND GLOBAL VARIABLES WITH SAME NAME

name = "Alice"


def show_name():
    name = "Bob"
    print("Inside:", name)


show_name()

print("Outside:", name)

# Output:
# Inside: Bob
# Outside: Alice


# The local variable and global variable
# are separate.


# 44. global KEYWORD

# global allows a function to assign
# to a global variable.

count = 0


def increase():
    global count

    count = count + 1


increase()

print(count)

# Output:
# 1


# Use global carefully.
# Functions are often easier to understand
# when values are passed and returned instead.


# 45. BETTER ALTERNATIVE TO global

count = 0


def increase(number):
    return number + 1


count = increase(count)

print(count)

# Output:
# 1


# 46. VARIABLE SCOPE

# Scope means:
# Where a variable can be accessed.


# Common scopes:

# Local
# Enclosing
# Global
# Built-in


# Python follows the LEGB rule:

# L = Local
# E = Enclosing
# G = Global
# B = Built-in


# 47. SIMPLE LEGB EXAMPLE

name = "Global"


def outer():
    name = "Enclosing"

    def inner():
        name = "Local"

        print(name)

    inner()


outer()

# Output:
# Local


# Python first searches the nearest scope.


# 48. NESTED FUNCTIONS

# A function can be defined
# inside another function.

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()


outer()

# Output:
# Outer function
# Inner function


# 49. INNER FUNCTION SCOPE

def outer():
    def inner():
        print("Hello from inner")

    inner()


outer()


# Normally, inner() exists only inside outer().

# Calling this outside would fail:

# inner()


# 50. nonlocal KEYWORD

# nonlocal allows a nested function
# to modify a variable from its enclosing function.

def outer():
    number = 10

    def inner():
        nonlocal number

        number = 20

    inner()

    print(number)


outer()

# Output:
# 20


# 51. *args

# *args allows a function to receive
# any number of positional arguments.

def add_numbers(*numbers):
    print(numbers)


add_numbers(10, 20, 30)

# Output:
# (10, 20, 30)


# *args collects arguments into a tuple.


# 52. USING *args

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


print(add_numbers(10, 20))

# 30


print(add_numbers(10, 20, 30, 40))

# 100


# 53. *args NAME CAN BE DIFFERENT

def show_values(*values):
    print(values)


show_values(1, 2, 3)


# The name does not have to be args.

# However, args is the common convention.


# 54. NORMAL PARAMETER WITH *args

def student(name, *subjects):
    print("Name:", name)
    print("Subjects:", subjects)


student(
    "Alice",
    "Python",
    "Maths",
    "Physics"
)


# Output:
# Name: Alice
# Subjects: ('Python', 'Maths', 'Physics')


# 55. **kwargs

# **kwargs allows a function to receive
# any number of keyword arguments.

def show_student(**details):
    print(details)


show_student(
    name="Alice",
    age=20,
    course="CSE"
)


# Output:
# {'name': 'Alice', 'age': 20, 'course': 'CSE'}


# **kwargs stores values in a dictionary.


# 56. LOOPING THROUGH **kwargs

def show_student(**details):
    for key, value in details.items():
        print(key, value)


show_student(
    name="Alice",
    age=20,
    course="CSE"
)


# 57. kwargs NAME CAN BE DIFFERENT

def show_data(**data):
    print(data)


show_data(
    name="Alice",
    age=20
)


# kwargs is simply the common convention.


# 58. USING NORMAL PARAMETERS, *args AND **kwargs

def example(name, *args, **kwargs):
    print("Name:", name)
    print("Args:", args)
    print("Kwargs:", kwargs)


example(
    "Alice",
    10,
    20,
    course="CSE",
    city="Delhi"
)


# 59. PARAMETER ORDER

# A common parameter order is:

# Normal positional parameters
# *args
# Keyword-only parameters
# **kwargs


def example(a, b, *args, option=True, **kwargs):
    print(a)
    print(b)
    print(args)
    print(option)
    print(kwargs)


example(
    10,
    20,
    30,
    40,
    option=False,
    name="Alice"
)


# 60. UNPACKING A LIST INTO FUNCTION ARGUMENTS

def add(a, b):
    return a + b


numbers = [10, 20]

result = add(*numbers)

print(result)

# Output:
# 30


# * unpacks list or tuple values.


# 61. UNPACKING A TUPLE INTO FUNCTION ARGUMENTS

def student(name, age):
    print(name, age)


details = ("Alice", 20)

student(*details)


# Equivalent to:

# student("Alice", 20)


# 62. UNPACKING A DICTIONARY INTO FUNCTION ARGUMENTS

def student(name, age):
    print(name, age)


details = {
    "name": "Alice",
    "age": 20
}

student(**details)


# ** unpacks dictionary key-value pairs.


# Dictionary keys must match parameter names.


# 63. POSITIONAL-ONLY PARAMETERS

# / can be used to make parameters
# positional-only.

def divide(a, b, /):
    return a / b


print(divide(10, 2))

# Output:
# 5.0


# This is valid:

divide(10, 2)


# This is invalid:

# divide(a=10, b=2)


# Parameters before / must be passed by position.


# 64. KEYWORD-ONLY PARAMETERS

# * can make parameters keyword-only.

def create_user(name, *, active=True):
    print(name, active)


create_user(
    "Alice",
    active=False
)


# This is invalid:

# create_user("Alice", False)


# active must be supplied using its name.


# 65. COMBINING POSITIONAL-ONLY AND KEYWORD-ONLY

def example(a, /, b, *, c):
    print(a, b, c)


example(
    10,
    20,
    c=30
)


# a = positional-only
# b = positional or keyword
# c = keyword-only


# 66. TYPE HINTS

# Type hints describe the expected types
# of function parameters and return values.

def add(a: int, b: int) -> int:
    return a + b


print(add(10, 20))


# Type hints improve readability.


# 67. TYPE HINTS DO NOT STRICTLY ENFORCE TYPES

def greet(name: str) -> str:
    return "Hello " + name


print(greet("Alice"))


# Python does not automatically enforce
# type hints at runtime.

# They mainly help:
# Programmers
# Editors
# Linters
# Type checkers


# 68. TYPE HINTS WITH LIST

def show_numbers(numbers: list[int]) -> None:
    for number in numbers:
        print(number)


show_numbers([1, 2, 3])


# -> None means the function
# is not expected to return a useful value.


# 69. TYPE HINTS WITH DICTIONARY

def show_user(user: dict[str, str]) -> None:
    print(user)


user = {
    "name": "Alice",
    "course": "CSE"
}

show_user(user)


# 70. FUNCTION DOCSTRING

# A docstring explains what a function does.

def add(a, b):
    """
    Return the sum of two numbers.
    """
    return a + b


print(add(10, 20))


# Docstrings use triple quotes.


# 71. ACCESSING A DOCSTRING

def greet(name):
    """
    Print a greeting for the given name.
    """
    print("Hello", name)


print(greet.__doc__)


# 72. help() WITH A FUNCTION

def multiply(a, b):
    """
    Return the product of two values.
    """
    return a * b


# You can use:

# help(multiply)

# to see information about the function.


# 73. pass IN A FUNCTION

# pass means:
# Do nothing for now.

def future_function():
    pass


future_function()


# pass is useful when creating
# the function structure before writing its code.


# 74. EMPTY FUNCTION WITHOUT pass IS INVALID

# Invalid:

# def my_function():


# Python expects an indented block.


# Correct:

def my_function():
    pass


# 75. FUNCTIONS CAN CALL OTHER FUNCTIONS

def add(a, b):
    return a + b


def double_sum(a, b):
    result = add(a, b)

    return result * 2


print(double_sum(10, 20))

# Output:
# 60


# 76. RETURN VALUE FROM ANOTHER FUNCTION

def calculate_total(price, quantity):
    return price * quantity


def show_bill(price, quantity):
    total = calculate_total(price, quantity)

    print("Total:", total)


show_bill(100, 5)


# 77. FUNCTION AS A VALUE

# Functions are objects in Python.

def greet():
    print("Hello")


another_name = greet

another_name()

# Output:
# Hello


# Notice:
# greet has no () when assigning it.


# 78. FUNCTION CALL VS FUNCTION OBJECT

def greet():
    print("Hello")


function_object = greet

# Stores the function itself.


greet()

# Calls the function.


# greet
# means the function object.

# greet()
# means execute the function.


# 79. PASSING A FUNCTION TO ANOTHER FUNCTION

def greet():
    return "Hello"


def run_function(function):
    print(function())


run_function(greet)

# Output:
# Hello


# Functions can be passed as arguments.


# 80. FUNCTION RETURNING ANOTHER FUNCTION

def outer():
    def inner():
        print("Hello from inner")

    return inner


function = outer()

function()

# Output:
# Hello from inner


# 81. BUILT-IN FUNCTIONS

# Python already provides many functions.

print("Hello")

len([1, 2, 3])

type(10)

int("20")

str(100)

float("3.14")

list((1, 2, 3))

tuple([1, 2, 3])

set([1, 2, 2, 3])

dict(name="Alice")

sum([1, 2, 3])

min([1, 2, 3])

max([1, 2, 3])

sorted([3, 1, 2])

abs(-10)

round(3.14159, 2)


# These are built-in functions.


# 82. USER-DEFINED FUNCTIONS

# Functions created using def
# are user-defined functions.

def welcome():
    print("Welcome")


welcome()


# 83. LAMBDA FUNCTIONS

# lambda creates a small anonymous function.

square = lambda number: number ** 2

print(square(5))

# Output:
# 25


# Equivalent normal function:

def square_normal(number):
    return number ** 2


print(square_normal(5))


# 84. LAMBDA WITH MULTIPLE PARAMETERS

add = lambda a, b: a + b

print(add(10, 20))

# Output:
# 30


# 85. LAMBDA SYNTAX

# lambda parameters: expression


# Example:

multiply = lambda a, b: a * b

print(multiply(4, 5))


# Lambda functions are generally used
# for small simple operations.


# 86. LAMBDA WITH sorted()

names = [
    "Bob",
    "Alexander",
    "Tom",
    "Alice"
]

names.sort(key=lambda name: len(name))

print(names)


# Sorts names according to their length.


# 87. FUNCTION WITH if STATEMENT

def check_age(age):
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


check_age(20)


# 88. FUNCTION WITH for LOOP

def show_numbers(numbers):
    for number in numbers:
        print(number)


show_numbers([10, 20, 30])


# 89. FUNCTION WITH while LOOP

def countdown(number):
    while number > 0:
        print(number)

        number = number - 1

    print("Done")


countdown(3)


# Output:
# 3
# 2
# 1
# Done


# 90. FUNCTION WITH MULTIPLE return STATEMENTS

def check_number(number):
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


print(check_number(10))

print(check_number(-5))

print(check_number(0))


# 91. EARLY RETURN

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print(divide(10, 2))

print(divide(10, 0))


# Early return can simplify functions.


# 92. BOOLEAN FUNCTION

def is_even(number):
    return number % 2 == 0


print(is_even(10))

# True


print(is_even(7))

# False


# 93. FUNCTION USING USER INPUT

def greet_user():
    name = input("Enter your name: ")

    print("Hello", name)


# Uncomment when you want to test:

# greet_user()


# 94. FUNCTION WITH INPUT AND RETURN

def get_age():
    age = int(input("Enter your age: "))

    return age


# Uncomment when testing:

# user_age = get_age()
# print(user_age)


# 95. FUNCTION WITH VALIDATION

def check_age(age):
    if age < 0:
        return "Invalid age"

    if age >= 18:
        return "Adult"

    return "Minor"


print(check_age(20))

print(check_age(15))

print(check_age(-5))


# 96. RECURSION

# Recursion means a function calls itself.

def countdown(number):
    if number == 0:
        print("Done")

        return

    print(number)

    countdown(number - 1)


countdown(3)


# Output:
# 3
# 2
# 1
# Done


# 97. BASE CASE IN RECURSION

# A recursive function usually needs
# a condition that stops recursion.

def countdown(number):
    if number <= 0:
        return

    print(number)

    countdown(number - 1)


countdown(3)


# number <= 0 is the base case.


# Without a proper stopping condition,
# recursion can continue until Python
# raises RecursionError.


# 98. FUNCTION DEFAULT ARGUMENT WARNING

# Be careful with mutable default values.

# Avoid:

def bad_example(items=[]):
    items.append("Python")

    return items


print(bad_example())

print(bad_example())

# The same list can be reused across calls.


# Output:
# ['Python']
# ['Python', 'Python']


# 99. BETTER WAY FOR MUTABLE DEFAULT VALUES

def good_example(items=None):
    if items is None:
        items = []

    items.append("Python")

    return items


print(good_example())

print(good_example())

# Each call receives a new list.


# 100. DEFAULT IMMUTABLE VALUES ARE USUALLY FINE

def greet(name="User"):
    print("Hello", name)


def calculate_tax(rate=0.10):
    print(rate)


greet()

calculate_tax()


# Strings, numbers, booleans, and None
# are commonly safe default values.


# 101. FUNCTION NAMING RULES

# Function names follow normal variable naming rules.

# Valid:

def calculate_total():
    pass


def get_name():
    pass


def student_details():
    pass


# Invalid examples:

# def 1function():
#     pass

# def my-function():
#     pass

# def my function():
#     pass


# 102. FUNCTION NAMING CONVENTION

# Python normally uses snake_case
# for function names.

def calculate_total_price():
    pass


def get_student_name():
    pass


# Prefer:

# calculate_total_price()

# Instead of:

# CalculateTotalPrice()
# calculateTotalPrice()


# 103. USE MEANINGFUL FUNCTION NAMES

# Better:

def calculate_average():
    pass


# Harder to understand:

def ca():
    pass


# Function names should clearly describe
# what the function does.


# 104. FUNCTIONS SHOULD DO ONE CLEAR JOB

# Better:

def calculate_total(price, quantity):
    return price * quantity


def display_total(total):
    print("Total:", total)


total = calculate_total(100, 5)

display_total(total)


# Small focused functions
# are easier to understand and reuse.


# 105. DON'T REPEAT CODE

# Without a function:

print("Hello Alice")
print("Hello Bob")
print("Hello Charlie")


# With a function:

def greet(name):
    print("Hello", name)


greet("Alice")

greet("Bob")

greet("Charlie")


# 106. RETURNING CALCULATED VALUES

def calculate_area(length, width):
    area = length * width

    return area


room_area = calculate_area(10, 5)

print(room_area)


# 107. FUNCTION WITH DEFAULT BOOLEAN

def create_account(name, active=True):
    print("Name:", name)
    print("Active:", active)


create_account("Alice")

create_account(
    "Bob",
    active=False
)


# 108. FUNCTION WITH None DEFAULT

def greet(name=None):
    if name is None:
        print("Hello User")
    else:
        print("Hello", name)


greet()

greet("Alice")


# 109. CHECKING WHETHER ARGUMENT WAS PROVIDED

def show_message(message=None):
    if message is None:
        print("No message provided")

        return

    print(message)


show_message()

show_message("Hello")


# 110. RETURNING DIFFERENT TYPES

# Python functions can return different types.

def get_value(condition):
    if condition:
        return 100

    return None


print(get_value(True))

print(get_value(False))


# However, keeping return types predictable
# often makes code easier to understand.


# 111. FUNCTION ANNOTATION WITH DEFAULT VALUE

def greet(name: str = "User") -> str:
    return "Hello " + name


print(greet())

print(greet("Alice"))


# 112. FUNCTION WITH list TYPE HINT

def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)


print(calculate_total([10, 20, 30]))

# Output:
# 60


# 113. FUNCTION WITH tuple TYPE HINT

def get_point() -> tuple[int, int]:
    return 10, 20


print(get_point())


# 114. FUNCTION WITH set TYPE HINT

def unique_values(values: list[int]) -> set[int]:
    return set(values)


print(unique_values([1, 2, 2, 3]))


# 115. FUNCTION WITH dictionary TYPE HINT

def create_user(name: str, age: int) -> dict:
    return {
        "name": name,
        "age": age
    }


print(create_user("Alice", 20))


# 116. FUNCTION CAN USE ANOTHER FUNCTION'S RETURN VALUE

def get_price():
    return 100


def calculate_total(quantity):
    price = get_price()

    return price * quantity


print(calculate_total(5))

# Output:
# 500


# 117. STORING FUNCTIONS IN A LIST

def greet():
    print("Hello")


def goodbye():
    print("Goodbye")


functions = [
    greet,
    goodbye
]


for function in functions:
    function()


# Notice:
# We store greet, not greet().


# 118. FUNCTION INSIDE A DICTIONARY

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


operations = {
    "add": add,
    "subtract": subtract
}


print(operations["add"](10, 5))

# Output:
# 15


# 119. id() OF A FUNCTION

def greet():
    print("Hello")


print(type(greet))

# Output:
# <class 'function'>


print(id(greet))


# Functions are Python objects.


# 120. __name__ ATTRIBUTE

def greet():
    print("Hello")


print(greet.__name__)

# Output:
# greet


# 121. COMMON ERROR: FORGETTING ()

def greet():
    print("Hello")


print(greet)

# This prints information about the function object.


greet()

# This actually calls the function.


# 122. COMMON ERROR: WRONG INDENTATION

# Wrong:

# def greet():
# print("Hello")


# Correct:

def greet():
    print("Hello")


# Function body must be indented.


# 123. COMMON ERROR: WRONG NUMBER OF ARGUMENTS

def add(a, b):
    return a + b


# add(10)

# TypeError:
# missing required argument


# add(10, 20, 30)

# TypeError:
# too many arguments


# Correct:

print(add(10, 20))


# 124. COMMON ERROR: RETURN VS PRINT

def add_wrong(a, b):
    print(a + b)


result = add_wrong(10, 20)

print(result)

# Output:
# 30
# None


# If you need the answer later,
# return it instead.


def add_correct(a, b):
    return a + b


result = add_correct(10, 20)

print(result)


# 125. COMMON ERROR: USING LOCAL VARIABLE OUTSIDE

def example():
    number = 10

    print(number)


example()


# This would give NameError:

# print(number)


# 126. COMMON ERROR: MODIFYING GLOBAL VARIABLE WITHOUT global

count = 0


def incorrect_example():
    # count = count + 1

    pass


# The commented statement would cause:

# UnboundLocalError


# One solution:

def correct_example():
    global count

    count = count + 1


correct_example()

print(count)


# Often a cleaner solution is to
# return the changed value instead.


# 127. COMMON ERROR: MUTABLE DEFAULT ARGUMENT

def add_item_bad(item, items=[]):
    items.append(item)

    return items


# Avoid this pattern when you want
# a fresh list for every call.


# Better:

def add_item_good(item, items=None):
    if items is None:
        items = []

    items.append(item)

    return items


# 128. COMMON ERROR: SHADOWING BUILT-IN FUNCTION NAMES

# Avoid function names such as:

# list
# str
# int
# set
# dict
# sum
# max
# min
# input
# print


# Bad:

# def sum():
#     pass


# Better:

def calculate_sum(numbers):
    return sum(numbers)


print(calculate_sum([1, 2, 3]))


# 129. COMMON ERROR: CALLING FUNCTION BEFORE DEFINITION

# Python executes code from top to bottom.

# This would fail:

# greet_user()

# def greet_user():
#     print("Hello")


# Define the function first:

def greet_user():
    print("Hello")


greet_user()


# 130. COMMON ERROR: DUPLICATE FUNCTION NAMES

def greet():
    print("First function")


def greet():
    print("Second function")


greet()

# Output:
# Second function


# The newer definition replaces
# the previous name.


# 131. COMMON ERROR: CONFUSING ARGUMENT AND PARAMETER

def greet(name):
    print(name)


greet("Alice")


# name = parameter

# "Alice" = argument


# 132. COMMON ERROR: KEYWORD NAME DOES NOT EXIST

def greet(name):
    print(name)


# greet(username="Alice")

# TypeError


# Parameter is called name,
# not username.


# Correct:

greet(name="Alice")


# 133. PRACTICAL EXAMPLE: GREETING FUNCTION

def greet(name):
    return "Hello " + name


message = greet("Alice")

print(message)


# 134. PRACTICAL EXAMPLE: CALCULATOR FUNCTIONS

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print(add(10, 5))

print(subtract(10, 5))

print(multiply(10, 5))

print(divide(10, 5))


# 135. PRACTICAL EXAMPLE: MARKS

def calculate_average(marks):
    if len(marks) == 0:
        return 0

    return sum(marks) / len(marks)


student_marks = [
    90,
    85,
    95
]

average = calculate_average(student_marks)

print("Average:", average)


# 136. PRACTICAL EXAMPLE: STUDENT DETAILS

def create_student(name, age, course):
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    return student


student = create_student(
    "Alice",
    20,
    "CSE"
)

print(student)


# 137. PRACTICAL EXAMPLE: DISPLAY STUDENT

def display_student(student):
    for key, value in student.items():
        print(f"{key}: {value}")


student = {
    "name": "Alice",
    "age": 20,
    "course": "CSE"
}

display_student(student)


# 138. PRACTICAL EXAMPLE: CHECK PASSWORD LENGTH

def is_valid_password(password):
    return len(password) >= 8


print(is_valid_password("hello"))

# False


print(is_valid_password("hello123"))

# True


# 139. PRACTICAL EXAMPLE: TEMPERATURE CONVERSION

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit


print(celsius_to_fahrenheit(0))

# 32.0


print(celsius_to_fahrenheit(100))

# 212.0


# 140. PRACTICAL EXAMPLE: FULL NAME

def get_full_name(first_name, last_name):
    return first_name + " " + last_name


full_name = get_full_name(
    "Alice",
    "Smith"
)

print(full_name)


# 141. PRACTICAL EXAMPLE: SHOPPING TOTAL

def calculate_bill(price, quantity):
    return price * quantity


total = calculate_bill(
    price=500,
    quantity=3
)

print("Total:", total)


# 142. PRACTICAL EXAMPLE: DISCOUNT

def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100

    final_price = price - discount

    return final_price


print(calculate_discount(1000, 10))

# Output:
# 900.0


# 143. PRACTICAL EXAMPLE: DEFAULT DISCOUNT

def calculate_price(price, discount=0):
    discount_amount = price * discount / 100

    return price - discount_amount


print(calculate_price(1000))

# 1000.0


print(calculate_price(1000, 10))

# 900.0


# 144. FUNCTION METHOD CHEAT SHEET

# Functions do not have "methods"
# like lists or dictionaries.

# Main function-related keywords:

# def
# Creates a function.

# return
# Sends a value back and exits the function.

# pass
# Creates an empty placeholder body.

# global
# Allows assignment to a global variable.

# nonlocal
# Allows assignment to a variable
# in an enclosing function.

# lambda
# Creates a small anonymous function.


# 145. FUNCTION ARGUMENT CHEAT SHEET


# Normal positional parameters:

def example1(a, b):
    print(a, b)


example1(10, 20)


# Keyword arguments:

example1(
    a=10,
    b=20
)


# Default parameter:

def example2(name="User"):
    print(name)


example2()


# *args:

def example3(*args):
    print(args)


example3(1, 2, 3)


# **kwargs:

def example4(**kwargs):
    print(kwargs)


example4(
    name="Alice",
    age=20
)


# 146. RETURN CHEAT SHEET


# Return one value:

def example_one():
    return 10


# Return multiple values:

def example_multiple():
    return 10, 20


# Return nothing useful:

def example_none():
    return None


# No return statement:

def example_no_return():
    print("Hello")


# Python returns None automatically.


# 147. SCOPE CHEAT SHEET

global_variable = "Global"


def outer():
    enclosing_variable = "Enclosing"

    def inner():
        local_variable = "Local"

        print(local_variable)
        print(enclosing_variable)
        print(global_variable)

    inner()


outer()


# LEGB:

# Local
# Enclosing
# Global
# Built-in


# 148. MOST IMPORTANT THINGS TO REMEMBER

# Functions are reusable blocks of code.

# Use def to create a function.

# Syntax:

# def function_name():
#     code


# Call a function using:

# function_name()


# Parameter:
# Variable in function definition.

# Argument:
# Actual value passed to a function.


# Example:

def greet(name):
    print("Hello", name)


greet("Alice")


# name is a parameter.

# "Alice" is an argument.


# return sends a value back.

def add(a, b):
    return a + b


# print() displays a result.

# return gives the result back
# so it can be reused.


# A function with no explicit return
# returns None.


# Positional arguments depend on order.

# Keyword arguments use parameter names.

# Default parameters provide fallback values.

# *args stores extra positional arguments
# inside a tuple.

# **kwargs stores extra keyword arguments
# inside a dictionary.

# Variables inside functions are usually local.

# Variables outside functions are usually global.

# global can modify a global variable.

# nonlocal can modify a variable
# in an enclosing function.

# Functions can call other functions.

# Functions can return other functions.

# Functions can be passed as arguments.

# Functions are objects in Python.

# Type hints describe expected types
# but normally do not enforce them.

# Docstrings explain what functions do.

# lambda creates a small anonymous function.

# Functions can contain:
# if
# elif
# else
# for
# while
# try
# other functions
# and almost any normal Python code.

# Always indent the function body.

# Use meaningful snake_case names.

# Avoid mutable default arguments such as:

# def example(items=[]):

# Prefer:

# def example(items=None):


# 149. QUICK FUNCTION SYNTAX SUMMARY


# Simple function:

def greet():
    print("Hello")


greet()


# Parameter:

def greet(name):
    print("Hello", name)


greet("Alice")


# Multiple parameters:

def add(a, b):
    return a + b


print(add(10, 20))


# Default parameter:

def greet(name="User"):
    print("Hello", name)


greet()


# Keyword argument:

greet(name="Alice")


# Return value:

def multiply(a, b):
    return a * b


result = multiply(5, 10)

print(result)


# *args:

def total(*numbers):
    return sum(numbers)


print(total(1, 2, 3, 4))


# **kwargs:

def profile(**details):
    print(details)


profile(
    name="Alice",
    age=20
)


# Type hints:

def subtract(a: int, b: int) -> int:
    return a - b


print(subtract(20, 5))


# Lambda:

square = lambda number: number ** 2

print(square(5))


# 150. FINAL BEGINNER EXAMPLE

def create_student(name, age, course="CSE"):
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    return student


def display_student(student):
    print("Student Details")

    for key, value in student.items():
        print(f"{key}: {value}")


def is_adult(age):
    return age >= 18


student = create_student(
    "Alice",
    20
)

display_student(student)


if is_adult(student["age"]):
    print("Student is an adult")
else:
    print("Student is a minor")


# END OF PYTHON FUNCTIONS NOTES