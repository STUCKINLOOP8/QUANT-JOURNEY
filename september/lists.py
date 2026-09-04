age=25
has_license = False
my_list = ["Alice", 25, age, True, has_license]

name = my_list[0]
age = my_list[1]

has_license = my_list[-1]
print(name,age,has_license)


#to update
my_list[0] = "Dave"

#to add at end
my_list.append("Alice")

#to  remove
my_list.remove("Alice")

#to insert at specific position
my_list.insert(1,"Alice")


print(my_list)












#NOTES


# PYTHON LISTS

# Beginner Notes

# Lists are one of the most commonly used data types in Python.

# 1. WHAT IS A LIST?

# A list is used to store multiple values inside a single variable.

fruits = ["apple", "banana", "mango"]

print(fruits)

# Output:

# ['apple', 'banana', 'mango']

# Lists are written using square brackets []

numbers = [10, 20, 30, 40]

names = ["Alice", "Bob", "Charlie"]

# 2. IMPORTANT PROPERTIES OF LISTS

# Lists are:

# Ordered

# Every element has a fixed position called an index.

# Mutable

# We can change the elements after creating the list.

# Allow duplicate values

# The same value can appear multiple times.

# Can contain different data types

# A single list can contain strings, integers, floats, booleans, etc.

example = ["Alice", 20, 85.5, True]

print(example)

# 3. CREATING A LIST

# Empty list

my_list = []

print(my_list)

# List containing integers

numbers = [1, 2, 3, 4, 5]

# List containing strings

fruits = ["apple", "banana", "mango"]

# List containing different data types

student = ["Ansh", 20, 85.5, True]

# A list can also contain another list.

data = [10, 20, [30, 40], 50]

# 4. USING list() TO CREATE A LIST

# Python also provides the list() constructor.

numbers = list((1, 2, 3, 4))

print(numbers)

# Output:

# [1, 2, 3, 4]

# Converting a string into a list

name = list("Python")

print(name)

# Output:

# ['P', 'y', 't', 'h', 'o', 'n']

# 5. LIST INDEXING

# Every element in a list has an index.

fruits = ["apple", "banana", "mango", "orange"]

# Index:

#

# apple   -> 0

# banana  -> 1

# mango   -> 2

# orange  -> 3

print(fruits[0])

# Output:

# apple

print(fruits[2])

# Output:

# mango

# Python indexing starts from 0, not 1.

# 6. NEGATIVE INDEXING

# Negative indexing starts from the end of the list.

fruits = ["apple", "banana", "mango", "orange"]

print(fruits[-1])

# Output:

# orange

print(fruits[-2])

# Output:

# mango

# Negative indexing:

# -1 = last element

# -2 = second last

# -3 = third last

# Example

my_list = ["Alice", 25, 100, True, False]

print(my_list[-1])

# False

print(my_list[-3])

# 100

# 7. FINDING THE LENGTH OF A LIST

# len() tells us how many elements are inside the list.

numbers = [10, 20, 30, 40, 50]

print(len(numbers))

# Output:

# 5

# 8. ACCESSING THE LAST ELEMENT

numbers = [10, 20, 30, 40]

print(numbers[-1])

# Output:

# 40

# Another way:

print(numbers[len(numbers) - 1])

# 9. CHANGING LIST ELEMENTS

# Lists are mutable.

# This means their elements can be changed.

fruits = ["apple", "banana", "mango"]

fruits[1] = "orange"

print(fruits)

# Output:

# ['apple', 'orange', 'mango']

# 10. ADDING ELEMENTS USING append()

# append() adds ONE element to the END of the list.

fruits = ["apple", "banana"]

fruits.append("mango")

print(fruits)

# Output:

# ['apple', 'banana', 'mango']

# append() can add any object.

numbers = [1, 2]

numbers.append(3)

print(numbers)

# Important:

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# Output:

# [1, 2, [3, 4]]

# The complete [3, 4] list becomes ONE element.

# 11. ADDING ELEMENTS USING extend()

# extend() adds multiple elements to an existing list.

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

# Output:

# [1, 2, 3, 4]

# Difference between append() and extend()

a = [1, 2]

a.append([3, 4])

print(a)

# [1, 2, [3, 4]]

b = [1, 2]

b.extend([3, 4])

print(b)

# [1, 2, 3, 4]

# append()

# Adds one object.

# extend()

# Adds each element from another iterable.

