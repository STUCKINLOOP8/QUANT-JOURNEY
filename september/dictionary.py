# PYTHON DICTIONARIES

# Dictionaries are used to store data in key-value pairs.

# 1. WHAT IS A DICTIONARY?

# A dictionary stores data in pairs.

# Each pair contains:

# key : value

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

print(student)

# Output:

# {'name': 'Alice', 'age': 20, 'course': 'CSE'}

# 2. IMPORTANT PROPERTIES OF DICTIONARIES

# Dictionaries:

# Store data as key-value pairs.

# Are mutable.

# Do not allow duplicate keys.

# Can contain different data types.

# Preserve insertion order in modern Python.

# Access values using keys instead of indexes.

# 3. CREATING A DICTIONARY

student = {
"name": "Alice",
"age": 20,
"marks": 95
}

print(student)

# 4. CREATING AN EMPTY DICTIONARY

student = {}

print(student)

# Another way:

student = dict()

print(student)

# 5. USING dict() TO CREATE A DICTIONARY

student = dict(
name="Alice",
age=20,
marks=95
)

print(student)

# Output:

# {'name': 'Alice', 'age': 20, 'marks': 95}

# 6. KEYS AND VALUES

student = {
"name": "Alice",
"age": 20
}

# "name" is a key.

# "Alice" is its value.

# "age" is a key.

# 20 is its value.

# 7. ACCESSING VALUES USING KEYS

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

print(student["name"])

# Output:

# Alice

print(student["age"])

# Output:

# 20

# 8. IMPORTANT: DICTIONARIES DO NOT USE NORMAL INDEXING

student = {
"name": "Alice",
"age": 20
}

# This is incorrect if there is no key 0:

# print(student[0])

# Dictionaries normally use keys:

print(student["name"])

# 9. ACCESSING VALUES USING get()

student = {
"name": "Alice",
"age": 20
}

print(student.get("name"))

# Output:

# Alice

# 10. DIFFERENCE BETWEEN [] AND get()

student = {
"name": "Alice",
"age": 20
}

# Using square brackets:

print(student["name"])

# If the key does not exist:

# print(student["course"])

# Python gives:

# KeyError

# Using get():

print(student.get("course"))

# Output:

# None

# get() is safer when you are not sure whether a key exists.

# 11. DEFAULT VALUE WITH get()

student = {
"name": "Alice"
}

print(student.get("age", "Not Found"))

# Output:

# Not Found

# Syntax:

# dictionary.get(key, default_value)

# 12. ADDING A NEW KEY-VALUE PAIR

student = {
"name": "Alice",
"age": 20
}

student["course"] = "CSE"

print(student)

# Output:

# {'name': 'Alice', 'age': 20, 'course': 'CSE'}

# 13. UPDATING AN EXISTING VALUE

student = {
"name": "Alice",
"age": 20
}

student["age"] = 21

print(student)

# Output:

# {'name': 'Alice', 'age': 21}

# 14. ADDING VS UPDATING

student = {
"name": "Alice"
}

# If key does not exist:

# A new key-value pair is added.

student["age"] = 20

# If key already exists:

# Its value is changed.

student["age"] = 21

print(student)

# 15. update()

# update() can add or update multiple key-value pairs.

student = {
"name": "Alice",
"age": 20
}

student.update({
"age": 21,
"course": "CSE"
})

print(student)

# Output:

# {'name': 'Alice', 'age': 21, 'course': 'CSE'}

# 16. UPDATE USING KEYWORD ARGUMENTS

student = {
"name": "Alice"
}

student.update(age=20, course="CSE")

print(student)

# 17. REMOVING ITEMS USING pop()

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

student.pop("age")

print(student)

# Output:

# {'name': 'Alice', 'course': 'CSE'}

# pop() also returns the removed value.

student = {
"name": "Alice",
"age": 20
}

removed_value = student.pop("age")

print(removed_value)

# Output:

# 20

# 18. pop() WITH A DEFAULT VALUE

student = {
"name": "Alice"
}

value = student.pop("age", "Not Found")

print(value)

# Output:

# Not Found

# This prevents KeyError if the key does not exist.

# 19. popitem()

# popitem() removes and returns the last inserted key-value pair.

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

removed = student.popitem()

print(removed)

# Output:

# ('course', 'CSE')

print(student)

# Output:

# {'name': 'Alice', 'age': 20}

# 20. REMOVING ITEMS USING del

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

del student["age"]

print(student)

# Output:

# {'name': 'Alice', 'course': 'CSE'}

# 21. DELETING THE COMPLETE DICTIONARY

student = {
"name": "Alice"
}

del student

