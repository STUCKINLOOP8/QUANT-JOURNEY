# PYTHON SETS

# 1. WHAT IS A SET?

# A set is a collection of unique values.

# Sets are written using curly braces {}.

fruits = {"apple", "banana", "mango"}

print(fruits)


# Important:
# Sets do not store duplicate values.


# 2. IMPORTANT PROPERTIES OF SETS

# Sets are:
# Unordered
# Mutable
# Do not allow duplicate values
# Do not support normal indexing
# Can contain different immutable data types


# Unordered means:
# Elements do not have a fixed index position
# that you should rely on.


# Mutable means:
# We can add and remove elements.


# 3. CREATING A SET

numbers = {1, 2, 3, 4}

names = {"Alice", "Bob", "Charlie"}

print(numbers)
print(names)


# 4. DUPLICATE VALUES ARE REMOVED

numbers = {1, 2, 2, 3, 3, 3}

print(numbers)

# Output may be:
# {1, 2, 3}


# Duplicate values are automatically ignored.


# 5. EMPTY SET

# Important:
# {} creates an empty DICTIONARY, not an empty set.

empty_dictionary = {}

print(type(empty_dictionary))

# Output:
# <class 'dict'>


# Correct way to create an empty set:

empty_set = set()

print(empty_set)
print(type(empty_set))

# Output:
# set()
# <class 'set'>


# 6. USING set()

numbers = set([1, 2, 3, 4])

print(numbers)


# set() can convert other iterables into a set.


# 7. CONVERTING LIST TO SET

numbers_list = [1, 2, 2, 3, 3, 4]

numbers_set = set(numbers_list)

print(numbers_set)

# Output:
# {1, 2, 3, 4}


# This is often used to remove duplicate values.


# 8. CONVERTING TUPLE TO SET

numbers_tuple = (1, 2, 2, 3)

numbers_set = set(numbers_tuple)

print(numbers_set)


# 9. CONVERTING STRING TO SET

word = "banana"

characters = set(word)

print(characters)

# Output order may vary.

# Duplicate characters are removed.


# 10. SETS DO NOT SUPPORT INDEXING

fruits = {"apple", "banana", "mango"}

# This is invalid:

# print(fruits[0])

# Python gives:
# TypeError


# Sets do not have normal positional indexes.


# 11. SET ORDER

fruits = {"apple", "banana", "mango"}

print(fruits)


# The printed order may not match
# the order in which values were written.

# Never rely on set order.


# 12. CHECKING IF AN ELEMENT EXISTS

fruits = {"apple", "banana", "mango"}

print("banana" in fruits)

# True


print("orange" in fruits)

# False


# 13. USING not in

fruits = {"apple", "banana", "mango"}

print("orange" not in fruits)

# True


# 14. ADDING ONE ELEMENT USING add()

fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)


# add() adds one element.


# 15. ADDING A DUPLICATE VALUE

numbers = {1, 2, 3}

numbers.add(2)

print(numbers)

# Still:
# {1, 2, 3}


# Duplicate values are not added.


# 16. ADDING MULTIPLE ELEMENTS USING update()

numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)


# update() can add multiple values
# from another iterable.


# 17. update() WITH ANOTHER SET

set1 = {1, 2, 3}

set2 = {4, 5, 6}

set1.update(set2)

print(set1)


# 18. update() WITH TUPLE

numbers = {1, 2}

numbers.update((3, 4, 5))

print(numbers)


# 19. update() WITH STRING

letters = {"a", "b"}

letters.update("cd")

print(letters)

# Adds:
# c
# d


# 20. add() VS update()

numbers = {1, 2, 3}

numbers.add(4)

# Adds one element.


numbers.update([5, 6])

# Adds multiple elements.


print(numbers)


# 21. REMOVING AN ELEMENT USING remove()

numbers = {1, 2, 3, 4}

numbers.remove(3)

print(numbers)


# remove() removes a specific value.


# 22. remove() ERROR

numbers = {1, 2, 3}

# numbers.remove(10)

# If 10 does not exist,
# Python gives KeyError.


# 23. REMOVING USING discard()

numbers = {1, 2, 3}

numbers.discard(2)

print(numbers)


# discard() also removes a specific value.


# 24. discard() DOES NOT GIVE ERROR IF VALUE IS MISSING

numbers = {1, 2, 3}

numbers.discard(10)

print(numbers)

# No error.


# 25. remove() VS discard()

numbers = {1, 2, 3}