# 12. ADDING ELEMENTS USING insert()

# insert() adds an element at a particular index.

fruits = ["apple", "mango"]

fruits.insert(1, "banana")

print(fruits)

# Output:

# ['apple', 'banana', 'mango']

# Syntax:

# list.insert(index, value)

# 13. REMOVING AN ELEMENT USING remove()

# remove() removes an element using its VALUE.

fruits = ["apple", "banana", "mango"]

fruits.remove("banana")

print(fruits)

# Output:

# ['apple', 'mango']

# If duplicate values exist, remove() removes the first occurrence.

numbers = [10, 20, 20, 30]

numbers.remove(20)

print(numbers)

# Output:

# [10, 20, 30]

# If the value does not exist, Python gives ValueError.

# 14. REMOVING ELEMENTS USING pop()

# pop() removes an element using its INDEX.

fruits = ["apple", "banana", "mango"]

fruits.pop(1)

print(fruits)

# Output:

# ['apple', 'mango']

# pop() also returns the removed element.

fruits = ["apple", "banana", "mango"]

removed = fruits.pop(1)

print(removed)

# banana

# If no index is given, pop() removes the last element.

fruits = ["apple", "banana", "mango"]

fruits.pop()

print(fruits)

# ['apple', 'banana']

# 15. remove() VS pop()

# remove(value)

# Removes using the value.

# pop(index)

# Removes using the index.

# pop() also returns the removed element.

# 16. REMOVING ELEMENTS USING del

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

# Output:

# [10, 30, 40]

# del can also delete multiple elements using slicing.

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print(numbers)

# Output:

# [10, 50]

# del can delete the entire list variable.

numbers = [1, 2, 3]

del numbers

# After this, using:

#

# print(numbers)

#

# would give NameError.

# 17. CLEARING A LIST

# clear() removes every element but keeps the list variable.

numbers = [1, 2, 3, 4]

numbers.clear()

print(numbers)

# Output:

# []

# Difference:

# clear()

# List still exists but becomes empty.

# del list_name

# Deletes the variable completely.

# 18. CHECKING IF AN ELEMENT EXISTS

fruits = ["apple", "banana", "mango"]

print("banana" in fruits)

# True

print("orange" in fruits)

# False

# Using not in

print("orange" not in fruits)

# True

# 19. LOOPING THROUGH A LIST

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
  print(fruit)

# Output:

# apple

# banana

# mango

# 20. LOOPING USING INDEXES

fruits = ["apple", "banana", "mango"]

for i in range(len(fruits)):
  print(i, fruits[i])

# Output:

# 0 apple

# 1 banana

# 2 mango

# 21. USING enumerate()

# enumerate() gives both the index and the value.

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
  print(index, fruit)

# Output:

# 0 apple

# 1 banana

# 2 mango

# You can also change the starting number.

for index, fruit in enumerate(fruits, start=1):
  print(index, fruit)

# Output:

# 1 apple

# 2 banana

# 3 mango

# 22. LIST SLICING

# Slicing is used to get a portion of a list.

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])

# Output:

# [20, 30, 40]

# Syntax:

# list[start : stop]

# start is included.

# stop is NOT included.

# 23. SLICING FROM THE BEGINNING

numbers = [10, 20, 30, 40, 50]

print(numbers[:3])

# Output:

# [10, 20, 30]

# 24. SLICING TO THE END

print(numbers[2:])

# Output:

# [30, 40, 50]

# 25. COPYING THE WHOLE LIST USING SLICING

print(numbers[:])

# Output:

# [10, 20, 30, 40, 50]

# 26. SLICING WITH STEPS

numbers = [1, 2, 3, 4, 5, 6]

print(numbers[::2])

# Output:

# [1, 3, 5]

# Syntax:

# list[start : stop : step]

# 27. REVERSING A LIST USING SLICING

numbers = [1, 2, 3, 4, 5]

print(numbers[::-1])

# Output:

# [5, 4, 3, 2, 1]

# This creates a reversed copy.

# It does not change the original list.

# 28. NEGATIVE INDEXING WITH SLICING

numbers = [10, 20, 30, 40, 50]

print(numbers[-3:])

# Output:

# [30, 40, 50]

# 29. CHANGING MULTIPLE ELEMENTS USING SLICING

numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300]

print(numbers)

# Output:

# [10, 200, 300, 40]

# Python also allows replacing a slice with a different number of values.

