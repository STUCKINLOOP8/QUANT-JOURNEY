# PYTHON TUPLES


# 1. WHAT IS A TUPLE?

# A tuple stores multiple values inside one variable.
# Tuples are usually written using parentheses ().

fruits = ("apple", "banana", "mango")

print(fruits)

# Output:
# ('apple', 'banana', 'mango')


# 2. IMPORTANT PROPERTIES OF TUPLES

# Tuples are:
# Ordered
# Immutable
# Allow duplicate values
# Can contain different data types
# Support indexing
# Support slicing


# Ordered means elements have a fixed position.

fruits = ("apple", "banana", "mango")

# apple  -> index 0
# banana -> index 1
# mango  -> index 2


# Immutable means the tuple cannot be changed after creation.

numbers = (10, 20, 30)

# numbers[0] = 100

# This would give TypeError.


# 3. CREATING A TUPLE

numbers = (1, 2, 3, 4)

names = ("Alice", "Bob", "Charlie")

data = ("Alice", 20, 85.5, True)

print(numbers)
print(names)
print(data)


# 4. EMPTY TUPLE

empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

# Output:
# ()
# <class 'tuple'>


# 5. SINGLE ELEMENT TUPLE

# A single-element tuple MUST have a comma.

number = (10,)

print(number)
print(type(number))

# Output:
# (10,)
# <class 'tuple'>


# Without the comma:

number = (10)

print(type(number))

# Output:
# <class 'int'>


# Therefore:

correct_tuple = (10,)


# 6. TUPLE WITHOUT PARENTHESES

# Parentheses are not always required.

numbers = 10, 20, 30

print(numbers)
print(type(numbers))

# Output:
# (10, 20, 30)
# <class 'tuple'>


# This is called tuple packing.


# 7. USING tuple()

numbers = tuple((10, 20, 30))

print(numbers)


# Converting list to tuple:

numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)

# Output:
# (10, 20, 30)


# 8. CONVERTING STRING TO TUPLE

word = "Python"

characters = tuple(word)

print(characters)

# Output:
# ('P', 'y', 't', 'h', 'o', 'n')


# 9. ACCESSING TUPLE ELEMENTS

fruits = ("apple", "banana", "mango")

print(fruits[0])
print(fruits[1])
print(fruits[2])

# Output:
# apple
# banana
# mango


# Indexing starts from 0.


# 10. NEGATIVE INDEXING

fruits = ("apple", "banana", "mango", "orange")

print(fruits[-1])

# orange


print(fruits[-2])

# mango


# -1 = last element
# -2 = second-last element
# -3 = third-last element


# 11. LENGTH OF A TUPLE

numbers = (10, 20, 30, 40)

print(len(numbers))

# Output:
# 4


# 12. FIRST AND LAST ELEMENT

numbers = (10, 20, 30, 40)

print(numbers[0])

# First element


print(numbers[-1])

# Last element


# 13. TUPLE SLICING

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

# Output:
# (20, 30, 40)


# Syntax:
# tuple[start:stop]

# start is included.
# stop is NOT included.


# 14. SLICE FROM BEGINNING

numbers = (10, 20, 30, 40, 50)

print(numbers[:3])

# Output:
# (10, 20, 30)


# 15. SLICE TO THE END

numbers = (10, 20, 30, 40, 50)

print(numbers[2:])

# Output:
# (30, 40, 50)


# 16. SLICING THE WHOLE TUPLE

numbers = (10, 20, 30, 40)

copy_tuple = numbers[:]

print(copy_tuple)


# 17. SLICING WITH STEP

numbers = (1, 2, 3, 4, 5, 6)

print(numbers[::2])

# Output:
# (1, 3, 5)


# Syntax:
# tuple[start:stop:step]


# 18. REVERSING A TUPLE

numbers = (1, 2, 3, 4, 5)

reversed_numbers = numbers[::-1]

print(reversed_numbers)