# After this:

# print(student)

# would give NameError.

# 22. clear()

# clear() removes all key-value pairs.

student = {
"name": "Alice",
"age": 20
}

student.clear()

print(student)

# Output:

# {}

# Difference:

# clear()

# Keeps the dictionary variable but removes all items.

# del dictionary_name

# Deletes the variable completely.

# 23. CHECKING IF A KEY EXISTS

student = {
"name": "Alice",
"age": 20
}

print("name" in student)

# True

print("course" in student)

# False

# 24. USING not in

student = {
"name": "Alice"
}

print("age" not in student)

# True

# 25. IMPORTANT: in CHECKS KEYS

student = {
"name": "Alice",
"age": 20
}

print("name" in student)

# True

print("Alice" in student)

# False

# By default, 'in' checks keys, not values.

# 26. CHECKING IF A VALUE EXISTS

student = {
"name": "Alice",
"age": 20
}

print("Alice" in student.values())

# True

print(20 in student.values())

# True

# 27. len()

# len() tells how many key-value pairs exist.

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

print(len(student))

# Output:

# 3

# 28. keys()

# keys() gives all dictionary keys.

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

print(student.keys())

# Output:

# dict_keys(['name', 'age', 'course'])

# 29. values()

# values() gives all dictionary values.

print(student.values())

# Output:

# dict_values(['Alice', 20, 'CSE'])

# 30. items()

# items() gives key-value pairs.

print(student.items())

# Output:

# dict_items([

# ('name', 'Alice'),

# ('age', 20),

# ('course', 'CSE')

# ])

# 31. LOOPING THROUGH A DICTIONARY

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

for key in student:
  print(key)

# Output:

# name

# age

# course

# 32. LOOPING THROUGH KEYS

student = {
"name": "Alice",
"age": 20
}

for key in student.keys():
  print(key)

# Same as:

for key in student:
  print(key)

# 33. LOOPING THROUGH VALUES

student = {
"name": "Alice",
"age": 20
}

for value in student.values():
  print(value)

# Output:

# Alice

# 20

# 34. LOOPING THROUGH KEYS AND VALUES

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

for key, value in student.items():
  print(key, value)

# Output:

# name Alice

# age 20

# course CSE

# 35. PRINTING KEY-VALUE PAIRS NICELY

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

for key, value in student.items():
  print(f"{key}: {value}")

# Output:

# name: Alice

# age: 20

# course: CSE

# 36. DICTIONARY KEYS MUST BE UNIQUE

student = {
"name": "Alice",
"name": "Bob"
}

print(student)

# Output:

# {'name': 'Bob'}

# The last value replaces the earlier value

# because duplicate keys are not allowed.

# 37. VALUES CAN BE DUPLICATED

students = {
"student1": "Alice",
"student2": "Alice"
}

print(students)

# Duplicate values are allowed.

# 38. DICTIONARY VALUES CAN HAVE DIFFERENT DATA TYPES

student = {
"name": "Alice",
"age": 20,
"height": 5.6,
"is_student": True
}

print(student)

# 39. DICTIONARY VALUES CAN ALSO BE LISTS

student = {
"name": "Alice",
"subjects": ["Python", "Maths", "Physics"]
}

print(student["subjects"])

# Output:

# ['Python', 'Maths', 'Physics']

# Accessing a list element:

print(student["subjects"][0])

# Output:

# Python

# 40. DICTIONARY VALUES CAN ALSO BE DICTIONARIES

student = {
"name": "Alice",
"marks": {
"maths": 90,
"python": 95
}
}

print(student["marks"])

# Output:

# {'maths': 90, 'python': 95}

# Accessing nested dictionary data:

print(student["marks"]["python"])

# Output:

# 95

# 41. NESTED DICTIONARIES

students = {
"student1": {
"name": "Alice",
"age": 20
},
"student2": {
"name": "Bob",
"age": 21
}
}

print(students)

# 42. ACCESSING NESTED DICTIONARY VALUES

students = {
"student1": {
"name": "Alice",
"age": 20
},
"student2": {
"name": "Bob",
"age": 21
}
}

print(students["student1"]["name"])

# Output:

# Alice

print(students["student2"]["age"])

# Output:

# 21

# 43. LOOPING THROUGH NESTED DICTIONARIES

students = {
"student1": {
"name": "Alice",
"age": 20
},
"student2": {
"name": "Bob",
"age": 21
}
}

for student_id, details in students.items():
  print(student_id)

for key, value in details.items():
    print(key, value)

# 44. COPYING A DICTIONARY

student = {
"name": "Alice",
"age": 20
}

student_copy = student.copy()