numbers = [1, 2, 3, 4]

numbers[1:3] = [10, 20, 30]

print(numbers)

# Output:

# [1, 10, 20, 30, 4]

# 30. JOINING LISTS USING +

list1 = [1, 2, 3]

list2 = [4, 5, 6]

result = list1 + list2

print(result)

# Output:

# [1, 2, 3, 4, 5, 6]

# 31. REPEATING LISTS USING *

numbers = [1, 2]

result = numbers * 3

print(result)

# Output:

# [1, 2, 1, 2, 1, 2]

# 32. count()

# count() tells how many times a value appears.

numbers = [10, 20, 20, 20, 30]

print(numbers.count(20))

# Output:

# 3

# 33. index()

# index() returns the index of the first occurrence of a value.

fruits = ["apple", "banana", "mango"]

print(fruits.index("banana"))

# Output:

# 1

# If the value does not exist, index() gives ValueError.

# 34. reverse()

# reverse() reverses the original list.

numbers = [1, 2, 3, 4]

numbers.reverse()

print(numbers)

# Output:

# [4, 3, 2, 1]

# reverse() modifies the existing list.

# 35. sort()

# sort() sorts the original list.

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)

# Output:

# [1, 2, 3, 5, 8]

# Sorting strings

names = ["Charlie", "Alice", "Bob"]

names.sort()

print(names)

# Output:

# ['Alice', 'Bob', 'Charlie']

# 36. SORTING IN DESCENDING ORDER

numbers = [5, 2, 8, 1]

numbers.sort(reverse=True)

print(numbers)

# Output:

# [8, 5, 2, 1]

# 37. sorted()

# sorted() returns a NEW sorted list.

# It does not change the original list.

numbers = [5, 2, 8, 1]

new_numbers = sorted(numbers)

print(numbers)

# [5, 2, 8, 1]

print(new_numbers)

# [1, 2, 5, 8]

# Difference:

# list.sort()

# Changes the original list.

# sorted(list)

# Creates a new sorted list.

# 38. SORTING USING key

names = ["Bob", "Alexander", "Tom", "Alice"]

names.sort(key=len)

print(names)

# Output:

# ['Bob', 'Tom', 'Alice', 'Alexander']

# Here Python sorts according to string length.

# 39. min()

numbers = [5, 2, 8, 1]

print(min(numbers))

# Output:

# 1

# 40. max()

print(max(numbers))

# Output:

# 8

# 41. sum()

numbers = [10, 20, 30]

print(sum(numbers))

# Output:

# 60

# 42. LISTS CAN STORE DIFFERENT DATA TYPES

data = [
"Ansh",
20,
75.5,
True
]

print(data)

# However, in real programs it is often easier to understand lists

# when their elements represent similar kinds of data.

# 43. NESTED LISTS

# A list inside another list is called a nested list.

students = [
["Alice", 90],
["Bob", 85],
["Charlie", 95]
]

print(students)

# Accessing a nested list

print(students[0])

# ['Alice', 90]

# Accessing an element inside the nested list

print(students[0][0])

# Alice

print(students[0][1])

# 90

# 44. LOOPING THROUGH NESTED LISTS

students = [
["Alice", 90],
["Bob", 85],
["Charlie", 95]
]

for student in students:
  print(student)

# We can also unpack values.

for name, marks in students:
  print(name, marks)

# 45. LIST UNPACKING

numbers = [10, 20, 30]

a, b, c = numbers

print(a)
print(b)
print(c)

# Output:

# 10

# 20

# 30

# The number of variables normally needs to match

# the number of list elements.

# 46. EXTENDED UNPACKING

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)

# 10

print(middle)

# [20, 30, 40]

print(last)

# 50

# Another example

first, *remaining = numbers

print(first)

# 10

print(remaining)

# [20, 30, 40, 50]

# 47. COPYING LISTS

original = [1, 2, 3]

copy_list = original.copy()

print(copy_list)

# Another way:

copy_list = original[:]

# Another way:

copy_list = list(original)

# 48. IMPORTANT: ASSIGNMENT IS NOT COPYING

list1 = [1, 2, 3]

list2 = list1

list2.append(4)

print(list1)

# Output:

# [1, 2, 3, 4]

print(list2)

# Output:

# [1, 2, 3, 4]

# Why?

# list1 and list2 point to the SAME list object.

# Proper copy:

list1 = [1, 2, 3]