# Output:
# (5, 4, 3, 2, 1)


# 19. NEGATIVE SLICING

numbers = (10, 20, 30, 40, 50)

print(numbers[-3:])

# Output:
# (30, 40, 50)


# 20. TUPLES ARE IMMUTABLE

numbers = (10, 20, 30)

# This is NOT allowed:

# numbers[0] = 100


# Python would give:
# TypeError: 'tuple' object does not support item assignment


# 21. HOW TO CHANGE A TUPLE

# Tuples cannot be changed directly.
# One way is:
# tuple -> list -> modify -> tuple

numbers = (10, 20, 30)

numbers_list = list(numbers)

numbers_list[0] = 100

numbers = tuple(numbers_list)

print(numbers)

# Output:
# (100, 20, 30)


# 22. ADDING ONE ELEMENT

# Tuples do not have append().

numbers = (10, 20, 30)

numbers = numbers + (40,)

print(numbers)

# Output:
# (10, 20, 30, 40)


# Remember the comma:

# (40,) is a tuple.
# (40) is an integer.


# 23. ADDING MULTIPLE ELEMENTS

numbers = (10, 20, 30)

numbers = numbers + (40, 50)

print(numbers)

# Output:
# (10, 20, 30, 40, 50)


# 24. JOINING TWO TUPLES

tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)

# Output:
# (1, 2, 3, 4, 5, 6)


# 25. REPEATING A TUPLE

numbers = (1, 2)

result = numbers * 3

print(result)

# Output:
# (1, 2, 1, 2, 1, 2)


# 26. REMOVING AN ELEMENT

# Tuples do not have remove().

numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

numbers_list.remove(30)

numbers = tuple(numbers_list)

print(numbers)

# Output:
# (10, 20, 40)


# 27. DELETING A COMPLETE TUPLE

numbers = (10, 20, 30)

del numbers

# After this:

# print(numbers)

# would give NameError.


# Individual tuple elements cannot be deleted directly.


# 28. CHECKING IF A VALUE EXISTS

fruits = ("apple", "banana", "mango")

print("banana" in fruits)

# True


print("orange" in fruits)

# False


# 29. USING not in

fruits = ("apple", "banana", "mango")

print("orange" not in fruits)

# True


# 30. LOOPING THROUGH A TUPLE

fruits = ("apple", "banana", "mango")

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# mango


# 31. LOOPING USING INDEX

fruits = ("apple", "banana", "mango")

for i in range(len(fruits)):
    print(i, fruits[i])

# Output:
# 0 apple
# 1 banana
# 2 mango


# 32. USING enumerate()

fruits = ("apple", "banana", "mango")

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 mango


# 33. enumerate() STARTING FROM 1

fruits = ("apple", "banana", "mango")

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 mango


# 34. count()

# count() tells how many times a value appears.

numbers = (10, 20, 20, 20, 30)

print(numbers.count(20))

# Output:
# 3


# 35. index()

# index() returns the index of the first matching value.

fruits = ("apple", "banana", "mango")

print(fruits.index("banana"))

# Output:
# 1


# If the value is not present,
# index() gives ValueError.


# 36. SAFE USE OF index()

fruits = ("apple", "banana", "mango")

search = "banana"

if search in fruits:
    print(fruits.index(search))
else:
    print("Fruit not found")


# 37. min()

numbers = (5, 2, 8, 1)

print(min(numbers))

# Output:
# 1


# 38. max()

numbers = (5, 2, 8, 1)

print(max(numbers))

# Output:
# 8


# 39. sum()

numbers = (10, 20, 30)

print(sum(numbers))

# Output:
# 60


# 40. sorted()

numbers = (5, 2, 8, 1)

result = sorted(numbers)

print(result)

# Output:
# [1, 2, 5, 8]


# Important:
# sorted() returns a LIST.


# To get a tuple:

result = tuple(sorted(numbers))

print(result)

# Output:
# (1, 2, 5, 8)