print(student_copy)

# 45. ANOTHER WAY TO COPY

student = {
"name": "Alice",
"age": 20
}

student_copy = dict(student)

print(student_copy)

# 46. IMPORTANT: ASSIGNMENT IS NOT COPYING

student1 = {
"name": "Alice"
}

student2 = student1

student2["age"] = 20

print(student1)

# Output:

# {'name': 'Alice', 'age': 20}

print(student2)

# Output:

# {'name': 'Alice', 'age': 20}

# Both variables point to the same dictionary.

# Proper copy:

student1 = {
"name": "Alice"
}

student2 = student1.copy()

student2["age"] = 20

print(student1)

# {'name': 'Alice'}

print(student2)

# {'name': 'Alice', 'age': 20}

# 47. SHALLOW COPY

student = {
"name": "Alice",
"marks": {
"maths": 90,
"python": 95
}
}

student_copy = student.copy()

student_copy["marks"]["maths"] = 100

print(student)

# The nested dictionary is also affected.

# copy() creates a shallow copy.

# 48. DEEP COPY

import copy

student = {
"name": "Alice",
"marks": {
"maths": 90,
"python": 95
}
}

student_copy = copy.deepcopy(student)

student_copy["marks"]["maths"] = 100

print(student["marks"]["maths"])

# Output:

# 90

print(student_copy["marks"]["maths"])

# Output:

# 100

# deepcopy() creates independent nested objects.

# 49. fromkeys()

# fromkeys() creates a dictionary using given keys.

keys = ["name", "age", "course"]

student = dict.fromkeys(keys)

print(student)

# Output:

# {'name': None, 'age': None, 'course': None}

# 50. fromkeys() WITH A DEFAULT VALUE

keys = ["maths", "python", "physics"]

marks = dict.fromkeys(keys, 0)

print(marks)

# Output:

# {'maths': 0, 'python': 0, 'physics': 0}

# 51. setdefault()

# setdefault() returns the value of a key.

student = {
"name": "Alice"
}

value = student.setdefault("name", "Unknown")

print(value)

# Output:

# Alice

# If the key does not exist,

# it adds the key with the given default value.

student.setdefault("age", 20)

print(student)

# Output:

# {'name': 'Alice', 'age': 20}

# 52. get() VS setdefault()

student = {
"name": "Alice"
}

print(student.get("age", 20))

# Output:

# 20

print(student)

# Output:

# {'name': 'Alice'}

# get() does NOT add the missing key.

student.setdefault("age", 20)

print(student)

# Output:

# {'name': 'Alice', 'age': 20}

# setdefault() can add the missing key.

# 53. DICTIONARY COMPREHENSION

# Dictionary comprehension is a shorter way

# to create dictionaries.

numbers = [1, 2, 3, 4, 5]

squares = {
number: number ** 2
for number in numbers
}

print(squares)

# Output:

# {

# 1: 1,

# 2: 4,

# 3: 9,

# 4: 16,

# 5: 25

# }

# 54. NORMAL VERSION OF DICTIONARY COMPREHENSION

numbers = [1, 2, 3, 4, 5]

squares = {}

for number in numbers:
  squares[number] = number ** 2

print(squares)

# 55. DICTIONARY COMPREHENSION WITH CONDITION

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
number: number ** 2
for number in numbers
if number % 2 == 0
}

print(even_squares)

# Output:

# {2: 4, 4: 16, 6: 36}

# 56. CREATING A DICTIONARY FROM TWO LISTS USING zip()

names = ["Alice", "Bob", "Charlie"]

marks = [90, 85, 95]

students = dict(zip(names, marks))

print(students)

# Output:

# {

# 'Alice': 90,

# 'Bob': 85,

# 'Charlie': 95

# }

# 57. LOOPING THROUGH TWO LISTS WITH zip()

names = ["Alice", "Bob"]

marks = [90, 85]

for name, mark in zip(names, marks):
  print(name, mark)

# Output:

# Alice 90

# Bob 85

# 58. CONVERTING DICTIONARY KEYS TO A LIST

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

keys = list(student.keys())

print(keys)

# Output:

# ['name', 'age', 'course']

# 59. CONVERTING DICTIONARY VALUES TO A LIST

values = list(student.values())

print(values)

# Output:

# ['Alice', 20, 'CSE']

# 60. CONVERTING DICTIONARY ITEMS TO A LIST

items = list(student.items())

print(items)

# Output:

# [('name', 'Alice'), ('age', 20), ('course', 'CSE')]

# 61. CREATING A DICTIONARY FROM PAIRS

data = [
("name", "Alice"),
("age", 20),
("course", "CSE")
]