# remove(value)
# Gives KeyError if value does not exist.

# discard(value)
# Does nothing if value does not exist.


# 26. pop()

# pop() removes and returns an arbitrary element.

numbers = {10, 20, 30}

removed = numbers.pop()

print("Removed:", removed)

print(numbers)


# Important:
# Since sets are unordered,
# do not assume which element pop() will remove.


# 27. clear()

numbers = {1, 2, 3, 4}

numbers.clear()

print(numbers)

# Output:
# set()


# clear() removes all elements
# but keeps the set variable.


# 28. del

numbers = {1, 2, 3}

del numbers

# After this:

# print(numbers)

# would give NameError.


# 29. LENGTH OF A SET

numbers = {10, 20, 30, 40}

print(len(numbers))

# Output:
# 4


# 30. LOOPING THROUGH A SET

fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)


# Order may vary.


# 31. SETS CAN STORE DIFFERENT DATA TYPES

data = {
    "Alice",
    20,
    85.5,
    True
}

print(data)


# Important:
# Set elements must be hashable.


# 32. LISTS CANNOT BE SET ELEMENTS

# This is invalid:

# data = {
#     [1, 2],
#     [3, 4]
# }

# Lists are mutable and unhashable.


# 33. DICTIONARIES CANNOT BE SET ELEMENTS

# This is invalid:

# data = {
#     {"name": "Alice"}
# }

# Dictionaries are unhashable.


# 34. SETS CANNOT DIRECTLY CONTAIN OTHER SETS

# This is invalid:

# data = {
#     {1, 2},
#     {3, 4}
# }

# Normal sets are mutable and unhashable.


# 35. TUPLES CAN BE SET ELEMENTS

points = {
    (1, 2),
    (3, 4)
}

print(points)


# Tuples can be elements
# if all values inside them are hashable.


# 36. CHECKING TYPE

numbers = {1, 2, 3}

print(type(numbers))

# Output:
# <class 'set'>


print(isinstance(numbers, set))

# True


# 37. COPY A SET

set1 = {1, 2, 3}

set2 = set1.copy()

print(set2)


# 38. IMPORTANT: ASSIGNMENT IS NOT COPYING

set1 = {1, 2, 3}

set2 = set1

set2.add(4)

print(set1)

# Contains 4 too.


print(set2)


# Both variables refer to the same set.


# Correct:

set1 = {1, 2, 3}

set2 = set1.copy()

set2.add(4)

print(set1)

print(set2)


# 39. ANOTHER WAY TO COPY

set1 = {1, 2, 3}

set2 = set(set1)

print(set2)


# 40. UNION

# Union combines all unique elements
# from both sets.

set1 = {1, 2, 3}

set2 = {3, 4, 5}

result = set1.union(set2)

print(result)

# Output:
# {1, 2, 3, 4, 5}


# 41. UNION USING |

set1 = {1, 2, 3}

set2 = {3, 4, 5}

result = set1 | set2

print(result)


# | means union.


# 42. UNION DOES NOT MODIFY ORIGINAL SETS

set1 = {1, 2, 3}

set2 = {3, 4, 5}

result = set1 | set2

print(set1)

print(set2)

print(result)


# 43. UNION OF MULTIPLE SETS

set1 = {1, 2}

set2 = {2, 3}

set3 = {3, 4}

result = set1.union(set2, set3)

print(result)

# Output:
# {1, 2, 3, 4}


# 44. INTERSECTION

# Intersection returns values
# that exist in BOTH sets.

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

result = set1.intersection(set2)

print(result)

# Output:
# {3, 4}


# 45. INTERSECTION USING &

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

result = set1 & set2

print(result)

# Output:
# {3, 4}


# & means intersection.


# 46. DIFFERENCE

# Difference returns elements
# that exist in the first set
# but not in the second.

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5}

result = set1.difference(set2)

print(result)

# Output:
# {1, 2}


# 47. DIFFERENCE USING -

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5}

result = set1 - set2

print(result)

# Output:
# {1, 2}


# 48. DIFFERENCE DIRECTION MATTERS

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5}

print(set1 - set2)

# {1, 2}


print(set2 - set1)

# {5}


# 49. SYMMETRIC DIFFERENCE

# Symmetric difference returns elements
# that exist in either set,
# but NOT in both.

set1 = {1, 2, 3}

set2 = {3, 4, 5}

result = set1.symmetric_difference(set2)

print(result)

# Output:
# {1, 2, 4, 5}