list2 = list1.copy()

list2.append(4)

print(list1)

# [1, 2, 3]

print(list2)

# [1, 2, 3, 4]

# 49. SHALLOW COPY

# list.copy(), slicing [:], and list()

# create shallow copies.

original = [[1, 2], [3, 4]]

copied = original.copy()

copied[0][0] = 100

print(original)

# [[100, 2], [3, 4]]

# This happens because the inner lists are still shared.

# For completely independent nested structures,

# Python provides deepcopy().

import copy

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

copied[0][0] = 100

print(original)

# [[1, 2], [3, 4]]

print(copied)

# [[100, 2], [3, 4]]

# 50. LIST COMPREHENSION

# List comprehension is a shorter way to create lists.

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

# Output:

# [1, 4, 9, 16, 25]

# Normal version:

squares = []

for number in numbers:\
  squares.append(number ** 2)

print(squares)

# 51. LIST COMPREHENSION WITH CONDITION

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)

# Output:

# [2, 4, 6]

# Beginners should first understand normal for loops.

# After that, list comprehensions become easier.

# 52. CREATING A LIST USING range()

numbers = list(range(1, 6))

print(numbers)

# Output:

# [1, 2, 3, 4, 5]

# range() itself is not a list.

# list() converts it into a list.

# 53. CONVERTING OTHER DATA INTO LISTS

# String to list

word = "Python"

characters = list(word)

print(characters)

# ['P', 'y', 't', 'h', 'o', 'n']

# Tuple to list

data = (10, 20, 30)

data = list(data)

print(data)

# [10, 20, 30]

# Set to list

values = {1, 2, 3}

values = list(values)

print(values)

# Order should not be relied on when converting from a set.

# 54. CONVERTING A LIST TO A STRING

words = ["I", "love", "Python"]

sentence = " ".join(words)

print(sentence)

# Output:

# I love Python

# join() works when the list contains strings.

# 55. split() CREATES A LIST

sentence = "Python is easy"

words = sentence.split()

print(words)

# Output:

# ['Python', 'is', 'easy']

# split() is a string method,

# but it commonly produces lists.

# Custom separator

data = "apple,banana,mango"

fruits = data.split(",")

print(fruits)

# ['apple', 'banana', 'mango']

# 56. USER INPUT AND LISTS

name = input("Enter your name: ")

print(name)

# Taking several words

data = input("Enter words separated by spaces: ")

words = data.split()

print(words)

# Example input:

# apple banana mango

# Result:

# ['apple', 'banana', 'mango']

# 57. TAKING MULTIPLE NUMBERS FROM USER

numbers = input("Enter numbers separated by spaces: ").split()

print(numbers)

# Important:

# input() always gives strings.

# If input is:

# 10 20 30

# Result:

# ['10', '20', '30']

# To convert them into integers:

numbers = list(map(int, input("Enter numbers: ").split()))

print(numbers)

# If input:

# 10 20 30

# Result:

# [10, 20, 30]

# Beginner-friendly version without map():

values = input("Enter numbers: ").split()

numbers = []

for value in values:
  numbers.append(int(value))

print(numbers)

# 58. EMPTY LIST CHECK

numbers = []

if not numbers:
  print("The list is empty")

# Another way:

if len(numbers) == 0:
  print("The list is empty")

# Usually:

# if not numbers:

# is considered simpler Python style.

# 59. BOOLEAN VALUE OF LISTS

print(bool([]))

# False

print(bool([1, 2, 3]))

# True

# Empty list = False

# Non-empty list = True

# 60. COMPARING LISTS

a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)

# True

# Lists are equal when their elements are equal

# and appear in the same order.

a = [1, 2, 3]

b = [3, 2, 1]

print(a == b)

# False

# 61. == VS is

a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)

# True

print(a is b)

# False

# == compares values.

# is checks whether both variables point

# to the exact same object.

# Example:

a = [1, 2, 3]

b = a

print(a is b)

# True

# 62. MEMBERSHIP OPERATORS

numbers = [10, 20, 30]

print(20 in numbers)

# True

print(50 not in numbers)

# True

# 63. FINDING THE POSITION OF AN ELEMENT SAFELY

fruits = ["apple", "banana", "mango"]

fruit = "banana"

if fruit in fruits:
  print(fruits.index(fruit))
else:
  print("Fruit not found")

# This prevents ValueError when using index().

# 64. REMOVING AN ELEMENT SAFELY