student = dict(data)

print(student)

# Output:

# {'name': 'Alice', 'age': 20, 'course': 'CSE'}

# 62. USER INPUT WITH DICTIONARIES

student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["course"] = input("Enter course: ")

print(student)

# 63. DISPLAYING USER DATA

student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))

print("Student Details")

for key, value in student.items():
  print(f"{key}: {value}")

# 64. SEARCHING FOR A KEY

student = {
    "name": "Alice",
    "age": 20
}

search_key = input("Enter key to search: ")

if search_key in student:
    print("Key found")
    print("Value:", student[search_key])
else:
    print("Key not found")

# 65. SEARCHING FOR A VALUE
student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

search_value = input("Enter value to search: ")

if search_value in student.values():
  print("Value found")
else:
  print("Value not found")

# Important:

# input() returns strings.

# Searching for numeric values may require conversion.

# 66. SAFELY ACCESSING A KEY

student = {
"name": "Alice"
}

key = "age"

if key in student:
  print(student[key])
else:
  print("Key not found")

# Another way:

print(student.get(key, "Key not found"))

# 67. SAFELY REMOVING A KEY

student = {
"name": "Alice",
"age": 20
}

key = "age"

if key in student:
  student.pop(key)
else:
  print("Key not found")

print(student)

# 68. EMPTY DICTIONARY CHECK

student = {}

if not student:
  print("Dictionary is empty")

# Another way:

if len(student) == 0:
  print("Dictionary is empty")

# Usually:

# if not student:

# is simpler.

# 69. BOOLEAN VALUE OF DICTIONARIES

print(bool({}))

# False

print(bool({"name": "Alice"}))

# True

# Empty dictionary = False

# Non-empty dictionary = True

# 70. COMPARING DICTIONARIES

student1 = {
"name": "Alice",
"age": 20
}

student2 = {
"name": "Alice",
"age": 20
}

print(student1 == student2)

# True

# Dictionary equality compares key-value pairs.

# 71. ORDER DOES NOT AFFECT DICTIONARY EQUALITY

student1 = {
"name": "Alice",
"age": 20
}

student2 = {
"age": 20,
"name": "Alice"
}

print(student1 == student2)

# True

# 72. == VS is

student1 = {
"name": "Alice"
}

student2 = {
"name": "Alice"
}

print(student1 == student2)

# True

print(student1 is student2)

# False

# == checks whether values are equal.

# is checks whether both variables point

# to the exact same object.

# 73. WHAT TYPES CAN BE DICTIONARY KEYS?

# Dictionary keys must be hashable.

# Common valid key types:

# string

# integer

# float

# boolean

# tuple containing hashable values

example = {
"name": "Alice",
1: "one",
2.5: "float key",
True: "boolean key"
}

print(example)

# 74. LISTS CANNOT BE DICTIONARY KEYS

# This is invalid:

# example = {

# [1, 2]: "value"

# }

# Python gives:

# TypeError: unhashable type: 'list'

# Lists are mutable and cannot normally be keys.

# 75. DICTIONARIES CANNOT BE KEYS

# This is also invalid:

# example = {

# {"a": 1}: "value"

# }

# 76. TUPLES CAN SOMETIMES BE KEYS

coordinates = {
(10, 20): "Point A",
(30, 40): "Point B"
}

print(coordinates[(10, 20)])

# Output:

# Point A

# 77. BOOLEAN AND INTEGER KEY BEHAVIOR

example = {
True: "yes",
1: "one"
}

print(example)

# True and 1 compare as equal in Python,

# so they can behave as the same key.

# 78. COMMON ERROR: KeyError

student = {
"name": "Alice"
}

# print(student["age"])

# Gives:

# KeyError: 'age'

# Safer options:

print(student.get("age"))

# None

print(student.get("age", "Not Found"))

# Not Found

# 79. COMMON ERROR: USING INDEXES

student = {
"name": "Alice",
"age": 20
}

# Incorrect:

# print(student[0])

# Correct:

print(student["name"])

# 80. COMMON ERROR: DUPLICATE KEYS

student = {
"name": "Alice",
"name": "Bob"
}

print(student)

# {'name': 'Bob'}

# The earlier value is replaced.

# 81. COMMON ERROR: MODIFYING DICTIONARY SIZE WHILE LOOPING

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

# Avoid doing this:

# for key in student:

# if key == "age":

# del student[key]

# This may give:

# RuntimeError:

# dictionary changed size during iteration

# 82. SAFE WAY TO DELETE WHILE LOOPING

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

for key in list(student.keys()):
  if key == "age":
    del student[key]

print(student)