# 50. SYMMETRIC DIFFERENCE USING ^

set1 = {1, 2, 3}

set2 = {3, 4, 5}

result = set1 ^ set2

print(result)

# Output:
# {1, 2, 4, 5}


# ^ means symmetric difference.


# 51. SET OPERATOR SUMMARY

set1 = {1, 2, 3}

set2 = {3, 4, 5}


print(set1 | set2)

# Union


print(set1 & set2)

# Intersection


print(set1 - set2)

# Difference


print(set1 ^ set2)

# Symmetric difference


# 52. intersection_update()

# intersection_update() changes the original set.

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5}

set1.intersection_update(set2)

print(set1)

# Output:
# {3, 4}


# 53. difference_update()

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5}

set1.difference_update(set2)

print(set1)

# Output:
# {1, 2}


# 54. symmetric_difference_update()

set1 = {1, 2, 3}

set2 = {3, 4, 5}

set1.symmetric_difference_update(set2)

print(set1)

# Output:
# {1, 2, 4, 5}


# 55. update() AS UNION UPDATE

set1 = {1, 2, 3}

set2 = {3, 4, 5}

set1.update(set2)

print(set1)

# Output:
# {1, 2, 3, 4, 5}


# 56. METHOD VS UPDATE METHOD

set1 = {1, 2, 3}

set2 = {3, 4, 5}


result = set1.intersection(set2)

# Returns a new set.


set1.intersection_update(set2)

# Changes set1 itself.


# 57. issubset()

# A set is a subset if all its elements
# exist inside another set.

set1 = {1, 2}

set2 = {1, 2, 3, 4}

print(set1.issubset(set2))

# True


# 58. SUBSET USING <=

set1 = {1, 2}

set2 = {1, 2, 3}

print(set1 <= set2)

# True


# <= means subset.


# 59. PROPER SUBSET USING <

set1 = {1, 2}

set2 = {1, 2, 3}

print(set1 < set2)

# True


# Proper subset means:
# set1 is a subset,
# and set1 is not equal to set2.


# 60. issuperset()

# A set is a superset if it contains
# all elements of another set.

set1 = {1, 2, 3, 4}

set2 = {1, 2}

print(set1.issuperset(set2))

# True


# 61. SUPERSET USING >=

set1 = {1, 2, 3}

set2 = {1, 2}

print(set1 >= set2)

# True


# 62. PROPER SUPERSET USING >

set1 = {1, 2, 3}

set2 = {1, 2}

print(set1 > set2)

# True


# 63. isdisjoint()

# isdisjoint() checks whether two sets
# have NO common elements.

set1 = {1, 2, 3}

set2 = {4, 5, 6}

print(set1.isdisjoint(set2))

# True


# 64. isdisjoint() WITH COMMON ELEMENT

set1 = {1, 2, 3}

set2 = {3, 4, 5}

print(set1.isdisjoint(set2))

# False


# Because 3 exists in both sets.


# 65. EQUALITY OF SETS

set1 = {1, 2, 3}

set2 = {3, 2, 1}

print(set1 == set2)

# True


# Order does not matter in set equality.


# 66. NOT EQUAL

set1 = {1, 2, 3}

set2 = {1, 2, 4}

print(set1 != set2)

# True


# 67. SET COMPREHENSION

# Set comprehension is a shorter way
# to create sets.

numbers = {
    number
    for number in range(1, 6)
}

print(numbers)


# 68. SET COMPREHENSION WITH CALCULATION

squares = {
    number ** 2
    for number in range(1, 6)
}

print(squares)

# Output:
# {1, 4, 9, 16, 25}


# 69. SET COMPREHENSION WITH CONDITION

even_numbers = {
    number
    for number in range(1, 11)
    if number % 2 == 0
}

print(even_numbers)

# Output:
# {2, 4, 6, 8, 10}


# 70. NORMAL VERSION OF SET COMPREHENSION

even_numbers = set()

for number in range(1, 11):
    if number % 2 == 0:
        even_numbers.add(number)

print(even_numbers)


# 71. REMOVING DUPLICATES FROM A LIST

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)

# Output:
# {1, 2, 3, 4}


# 72. CONVERTING BACK TO LIST

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = list(set(numbers))

print(unique_numbers)


# Important:
# Original order should not be relied on.


# 73. REMOVE DUPLICATES WHILE PRESERVING ORDER

numbers = [3, 1, 3, 2, 1]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)

# Output:
# [3, 1, 2]


# This uses dictionary insertion order.