fruits = ["apple", "banana"]

fruit = "mango"

if fruit in fruits:
  fruits.remove(fruit)
else:
  print("Fruit does not exist")

# 65. MODIFYING ELEMENTS WHILE LOOPING

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
  numbers[i] = numbers[i] * 2

print(numbers)

# Output:

# [2, 4, 6, 8]

# 66. BE CAREFUL WHEN REMOVING ELEMENTS WHILE LOOPING

numbers = [1, 2, 3, 4, 5, 6]

# Modifying a list while directly looping through it

# can cause elements to be skipped.

# It is often safer to loop over a copy.

for number in numbers.copy():
  if number % 2 == 0:
    numbers.remove(number)


print(numbers)

# [1, 3, 5]

# 67. COMMON LIST METHODS

# append(value)

# Adds one element to the end.

# extend(iterable)

# Adds multiple elements.

# insert(index, value)

# Inserts an element at an index.

# remove(value)

# Removes the first matching value.

# pop(index)

# Removes and returns an element.

# clear()

# Removes all elements.

# index(value)

# Finds the index of the first matching value.

# count(value)

# Counts how many times a value appears.

# sort()

# Sorts the original list.

# reverse()

# Reverses the original list.

# copy()

# Creates a shallow copy.

# 68. FUNCTIONS COMMONLY USED WITH LISTS

# len(list)

# Number of elements.

# min(list)

# Smallest element.

# max(list)

# Largest element.

# sum(list)

# Sum of numeric elements.

# sorted(list)

# Creates a sorted list.

# list(iterable)

# Creates or converts something into a list.

# any(list)

# True if at least one value is truthy.

# all(list)

# True if every value is truthy.

# 69. any()

values = [False, False, True]

print(any(values))

# True

# 70. all()

values = [True, True, True]

print(all(values))

# True

values = [True, False, True]

print(all(values))

# False

# 71. LIST METHOD RETURN VALUES

# Some list methods modify the list directly.

numbers = [3, 1, 2]

result = numbers.sort()

print(numbers)

# [1, 2, 3]

print(result)

# None

# This is a common beginner mistake:

numbers = [3, 1, 2]

numbers = numbers.sort()

print(numbers)

# None

# Correct:

numbers = [3, 1, 2]

numbers.sort()

print(numbers)

# Or:

numbers = [3, 1, 2]

numbers = sorted(numbers)

print(numbers)

# 72. append() ALSO RETURNS None

numbers = [1, 2]

result = numbers.append(3)

print(numbers)

# [1, 2, 3]

print(result)

# None

# Don't do:

# numbers = numbers.append(3)

# 73. COMMON ERROR: INDEX OUT OF RANGE

numbers = [10, 20, 30]

# print(numbers[5])

# This gives:

# IndexError: list index out of range

# Valid indexes here are:

# 0

# 1

# 2

# 74. COMMON ERROR: FORGETTING INDEX STARTS FROM ZERO

fruits = ["apple", "banana", "mango"]

# First element:

print(fruits[0])

# NOT:

# fruits[1]

# fruits[1] is the second element.

# 75. COMMON ERROR: remove() VS pop()

numbers = [10, 20, 30]

numbers.remove(20)

# Removes VALUE 20.

numbers = [10, 20, 30]

numbers.pop(1)

# Removes INDEX 1, which contains 20.

# 76. COMMON ERROR: append() VS extend()

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# [1, 2, [3, 4]]

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

# [1, 2, 3, 4]

# 77. COMMON ERROR: USING A LIST BEFORE CREATING IT

# Example:

# my_list.append(10)

# If my_list was never created, Python gives:

# NameError: name 'my_list' is not defined

# Correct:

my_list = []

my_list.append(10)

# 78. JUPYTER NOTE

# In Jupyter notebooks, variables only exist after

# the cell that creates them has been executed.

my_list = ["Alice", 25, True]

# If you restart the kernel and run only:

# print(my_list)

# Python will give NameError.

# Run the cell that creates my_list first.

# 79. COMMON ERROR: USING str AS A VARIABLE NAME

# Avoid:

# str = "hello"

# list = [1, 2, 3]

# int = 10

# str, list, and int are built-in Python names.

# Better:

string_value = "hello"

numbers = [1, 2, 3]

age = 10

# 80. LIST OF STRINGS VS STRING

word = "Python"