# 83. MODIFYING VALUES WHILE LOOPING

marks = {
"maths": 80,
"python": 90,
"physics": 70
}

for subject in marks:
  marks[subject] = marks[subject] + 5

print(marks)

# Modifying existing values is generally fine.

# Adding or deleting keys during iteration

# should be handled carefully.

# 84. keys(), values(), AND items() ARE VIEW OBJECTS

student = {
"name": "Alice",
"age": 20
}

keys = student.keys()

print(keys)

student["course"] = "CSE"

print(keys)

# The view reflects current dictionary contents.

# 85. CONVERTING VIEWS INTO LISTS

student = {
"name": "Alice",
"age": 20
}

keys = list(student.keys())

values = list(student.values())

items = list(student.items())

print(keys)
print(values)
print(items)

# 86. SORTING DICTIONARY KEYS

marks = {
"python": 95,
"maths": 90,
"physics": 85
}

for subject in sorted(marks):
  print(subject)

# sorted(marks) sorts the keys.

# 87. SORTING DICTIONARY ITEMS BY KEY

marks = {
"python": 95,
"maths": 90,
"physics": 85
}

for key, value in sorted(marks.items()):
  print(key, value)

# 88. SORTING BY VALUES

marks = {
"python": 95,
"maths": 90,
"physics": 85
}

sorted_marks = sorted(
marks.items(),
key=lambda item: item[1]
)

print(sorted_marks)

# Output:

# [('physics', 85), ('maths', 90), ('python', 95)]

# lambda is an anonymous function.

# You can understand it better later.

# 89. max() WITH DICTIONARIES

marks = {
"python": 95,
"maths": 90,
"physics": 85
}

print(max(marks))

# max() checks dictionary keys by default.

# To find the key with the highest value:

highest_subject = max(
marks,
key=marks.get
)

print(highest_subject)

# Output:

# python

# 90. min() WITH DICTIONARIES

lowest_subject = min(
marks,
key=marks.get
)

print(lowest_subject)

# Output:

# physics

# 91. sum() WITH DICTIONARY VALUES

marks = {
"python": 95,
"maths": 90,
"physics": 85
}

total = sum(marks.values())

print(total)

# Output:

# 270

# 92. AVERAGE OF DICTIONARY VALUES

marks = {
"python": 95,
"maths": 90,
"physics": 85
}

average = sum(marks.values()) / len(marks)

print(average)

# 93. CHECKING MULTIPLE CONDITIONS

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

if "name" in student and "age" in student:
  print("Required details are present")

# 94. MERGING DICTIONARIES USING update()

dict1 = {
"name": "Alice",
"age": 20
}

dict2 = {
"course": "CSE",
"marks": 95
}

dict1.update(dict2)

print(dict1)

# 95. MERGING DICTIONARIES USING |

# Modern Python supports the | operator.

dict1 = {
"name": "Alice",
"age": 20
}

dict2 = {
"course": "CSE",
"marks": 95
}

merged = dict1 | dict2

print(merged)

# dict1 and dict2 remain unchanged.

# 96. MERGING WITH OVERLAPPING KEYS

dict1 = {
"name": "Alice",
"age": 20
}

dict2 = {
"age": 21,
"course": "CSE"
}

merged = dict1 | dict2

print(merged)

# Output:

# {

# 'name': 'Alice',

# 'age': 21,

# 'course': 'CSE'

# }

# The later dictionary value wins.

# 97. |= OPERATOR

student = {
"name": "Alice"
}

student |= {
"age": 20,
"course": "CSE"
}

print(student)

# 98. DICTIONARY UNPACKING USING **

dict1 = {
"name": "Alice"
}

dict2 = {
"age": 20
}

student = {
**dict1,
**dict2
}

print(student)

# Output:

# {'name': 'Alice', 'age': 20}

# 99. USING ** WITH FUNCTIONS

def display_student(name, age):
  print(name)
  print(age)

student = {
"name": "Alice",
"age": 20
}

display_student(**student)

# This works because dictionary keys match

# the function parameter names.

# 100. DICTIONARY AS FUNCTION ARGUMENT

def show_student(student):
  print(student["name"])
print(student["age"])

student = {
"name": "Alice",
"age": 20
}

show_student(student)

# 101. FUNCTION RETURNING A DICTIONARY

def create_student(name, age):
  student = {
"name": name,
"age": age
}
  return student

student1 = create_student("Alice", 20)

print(student1)

# 102. LIST OF DICTIONARIES

students = [
{
"name": "Alice",
"age": 20
},
{
"name": "Bob",
"age": 21
},
{
"name": "Charlie",
"age": 22
}
]