# 74. USER INPUT INTO A SET

data = input("Enter words separated by spaces: ")

words = set(data.split())

print(words)


# Example input:
# apple banana apple mango

# Set contains each value only once.


# 75. MULTIPLE INTEGER INPUTS INTO A SET

values = input("Enter numbers separated by spaces: ").split()

numbers = set()

for value in values:
    numbers.add(int(value))

print(numbers)


# 76. SHORTER INTEGER INPUT USING map()

numbers = set(
    map(
        int,
        input("Enter numbers separated by spaces: ").split()
    )
)

print(numbers)


# 77. CHECKING IF SET IS EMPTY

numbers = set()

if not numbers:
    print("Set is empty")


# Another way:

if len(numbers) == 0:
    print("Set is empty")


# 78. BOOLEAN VALUE OF SETS

print(bool(set()))

# False


print(bool({1, 2, 3}))

# True


# Empty set = False
# Non-empty set = True


# 79. min()

numbers = {5, 2, 8, 1}

print(min(numbers))

# Output:
# 1


# 80. max()

numbers = {5, 2, 8, 1}

print(max(numbers))

# Output:
# 8


# 81. sum()

numbers = {10, 20, 30}

print(sum(numbers))

# Output:
# 60


# 82. sorted()

numbers = {5, 2, 8, 1}

result = sorted(numbers)

print(result)

# Output:
# [1, 2, 5, 8]


# Important:
# sorted() returns a LIST.


# Convert back to set:

result_set = set(sorted(numbers))

print(result_set)


# But remember:
# A set itself does not keep sorted order.


# 83. enumerate() WITH A SET

fruits = {"apple", "banana", "mango"}

for index, fruit in enumerate(fruits):
    print(index, fruit)


# This gives temporary loop indexes,
# but set order is still not something to rely on.


# 84. any()

values = {False, False, True}

print(any(values))

# True


# 85. all()

values = {True, True}

print(all(values))

# True


values = {True, False}

print(all(values))

# False


# 86. frozenset

# frozenset is an immutable version of a set.

numbers = frozenset([1, 2, 3])

print(numbers)

print(type(numbers))

# Output:
# <class 'frozenset'>


# 87. frozenset CANNOT BE MODIFIED

numbers = frozenset([1, 2, 3])

# numbers.add(4)

# Invalid


# frozenset does not support add() or remove().


# 88. frozenset CAN BE USED INSIDE A SET

group1 = frozenset({1, 2})

group2 = frozenset({3, 4})

groups = {
    group1,
    group2
}

print(groups)


# Normal sets cannot be set elements,
# but frozensets can be.


# 89. frozenset CAN BE A DICTIONARY KEY

coordinates = {
    frozenset({1, 2}): "Group A"
}

print(coordinates)


# 90. SET VS LIST

numbers_list = [1, 2, 2, 3]

numbers_set = {1, 2, 2, 3}

print(numbers_list)

# [1, 2, 2, 3]


print(numbers_set)

# {1, 2, 3}


# List:
# Ordered
# Allows duplicates
# Supports indexing
# Mutable


# Set:
# Unordered
# Does not allow duplicates
# Does not support normal indexing
# Mutable


# 91. SET VS TUPLE

numbers_tuple = (1, 2, 2, 3)

numbers_set = {1, 2, 2, 3}


# Tuple:
# Ordered
# Immutable
# Allows duplicates
# Supports indexing


# Set:
# Unordered
# Mutable
# Unique values only
# No normal indexing


# 92. SET VS DICTIONARY

numbers = {1, 2, 3}

student = {
    "name": "Alice",
    "age": 20
}


# Set:
# Stores values only.


# Dictionary:
# Stores key-value pairs.


# 93. IMPORTANT EMPTY COLLECTION DIFFERENCE

empty_dictionary = {}

empty_set = set()

print(type(empty_dictionary))

# dict


print(type(empty_set))

# set


# This is a very common beginner mistake.


# 94. COMMON SET METHODS

numbers = {1, 2, 3}


# add(value)
# Adds one value.

numbers.add(4)


# update(iterable)
# Adds multiple values.

numbers.update([5, 6])


# remove(value)
# Removes value.
# Gives KeyError if missing.

numbers.remove(1)


# discard(value)
# Removes value safely.

numbers.discard(100)


# pop()
# Removes an arbitrary element.

removed = numbers.pop()


# copy()
# Creates a copy.

numbers_copy = numbers.copy()


# clear()
# Removes all values.