letters = ["P", "y", "t", "h", "o", "n"]

# word is a string.

print(type(word))

# <class 'str'>

# letters is a list.

print(type(letters))

# <class 'list'>

# 81. CHECKING WHETHER SOMETHING IS A LIST

numbers = [1, 2, 3]

print(type(numbers))

# <class 'list'>

print(isinstance(numbers, list))

# True

# isinstance() is often preferred when checking types.

# 82. LISTS ARE MUTABLE

numbers = [1, 2, 3]

numbers[0] = 100

print(numbers)

# [100, 2, 3]

# Strings are different because strings are immutable.

# 83. LIST VS TUPLE

# List:

numbers = [1, 2, 3]

# Uses []

# Mutable

# Elements can be changed.

# Tuple:

numbers_tuple = (1, 2, 3)

# Uses ()

# Immutable

# Elements cannot normally be changed after creation.

# 84. LIST VS SET

numbers_list = [1, 2, 2, 3]

numbers_set = {1, 2, 2, 3}

print(numbers_list)

# [1, 2, 2, 3]

print(numbers_set)

# {1, 2, 3}

# Lists:

# Ordered

# Allow duplicates

# Support indexing

# Sets:

# Do not provide normal positional indexing

# Store unique elements

# 85. LIST VS DICTIONARY

names = ["Alice", "Bob", "Charlie"]

student = {
"name": "Alice",
"age": 20
}

# Lists mainly access values using indexes.

print(names[0])

# Dictionaries access values using keys.

print(student["name"])

# 86. LIST VS STRING

text = "Python"

characters = ["P", "y", "t", "h", "o", "n"]

# Both support:

# indexing

# slicing

# len()

# loops

# membership tests

# Main difference:

# Lists are mutable.

# Strings are immutable.

# 87. MULTIDIMENSIONAL OR NESTED LIST

matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

print(matrix[0])

# [1, 2, 3]

print(matrix[0][1])

# 2

print(matrix[2][2])

# 9

# 88. COPYING NESTED LISTS

original = [
[1, 2],
[3, 4]
]

# A normal copy is shallow.

copied = original.copy()

# For a fully independent nested copy:

import copy

deep_copied = copy.deepcopy(original)

# 89. CREATING REPEATED NESTED LISTS CAREFULLY

# Be careful with this:

wrong = [[0] * 3] * 3

wrong[0][0] = 1

print(wrong)

# You may get:

# [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# This happens because the inner lists refer to

# the same list object.

# Better:

correct = [[0] * 3 for _ in range(3)]

correct[0][0] = 1

print(correct)

# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# 90. USING _ IN LOOPS

numbers = []

for _ in range(5):
  numbers.append(0)

print(numbers)

# [0, 0, 0, 0, 0]

# _ is commonly used when the loop variable itself

# is not needed.

# 91. LIST COMPREHENSION EXAMPLES

numbers = [number for number in range(1, 6)]

print(numbers)

# [1, 2, 3, 4, 5]

squares = [number ** 2 for number in range(1, 6)]

print(squares)

# [1, 4, 9, 16, 25]

even_numbers = [
number
for number in range(1, 11)
if number % 2 == 0
]

print(even_numbers)

# [2, 4, 6, 8, 10]

# 92. CONDITIONAL EXPRESSION INSIDE LIST COMPREHENSION

numbers = [1, 2, 3, 4, 5]

result = [
"even" if number % 2 == 0 else "odd"
for number in numbers
]

print(result)

# ['odd', 'even', 'odd', 'even', 'odd']

# 93. USING zip() WITH LISTS

names = ["Alice", "Bob", "Charlie"]

marks = [90, 80, 85]

for name, mark in zip(names, marks):
  print(name, mark)

# Output:

# Alice 90

# Bob 80

# Charlie 85

# zip() combines corresponding values from iterables.

# We can create a list from zip():

combined = list(zip(names, marks))

print(combined)

# [('Alice', 90), ('Bob', 80), ('Charlie', 85)]

# 94. USING enumerate() WITH LISTS

names = ["Alice", "Bob", "Charlie"]

for index, name in enumerate(names):
  print(index, name)

# enumerate() is useful when you need

# both index and value.

# 95. FINDING MULTIPLE DETAILS ABOUT A LIST

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)

print("Length:", len(numbers))

print("First element:", numbers[0])

print("Last element:", numbers[-1])

print("Minimum:", min(numbers))