# 41. TUPLES DO NOT HAVE sort()

numbers = (5, 2, 8, 1)

# numbers.sort()

# This is invalid.


# Correct:

sorted_numbers = tuple(sorted(numbers))

print(sorted_numbers)


# 42. TUPLES DO NOT HAVE reverse()

numbers = (1, 2, 3)

# numbers.reverse()

# This is invalid.


# Use slicing:

numbers = numbers[::-1]

print(numbers)

# Output:
# (3, 2, 1)


# 43. TUPLE PACKING

# Putting multiple values together is called packing.

student = "Alice", 20, "CSE"

print(student)

# Output:
# ('Alice', 20, 'CSE')


# 44. TUPLE UNPACKING

student = ("Alice", 20, "CSE")

name, age, course = student

print(name)
print(age)
print(course)

# Output:
# Alice
# 20
# CSE


# 45. UNPACKING RULE

numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)

# Output:
# 10
# 20
# 30


# Usually the number of variables must match
# the number of tuple elements.


# 46. EXTENDED UNPACKING

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)
print(middle)
print(last)

# Output:
# 10
# [20, 30, 40]
# 50


# Important:
# *middle becomes a LIST.


# 47. FIRST AND REMAINING VALUES

numbers = (10, 20, 30, 40)

first, *remaining = numbers

print(first)
print(remaining)

# Output:
# 10
# [20, 30, 40]


# 48. IGNORING VALUES USING _

student = ("Alice", 20, "CSE")

name, _, course = student

print(name)
print(course)

# Output:
# Alice
# CSE


# _ is commonly used when we do not need a value.


# 49. SWAPPING VARIABLES

a = 10
b = 20

a, b = b, a

print(a)
print(b)

# Output:
# 20
# 10


# Python uses packing and unpacking here.


# 50. TUPLES CAN STORE DIFFERENT DATA TYPES

data = ("Alice", 20, 85.5, True)

print(data)


# 51. TUPLE CONTAINING A LIST

student = (
    "Alice",
    [90, 85, 95]
)

print(student)


# 52. IMPORTANT: MUTABLE OBJECT INSIDE A TUPLE

# Tuple itself is immutable.
# But a mutable object inside it can still change.

student = (
    "Alice",
    [90, 85, 95]
)

student[1][0] = 100

print(student)

# Output:
# ('Alice', [100, 85, 95])


# The tuple was not replaced.
# The list inside the tuple was modified.


# 53. NESTED TUPLES

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

print(students)


# 54. ACCESSING NESTED TUPLES

students = (
    ("Alice", 90),
    ("Bob", 85)
)

print(students[0])

# ('Alice', 90)


print(students[0][0])

# Alice


print(students[0][1])

# 90


# 55. LOOPING THROUGH NESTED TUPLES

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

for student in students:
    print(student)


# 56. UNPACKING NESTED TUPLES IN A LOOP

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

for name, marks in students:
    print(name, marks)

# Output:
# Alice 90
# Bob 85
# Charlie 95


# 57. LIST OF TUPLES

students = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
]

print(students)


# 58. ACCESSING LIST OF TUPLES

students = [
    ("Alice", 90),
    ("Bob", 85)
]

print(students[0])

# ('Alice', 90)


print(students[0][0])

# Alice


# 59. CONVERTING TUPLE TO LIST

numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list)

# Output:
# [10, 20, 30]


# 60. CONVERTING LIST TO TUPLE

numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)

# Output:
# (10, 20, 30)


# 61. CONVERTING SET TO TUPLE

numbers_set = {1, 2, 3}

numbers_tuple = tuple(numbers_set)

print(numbers_tuple)

# Do not rely on set order.


# 62. JOINING TUPLE OF STRINGS

words = ("I", "love", "Python")

sentence = " ".join(words)

print(sentence)

# Output:
# I love Python


# join() requires strings.


# 63. split() AND TUPLES

sentence = "Python is easy"