numbers_copy.clear()


# 95. SET OPERATION METHODS

set1 = {1, 2, 3}

set2 = {3, 4, 5}


print(set1.union(set2))

# Union


print(set1.intersection(set2))

# Intersection


print(set1.difference(set2))

# Difference


print(set1.symmetric_difference(set2))

# Symmetric difference


# 96. SET COMPARISON METHODS

set1 = {1, 2}

set2 = {1, 2, 3}


print(set1.issubset(set2))

# True


print(set2.issuperset(set1))

# True


print(set1.isdisjoint({5, 6}))

# True


# 97. COMMON ERROR: USING {}

empty = {}

print(type(empty))

# <class 'dict'>


# Wrong if you wanted a set.


# Correct:

empty = set()

print(type(empty))

# <class 'set'>


# 98. COMMON ERROR: INDEXING A SET

numbers = {10, 20, 30}

# print(numbers[0])

# TypeError


# Sets do not support normal indexing.


# 99. COMMON ERROR: ADDING LIST TO SET

numbers = {1, 2, 3}

# numbers.add([4, 5])

# TypeError:
# unhashable type: 'list'


# A list cannot be a set element.


# 100. COMMON ERROR: remove() ON MISSING VALUE

numbers = {1, 2, 3}

# numbers.remove(10)

# KeyError


# Safer:

numbers.discard(10)


# 101. COMMON ERROR: ASSUMING pop() REMOVES LAST ELEMENT

numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)


# Do not assume:
# first
# last
# smallest
# largest

# pop() removes an arbitrary element.


# 102. COMMON ERROR: RELYING ON SET ORDER

fruits = {"apple", "banana", "mango"}

print(fruits)


# Do not write code that depends on
# a particular set ordering.


# 103. COMMON ERROR: THINKING update() ADDS ONE ITEM ONLY

numbers = {1, 2}

numbers.update([3, 4])

print(numbers)


# update() adds elements from an iterable.


# add() is for one element.


# 104. COMMON ERROR: THINKING SETS ALLOW DUPLICATES

numbers = {1, 1, 1, 2, 2}

print(numbers)

# Only unique values remain.


# 105. SET WITH BOOLEANS AND INTEGERS

values = {
    True,
    1,
    False,
    0
}

print(values)


# Important:
# True == 1
# False == 0

# So sets may treat them as the same values.


# 106. SET MEMBERSHIP EXAMPLE

allowed_users = {
    "Alice",
    "Bob",
    "Charlie"
}

name = input("Enter name: ")

if name in allowed_users:
    print("Access allowed")
else:
    print("Access denied")


# 107. PRACTICAL EXAMPLE: UNIQUE SUBJECTS

subjects = {
    "Python",
    "Maths",
    "Python",
    "Physics"
}

print(subjects)


# Python appears only once.


# 108. PRACTICAL EXAMPLE: COMMON SUBJECTS

student1_subjects = {
    "Python",
    "Maths",
    "Physics"
}

student2_subjects = {
    "Python",
    "English",
    "Physics"
}

common_subjects = student1_subjects & student2_subjects

print(common_subjects)

# Output:
# {'Python', 'Physics'}


# 109. PRACTICAL EXAMPLE: ALL SUBJECTS

student1_subjects = {
    "Python",
    "Maths"
}

student2_subjects = {
    "Physics",
    "Python"
}

all_subjects = student1_subjects | student2_subjects

print(all_subjects)


# 110. PRACTICAL EXAMPLE: SUBJECTS ONLY STUDENT 1 HAS

student1_subjects = {
    "Python",
    "Maths",
    "Physics"
}

student2_subjects = {
    "Python",
    "Physics"
}

unique_to_student1 = student1_subjects - student2_subjects

print(unique_to_student1)

# Output:
# {'Maths'}


# 111. PRACTICAL EXAMPLE: DIFFERENT SUBJECTS

student1_subjects = {
    "Python",
    "Maths",
    "Physics"
}

student2_subjects = {
    "Python",
    "English",
    "Physics"
}

different_subjects = student1_subjects ^ student2_subjects

print(different_subjects)

# Output:
# {'Maths', 'English'}


# 112. PRACTICAL EXAMPLE: REMOVE DUPLICATE WORDS

words = [
    "python",
    "java",
    "python",
    "c++",
    "java"
]

unique_words = set(words)

print(unique_words)


# 113. PRACTICAL EXAMPLE: UNIQUE USER INPUT