print(students)

# 103. ACCESSING A LIST OF DICTIONARIES

students = [
{
"name": "Alice",
"age": 20
},
{
"name": "Bob",
"age": 21
}
]

print(students[0])

# {'name': 'Alice', 'age': 20}

print(students[0]["name"])

# Alice

print(students[1]["age"])

# 21

# 104. LOOPING THROUGH A LIST OF DICTIONARIES

students = [
{
"name": "Alice",
"age": 20
},
{
"name": "Bob",
"age": 21
}
]

for student in students:
  print(student["name"])
print(student["age"])

# 105. PRACTICAL EXAMPLE: STUDENT DETAILS

student = {
"name": "Alice",
"age": 20,
"course": "CSE",
"marks": 95
}

print("Student Details")

for key, value in student.items():
  print(f"{key}: {value}")

# 106. PRACTICAL EXAMPLE: PHONE BOOK

phone_book = {
"Alice": "9876543210",
"Bob": "9123456780",
"Charlie": "9988776655"
}

name = input("Enter name: ")

if name in phone_book:
  print("Phone:", phone_book[name])
else:
  print("Contact not found")

# 107. PRACTICAL EXAMPLE: ADDING A CONTACT

phone_book = {}

name = input("Enter name: ")
phone = input("Enter phone number: ")

phone_book[name] = phone

print(phone_book)

# 108. PRACTICAL EXAMPLE: INVENTORY

inventory = {
"apple": 10,
"banana": 20,
"mango": 15
}

item = input("Enter item name: ")

if item in inventory:
  print("Quantity:", inventory[item])
else:
  print("Item not found")

# 109. PRACTICAL EXAMPLE: UPDATE QUANTITY

inventory = {
"apple": 10,
"banana": 20
}

item = input("Enter item: ")

if item in inventory:
  quantity = int(input("Enter new quantity: "))
  inventory[item] = quantity
else:
  print("Item does not exist")

print(inventory)

# 110. PRACTICAL EXAMPLE: COUNTING USING A DICTIONARY

text = "apple"

character_count = {}

for character in text:
  if character in character_count:
    character_count[character] += 1
else:
  character_count[character] = 1

print(character_count)

# Output:

# {

# 'a': 1,

# 'p': 2,

# 'l': 1,

# 'e': 1

# }

# This is only an example of dictionary usage,

# not a DSA problem.

# 111. SIMPLER COUNTING USING get()

text = "apple"

character_count = {}

for character in text:
  character_count[character] = character_count.get(character, 0) + 1

print(character_count)

# get(character, 0) means:

# If character exists, use its current value.

# Otherwise use 0.

# 112. COMMON DICTIONARY METHODS

# clear()

# Removes all items.

# copy()

# Creates a shallow copy.

# fromkeys()

# Creates a dictionary from keys.

# get()

# Returns a value safely.

# items()

# Returns key-value pairs.

# keys()

# Returns keys.

# pop()

# Removes a key and returns its value.

# popitem()

# Removes and returns the last inserted pair.

# setdefault()

# Returns value and can create missing key.

# update()

# Adds or updates key-value pairs.

# values()

# Returns values.

# 113. COMMON FUNCTIONS USED WITH DICTIONARIES

# len(dictionary)

# Number of key-value pairs.

# dict()

# Creates a dictionary.

# list(dictionary)

# Converts dictionary keys to a list.

# sorted(dictionary)

# Returns sorted keys.

# min(dictionary)

# Returns minimum key.

# max(dictionary)

# Returns maximum key.

# sum(dictionary.values())

# Adds numeric values.

# 114. QUICK METHOD EXAMPLES

student = {
"name": "Alice",
"age": 20
}

# Access

print(student["name"])

# Safe access

print(student.get("name"))

# Add

student["course"] = "CSE"

# Update

student["age"] = 21

# Multiple updates

student.update({
"marks": 95,
"city": "Delhi"
})

# Keys

print(student.keys())

# Values

print(student.values())

# Items

print(student.items())

# Remove

student.pop("city")

# Copy

student_copy = student.copy()

# Length

print(len(student))

# Loop

for key, value in student.items():
  print(key, value)

# 115. COMMON BEGINNER MISTAKES

# Mistake 1:

# Trying to access a missing key with [].

student = {
"name": "Alice"
}

# print(student["age"])

# KeyError

# Better:

print(student.get("age"))

# Mistake 2:

# Thinking dictionaries use list-style indexes.

# student[0]

# Normally incorrect unless 0 itself is a key.

# Mistake 3:

# Creating duplicate keys.

student = {
"name": "Alice",
"name": "Bob"
}