words = sentence.split()

print(words)

# Output:
# ['Python', 'is', 'easy']


words_tuple = tuple(words)

print(words_tuple)

# Output:
# ('Python', 'is', 'easy')


# 64. USER INPUT INTO A TUPLE

data = input("Enter words separated by spaces: ")

words = tuple(data.split())

print(words)


# Example input:
# apple banana mango

# Output:
# ('apple', 'banana', 'mango')


# 65. MULTIPLE INTEGER INPUTS INTO A TUPLE

values = input("Enter numbers separated by spaces: ").split()

numbers = []

for value in values:
    numbers.append(int(value))

numbers_tuple = tuple(numbers)

print(numbers_tuple)


# Example input:
# 10 20 30

# Output:
# (10, 20, 30)


# 66. SHORTER USER INPUT USING map()

numbers = tuple(map(int, input("Enter numbers: ").split()))

print(numbers)


# 67. CHECKING IF TUPLE IS EMPTY

numbers = ()

if not numbers:
    print("Tuple is empty")


# Another way:

if len(numbers) == 0:
    print("Tuple is empty")


# 68. BOOLEAN VALUE OF A TUPLE

print(bool(()))

# False


print(bool((1, 2, 3)))

# True


# Empty tuple = False
# Non-empty tuple = True


# 69. COMPARING TUPLES

tuple1 = (1, 2, 3)

tuple2 = (1, 2, 3)

print(tuple1 == tuple2)

# True


# 70. ORDER MATTERS

tuple1 = (1, 2, 3)

tuple2 = (3, 2, 1)

print(tuple1 == tuple2)

# False


# 71. == VS is

tuple1 = tuple([1, 2, 3])

tuple2 = tuple([1, 2, 3])

print(tuple1 == tuple2)

# True


print(tuple1 is tuple2)

# Usually False


# == compares values.
# is checks whether both variables refer
# to the exact same object.


# 72. any()

values = (False, False, True)

print(any(values))

# True


# any() returns True if at least
# one element is truthy.


# 73. all()

values = (True, True, True)

print(all(values))

# True


values = (True, False, True)

print(all(values))

# False


# all() returns True only if
# every element is truthy.


# 74. TUPLES AS DICTIONARY KEYS

# Tuples can be dictionary keys
# if all their contents are hashable.

locations = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(locations[(10, 20)])

# Output:
# Point A


# 75. TUPLE WITH LIST CANNOT BE A DICTIONARY KEY

# This would be invalid:

# data = {
#     ([1, 2], 3): "value"
# }

# The tuple contains a list.
# Lists are unhashable.


# 76. FUNCTIONS RETURNING TUPLES

def get_student():
    return "Alice", 20


student = get_student()

print(student)

# Output:
# ('Alice', 20)


# Multiple returned values are packed
# into a tuple.


# 77. UNPACKING FUNCTION RETURN VALUES

def get_user():
    return "Alice", 20


name, age = get_user()

print(name)
print(age)

# Output:
# Alice
# 20


# 78. PASSING A TUPLE TO A FUNCTION

def show_student(student):
    print("Name:", student[0])
    print("Age:", student[1])


student = ("Alice", 20)

show_student(student)


# 79. UNPACKING FUNCTION ARGUMENTS USING *

def add(a, b):
    return a + b


numbers = (10, 20)

result = add(*numbers)

print(result)

# Output:
# 30


# *numbers changes:
# (10, 20)

# into:
# 10, 20


# 80. *args CREATES A TUPLE

def show_numbers(*numbers):
    print(numbers)


show_numbers(10, 20, 30)

# Output:
# (10, 20, 30)


# *args stores multiple positional arguments
# inside a tuple.


# 81. CHECKING TYPE

numbers = (1, 2, 3)

print(type(numbers))

# Output:
# <class 'tuple'>


print(isinstance(numbers, tuple))

# True


# 82. tuple() WITH range()