data = input("Enter words separated by spaces: ")

words = data.split()

unique_words = set(words)

print("Unique words:", unique_words)


# 114. SET METHOD CHEAT SHEET

# add(value)
# Adds one element.

# update(iterable)
# Adds multiple elements.

# remove(value)
# Removes value.
# Error if missing.

# discard(value)
# Removes value.
# No error if missing.

# pop()
# Removes and returns an arbitrary element.

# clear()
# Removes all elements.

# copy()
# Creates a shallow copy.

# union()
# Returns all unique values from sets.

# intersection()
# Returns common values.

# difference()
# Returns values only in first set.

# symmetric_difference()
# Returns values not shared by both.

# intersection_update()
# Changes set to intersection.

# difference_update()
# Changes set to difference.

# symmetric_difference_update()
# Changes set to symmetric difference.

# issubset()
# Checks whether all values exist in another set.

# issuperset()
# Checks whether set contains another set.

# isdisjoint()
# Checks whether sets have no common values.


# 115. OPERATOR CHEAT SHEET

set1 = {1, 2, 3}

set2 = {3, 4, 5}


# Union

print(set1 | set2)


# Intersection

print(set1 & set2)


# Difference

print(set1 - set2)


# Symmetric difference

print(set1 ^ set2)


# Subset

print({1, 2} <= set1)


# Proper subset

print({1, 2} < set1)


# Superset

print(set1 >= {1, 2})


# Proper superset

print(set1 > {1, 2})


# 116. USEFUL FUNCTIONS WITH SETS

numbers = {10, 20, 30}


print(len(numbers))

# Number of elements


print(min(numbers))

# Smallest value


print(max(numbers))

# Largest value


print(sum(numbers))

# Total


print(sorted(numbers))

# Returns sorted list


print(any(numbers))

# True if at least one value is truthy


print(all(numbers))

# True if all values are truthy


# 117. WHEN SHOULD YOU USE A SET?

# Use a set when:

# You only want unique values.

# You want to remove duplicates.

# You want fast membership checks.

# You want to compare collections.

# You need:
# union
# intersection
# difference
# symmetric difference


# 118. WHEN SHOULD YOU USE A LIST INSTEAD?

# Use a list when:

# Order matters.

# Duplicate values matter.

# You need indexes.

# You want to access:
# list[0]
# list[1]

# You need to keep repeated values.


# 119. WHEN SHOULD YOU USE A TUPLE INSTEAD?

# Use a tuple when:

# Order matters.

# Values should not change.

# Duplicate values are allowed.

# Indexing is required.

# You want a fixed collection.


# 120. MOST IMPORTANT THINGS TO REMEMBER

# Sets use curly braces {}.

# But:
# {} creates an empty dictionary.

# Empty set:
# set()

# Sets contain unique values.

# Duplicate values are removed.

# Sets are unordered.

# Do not rely on their printed order.

# Sets are mutable.

# Sets do not support normal indexing.

# add()
# adds one element.

# update()
# adds multiple elements.

# remove()
# removes a value but gives an error if missing.

# discard()
# removes a value safely.

# pop()
# removes an arbitrary element.

# clear()
# removes all elements.

# copy()
# creates a copy.

# in
# checks if a value exists.

# not in
# checks if a value does not exist.

# union:
# set1 | set2

# intersection:
# set1 & set2

# difference:
# set1 - set2

# symmetric difference:
# set1 ^ set2

# subset:
# set1 <= set2

# proper subset:
# set1 < set2

# superset:
# set1 >= set2

# proper superset:
# set1 > set2

# Sets cannot contain:
# lists
# dictionaries
# normal sets

# because they are unhashable.

# Sets can contain suitable tuples.

# frozenset is an immutable set.

# frozensets can be elements of other sets.

# set() can convert:
# lists
# tuples
# strings
# ranges
# and other iterables into sets.


# 121. FINAL BEGINNER EXAMPLE

subjects = {
    "Python",
    "Maths",
    "Physics"
}

print("Subjects:", subjects)


# Add one subject

subjects.add("English")


# Add multiple subjects

subjects.update(
    [
        "Statistics",
        "Computer Science"
    ]
)


# Check subject

if "Python" in subjects:
    print("Python is present")


# Remove safely

subjects.discard("Maths")


# Copy the set

backup = subjects.copy()


# Display all subjects

for subject in subjects:
    print(subject)


print("Total subjects:", len(subjects))

print("Backup:", backup)


# END OF PYTHON SET NOTES