# Only the latest value remains.

# Mistake 4:

# Using a mutable object as a key.

# Lists and dictionaries cannot normally be dictionary keys.

# Mistake 5:

# Thinking 'in' checks values.

student = {
"name": "Alice"
}

print("name" in student)

# True

print("Alice" in student)

# False

# To check values:

print("Alice" in student.values())

# True

# Mistake 6:

# Thinking assignment creates a copy.

student1 = {
"name": "Alice"
}

student2 = student1

# Both refer to the same dictionary.

# Mistake 7:

# Deleting keys while directly looping

# through the dictionary.

# Use list(dictionary.keys()) if necessary.

# 116. DICTIONARY VS LIST

student_list = [
"Alice",
20,
"CSE"
]

student_dict = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

# List:

# Access values using indexes.

print(student_list[0])

# Dictionary:

# Access values using keys.

print(student_dict["name"])

# Dictionary data is often more readable

# when values have clear labels.

# 117. DICTIONARY VS SET

student = {
"name": "Alice",
"age": 20
}

numbers = {
1,
2,
3
}

# Dictionary uses:

# key : value

# Set stores only unique values.

# Empty dictionary:

empty_dict = {}

print(type(empty_dict))

# <class 'dict'>

# Empty set:

empty_set = set()

print(type(empty_set))

# <class 'set'>

# 118. DICTIONARY VS TUPLE

student = {
"name": "Alice",
"age": 20
}

student_tuple = (
"Alice",
20
)

# Dictionary:

# Mutable.

# Uses key-value pairs.

# Tuple:

# Ordered.

# Usually immutable.

# Uses positions/indexes.

# 119. TYPE CHECKING

student = {
"name": "Alice"
}

print(type(student))

# <class 'dict'>

print(isinstance(student, dict))

# True

# 120. DICTIONARY MUTABILITY

student = {
"name": "Alice"
}

student["name"] = "Bob"

print(student)

# Output:

# {'name': 'Bob'}

# Dictionaries are mutable.

# 121. KEYS SHOULD USUALLY HAVE CLEAR NAMES

# Better:

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

# Harder to understand:

student = {
"a": "Alice",
"b": 20,
"c": "CSE"
}

# Use meaningful key names whenever possible.

# 122. STRING KEYS ARE VERY COMMON

user = {
"username": "alice123",
"email": "[alice@example.com](mailto:alice@example.com)",
"active": True
}

print(user)

# 123. DICTIONARY WITH NONE VALUES

student = {
"name": "Alice",
"phone": None
}

print(student["phone"])

# Output:

# None

# None usually represents the absence of a value.

# 124. CHECKING FOR None

student = {
"name": "Alice",
"phone": None
}

if student["phone"] is None:
  print("Phone number not provided")

# 125. get() AND None

student = {
"name": "Alice"
}

print(student.get("phone"))

# None

# Important:

# get() returning None can mean:

#

# 1. The key does not exist.

# 2. The key exists and its value is None.

# Example:

student = {
"phone": None
}

print(student.get("phone"))

# None

# To know whether the key actually exists:

if "phone" in student:
  print("Phone key exists")

# 126. MULTIPLE LEVEL NESTING

company = {
"employees": {
"employee1": {
"name": "Alice",
"skills": [
"Python",
"SQL"
]
}
}
}

print(
company["employees"]["employee1"]["skills"][0]
)

# Output:

# Python

# 127. READING NESTED DATA SAFELY

student = {
"name": "Alice",
"marks": {
"python": 95
}
}

marks = student.get("marks", {})

python_marks = marks.get("python", 0)

print(python_marks)

# Output:

# 95

# 128. DICTIONARY COMPREHENSION EXAMPLE

names = [
"Alice",
"Bob",
"Charlie"
]

name_lengths = {
name: len(name)
for name in names
}

print(name_lengths)

# Output:

# {

# 'Alice': 5,

# 'Bob': 3,

# 'Charlie': 7

# }

# 129. TRANSFORMING DICTIONARY VALUES

marks = {
"maths": 80,
"python": 90,
"physics": 70
}

updated_marks = {
subject: mark + 5
for subject, mark in marks.items()
}

print(updated_marks)

# Original dictionary remains unchanged.

# 130. FILTERING A DICTIONARY

marks = {
"maths": 80,
"python": 95,
"physics": 70,
"english": 92
}

high_marks = {
subject: mark
for subject, mark in marks.items()
if mark >= 90
}

print(high_marks)

# Output:

# {'python': 95, 'english': 92}

# 131. UNPACKING KEYS AND VALUES

student = {
"name": "Alice",
"age": 20
}