numbers = tuple(range(1, 6))

print(numbers)

# Output:
# (1, 2, 3, 4, 5)


# 83. reversed()

numbers = (1, 2, 3, 4)

reversed_numbers = tuple(reversed(numbers))

print(reversed_numbers)

# Output:
# (4, 3, 2, 1)


# 84. zip() WITH TUPLES

names = ("Alice", "Bob", "Charlie")

marks = (90, 85, 95)

for name, mark in zip(names, marks):
    print(name, mark)

# Output:
# Alice 90
# Bob 85
# Charlie 95


# 85. CONVERTING zip() INTO A TUPLE

names = ("Alice", "Bob")

marks = (90, 85)

students = tuple(zip(names, marks))

print(students)

# Output:
# (('Alice', 90), ('Bob', 85))


# 86. enumerate() AS A TUPLE

names = ("Alice", "Bob", "Charlie")

result = tuple(enumerate(names))

print(result)

# Output:
# ((0, 'Alice'), (1, 'Bob'), (2, 'Charlie'))


# 87. TUPLE VS LIST

numbers_list = [1, 2, 3]

numbers_tuple = (1, 2, 3)


# LIST

# Uses square brackets []

# Mutable

# Can change elements

# Has methods like:
# append()
# extend()
# insert()
# remove()
# pop()
# sort()
# reverse()


# TUPLE

# Usually uses parentheses ()

# Immutable

# Cannot directly change elements

# Has only two main methods:
# count()
# index()


# 88. TUPLE VS SET

numbers_tuple = (1, 2, 2, 3)

numbers_set = {1, 2, 2, 3}

print(numbers_tuple)

# (1, 2, 2, 3)


print(numbers_set)

# {1, 2, 3}


# Tuple:
# Ordered
# Allows duplicates
# Supports indexes


# Set:
# Stores unique values
# Does not support normal indexing


# 89. TUPLE VS DICTIONARY

student_tuple = ("Alice", 20)

student_dictionary = {
    "name": "Alice",
    "age": 20
}


# Tuple uses indexes:

print(student_tuple[0])


# Dictionary uses keys:

print(student_dictionary["name"])


# 90. TUPLE METHODS

# Tuples only have two main methods.


# count()

numbers = (1, 2, 2, 3)

print(numbers.count(2))


# index()

numbers = (10, 20, 30)

print(numbers.index(20))


# 91. FUNCTIONS COMMONLY USED WITH TUPLES

numbers = (10, 20, 30)


print(len(numbers))

# Number of elements


print(min(numbers))

# Smallest value


print(max(numbers))

# Largest value


print(sum(numbers))

# Total


print(sorted(numbers))

# Sorted LIST


print(tuple(sorted(numbers)))

# Sorted tuple


# 92. METHODS TUPLES DO NOT HAVE

# append()

# extend()

# insert()

# remove()

# pop()

# clear()

# sort()

# reverse()


# These methods change collections,
# but tuples are immutable.


# 93. COMMON ERROR: SINGLE ELEMENT TUPLE

wrong = (10)

print(type(wrong))

# <class 'int'>


correct = (10,)

print(type(correct))

# <class 'tuple'>


# Remember:
# The comma creates the tuple.


# 94. COMMON ERROR: CHANGING AN ELEMENT

numbers = (10, 20, 30)

# numbers[0] = 100

# TypeError


# Tuples are immutable.


# 95. COMMON ERROR: append()

numbers = (10, 20, 30)

# numbers.append(40)

# AttributeError


# Correct alternative:

numbers = numbers + (40,)

print(numbers)


# 96. COMMON ERROR: remove()

numbers = (10, 20, 30)

# numbers.remove(20)

# Invalid


# Alternative:

numbers_list = list(numbers)

numbers_list.remove(20)

numbers = tuple(numbers_list)

print(numbers)


# 97. COMMON ERROR: sort()

numbers = (3, 1, 2)

# numbers.sort()