print("Maximum:", max(numbers))

print("Total:", sum(numbers))

# 96. EXAMPLE: USER-MANAGED SHOPPING LIST

shopping_list = []

item = input("Enter an item: ")

shopping_list.append(item)

print(shopping_list)

# Add another item

item = input("Enter another item: ")

shopping_list.append(item)

print(shopping_list)

# 97. EXAMPLE: REMOVE AN ITEM FROM USER LIST

shopping_list = [
"milk",
"bread",
"eggs"
]

item = input("Which item do you want to remove? ")

if item in shopping_list:
  shopping_list.remove(item)
  print("Item removed")
else:
  print("Item not found")

print(shopping_list)

# 98. EXAMPLE: SEARCHING FOR A VALUE

names = [
"Alice",
"Bob",
"Charlie"
]

search_name = input("Enter a name: ")

if search_name in names:
  print("Name found")


else:
  print("Name not found")


# 99. EXAMPLE: COUNTING AN ITEM

fruits = [
"apple",
"banana",
"apple",
"mango",
"apple"
]

print(fruits.count("apple"))

# 3

# 100. IMPORTANT LIST SYNTAX SUMMARY

# Create list

numbers = [1, 2, 3]

# Access element

numbers[0]

# Last element

numbers[-1]

# Slice

numbers[0:2]

# Add one element

numbers.append(4)

# Add multiple elements

numbers.extend([5, 6])

# Insert element

numbers.insert(1, 100)

# Remove by value

numbers.remove(100)

# Remove by index

numbers.pop(0)

# Find length

len(numbers)

# Check membership

if 3 in numbers:
  print("Found")

# Loop

for number in numbers:
  print(number)

# Loop with index

for index, number in enumerate(numbers):
  print(index, number)

# Count occurrences

numbers.count(3)

# Find index

numbers.index(3)

# Sort

numbers.sort()

# Reverse

numbers.reverse()

# Copy

new_numbers = numbers.copy()

# Clear

numbers.clear()

# 101. MOST IMPORTANT THINGS TO REMEMBER

# Lists use square brackets [].

# Indexing starts from 0.

# Negative indexing starts from the end.

# -1 means the last element.

# Lists are ordered.

# Lists are mutable.

# Lists allow duplicates.

# Lists can contain different data types.

# append() adds ONE element.

# extend() adds MULTIPLE elements.

# insert() adds an element at a particular index.

# remove() removes using VALUE.

# pop() removes using INDEX.

# clear() removes all elements.

# del can remove elements or delete the complete variable.

# len() gives the number of elements.

# count() counts occurrences.

# index() finds the position of a value.

# sort() modifies the original list.

# sorted() creates a new sorted list.

# reverse() reverses the original list.

# [::-1] creates a reversed copy.

# copy() creates a shallow copy.

# Simply doing list2 = list1 does NOT make an independent copy.

# Lists can contain other lists.

# List comprehension provides a shorter way to create lists.

# in checks whether a value exists.

# not in checks whether a value does not exist.

# enumerate() gives index + value.

# zip() lets you loop through matching elements

# from multiple iterables.

# input() returns strings, so convert values to int

# when numeric input is required.

# 102. QUICK LIST METHOD CHEAT SHEET

# append(x)

# Add x to the end.

# extend(iterable)

# Add multiple elements.

# insert(i, x)

# Insert x at index i.

# remove(x)

# Remove first occurrence of x.

# pop(i)

# Remove and return element at index i.

# pop()

# Remove and return the last element.

# clear()

# Remove everything.

# index(x)

# Return index of first x.

# count(x)

# Count occurrences of x.

# sort()

# Sort the list.

# sort(reverse=True)

# Sort descending.

# reverse()

# Reverse the list.

# copy()

# Create a shallow copy.

# 103. FINAL BEGINNER EXAMPLE

students = [
"Alice",
"Bob",
"Charlie"
]

# Add student

students.append("David")

# Insert student

students.insert(1, "John")

# Remove student

students.remove("Bob")

# Print number of students

print("Number of students:", len(students))

# Print every student

for index, student in enumerate(students, start=1):
  print(index, student)

# Check student

search = "Alice"

if search in students:
  print(search, "is present")
else:
  print(search, "is not present")

# Create a copy

backup = students.copy()

# Sort students

students.sort()

print("Sorted list:", students)

print("Backup:", backup)

# END OF PYTHON LIST NOTES.