for key, value in student.items():
  print("Key:", key)
print("Value:", value)

# items() gives pairs like:

# ('name', 'Alice')

# Python can unpack them into:

# key, value

# 132. PRACTICAL EXAMPLE: MARKS SYSTEM

marks = {
"maths": 90,
"python": 95,
"physics": 85
}

print("Marks")

for subject, mark in marks.items():
  print(f"{subject}: {mark}")

total = sum(marks.values())

average = total / len(marks)

print("Total:", total)
print("Average:", average)

# 133. PRACTICAL EXAMPLE: SIMPLE USER PROFILE

user = {}

user["name"] = input("Enter your name: ")
user["age"] = int(input("Enter your age: "))
user["city"] = input("Enter your city: ")

print("User Profile")

for key, value in user.items():
  print(f"{key}: {value}")

# 134. PRACTICAL EXAMPLE: PRODUCT DETAILS

product = {
"name": "Laptop",
"price": 50000,
"stock": 10
}

print("Product:", product["name"])
print("Price:", product["price"])
print("Stock:", product["stock"])

# 135. QUICK DICTIONARY SYNTAX SUMMARY

# Create dictionary

student = {
"name": "Alice",
"age": 20
}

# Access value

student["name"]

# Safe access

student.get("name")

# Add value

student["course"] = "CSE"

# Update value

student["age"] = 21

# Add multiple values

student.update({
"marks": 95,
"city": "Delhi"
})

# Check key

if "name" in student:
  print("Found")

# Check value

if "Alice" in student.values():
  print("Found")

# Get keys

student.keys()

# Get values

student.values()

# Get items

student.items()

# Remove key

student.pop("city")

# Remove last inserted pair

student.popitem()

# Delete key

del student["marks"]

# Copy

student_copy = student.copy()

# Length

len(student)

# Clear

student.clear()

# 136. MOST IMPORTANT THINGS TO REMEMBER

# Dictionaries use curly braces {}.

# Dictionaries store key-value pairs.

# Syntax:

# key: value

# Keys must be unique.

# Values can be duplicated.

# Dictionaries are mutable.

# Values are accessed using keys.

# dictionary[key]

# gives the value.

# get()

# safely gets a value.

# dictionary[key] = value

# adds or updates data.

# update()

# adds or updates multiple values.

# pop()

# removes a key and returns its value.

# popitem()

# removes the last inserted key-value pair.

# del

# can delete a specific key or entire dictionary.

# clear()

# removes everything.

# keys()

# returns keys.

# values()

# returns values.

# items()

# returns key-value pairs.

# len()

# returns number of key-value pairs.

# 'in'

# checks dictionary keys by default.

# To check values:

# value in dictionary.values()

# Dictionaries can contain:

# lists

# tuples

# sets

# dictionaries

# numbers

# strings

# booleans

# None

# and other Python objects.

# Dictionaries can be nested.

# copy()

# creates a shallow copy.

# deepcopy()

# is useful for fully independent nested dictionaries.

# Dictionary comprehensions provide

# a shorter way to create dictionaries.

# zip()

# can create dictionaries from two sequences.

# Dictionary keys must normally be immutable/hashable.

# Strings, numbers, and suitable tuples can be keys.

# Lists and dictionaries cannot normally be keys.

# Modern Python dictionaries preserve insertion order.

# 137. DICTIONARY METHOD CHEAT SHEET

# clear()

# Removes all items.

# copy()

# Creates a shallow copy.

# fromkeys(keys, value)

# Creates dictionary from keys.

# get(key)

# Safely gets value.

# get(key, default)

# Gets value or returns default.

# items()

# Returns key-value pairs.

# keys()

# Returns keys.

# pop(key)

# Removes key and returns its value.

# pop(key, default)

# Safely removes a key.

# popitem()

# Removes last inserted item.

# setdefault(key, default)

# Gets value and creates missing key if necessary.

# update()

# Adds or updates key-value pairs.

# values()

# Returns values.

# 138. FINAL BEGINNER EXAMPLE

student = {
"name": "Alice",
"age": 20,
"course": "CSE"
}

# Display all data

for key, value in student.items():
  print(f"{key}: {value}")

# Add marks

student["marks"] = 95

# Update age

student["age"] = 21

# Check for key

if "course" in student:
  print("Course:", student["course"])

# Safe access

email = student.get(
"email",
"Email not provided"
)

print(email)

# Copy dictionary

backup = student.copy()

# Remove marks

student.pop("marks")

# Display final dictionary

print("Student:", student)

print("Backup:", backup)

# END OF PYTHON DICTIONARY NOTES