# Invalid


# Correct:

numbers = tuple(sorted(numbers))

print(numbers)

# Output:
# (1, 2, 3)


# 98. COMMON ERROR: INDEX OUT OF RANGE

numbers = (10, 20, 30)

# print(numbers[5])

# IndexError


# Valid indexes:
# 0
# 1
# 2


# 99. COMMON ERROR: WRONG UNPACKING

numbers = (10, 20, 30)

# a, b = numbers

# ValueError


# Correct:

a, b, c = numbers


# Or:

first, *remaining = numbers

print(first)
print(remaining)


# 100. PRACTICAL EXAMPLE: COORDINATES

point = (10, 20)

x, y = point

print("X:", x)
print("Y:", y)


# 101. PRACTICAL EXAMPLE: RGB COLOR

color = (255, 128, 0)

red, green, blue = color

print("Red:", red)
print("Green:", green)
print("Blue:", blue)


# 102. PRACTICAL EXAMPLE: DATE

date = (4, 9, 2026)

day, month, year = date

print("Day:", day)
print("Month:", month)
print("Year:", year)


# 103. PRACTICAL EXAMPLE: STUDENT RECORD

student = (
    "Alice",
    20,
    "CSE",
    95
)

name, age, course, marks = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)


# 104. PRACTICAL EXAMPLE: MULTIPLE STUDENTS

students = (
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
)

for name, marks in students:
    print(f"{name}: {marks}")


# 105. WHEN SHOULD YOU USE A TUPLE?

# Use a tuple when:

# The data should not change.

# The values belong together.

# You want a fixed collection.

# You want to return multiple values
# from a function.

# You need a suitable immutable value
# as a dictionary key.


# 106. WHEN SHOULD YOU USE A LIST?

# Use a list when:

# You need to add elements.

# You need to remove elements.

# You need to change elements.

# You need to sort the collection in place.

# The size of the collection changes often.


# 107. QUICK TUPLE CHEAT SHEET

numbers = (10, 20, 30)


# First element

print(numbers[0])


# Last element

print(numbers[-1])


# Slice

print(numbers[0:2])


# Length

print(len(numbers))


# Check value

print(20 in numbers)


# Count value

print(numbers.count(20))


# Find index

print(numbers.index(20))


# Loop

for number in numbers:
    print(number)


# Add another tuple

numbers = numbers + (40,)


# Reverse

reversed_numbers = numbers[::-1]


# Convert tuple to list

numbers_list = list(numbers)


# Convert list to tuple

numbers_tuple = tuple(numbers_list)


# Sort and convert back into tuple

sorted_numbers = tuple(sorted(numbers))


# 108. MOST IMPORTANT THINGS TO REMEMBER

# Tuples are ordered.

# Tuples are immutable.

# Tuples allow duplicates.

# Tuples support indexing.

# Tuples support slicing.

# Indexing starts from 0.

# -1 means the last element.

# A single-element tuple needs a comma.

# Correct:
# (10,)

# Incorrect:
# (10)


# Tuple packing:

numbers = 10, 20, 30


# Tuple unpacking:

a, b, c = numbers


# Tuples do not have append().

# Tuples do not have extend().

# Tuples do not have insert().

# Tuples do not have remove().

# Tuples do not have pop().

# Tuples do not have sort().

# Tuples do not have reverse().


# Tuple methods:

# count()
# index()


# Useful functions:

# len()
# min()
# max()
# sum()
# sorted()
# tuple()
# list()
# any()
# all()
# enumerate()
# zip()


# 109. FINAL BEGINNER EXAMPLE

student = (
    "Alice",
    20,
    "CSE",
    95
)

name, age, course, marks = student

print("Student Details")
print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Marks:", marks)

if "CSE" in student:
    print("Course found")

student_list = list(student)

student_list[3] = 98

student = tuple(student_list)

print("Updated tuple:", student)


# END OF PYTHON TUPLE NOTES