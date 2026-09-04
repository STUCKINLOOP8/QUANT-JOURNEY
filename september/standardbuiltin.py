# Python contains many modules that are already installed
# when Python is installed.

# We usually need to import them before using them.

# Example:

import math

print(math.sqrt(25))

# Output:
# 5.0


# Common standard library modules:

# math
# random
# json
# datetime
# time
# os
# sys
# statistics
# string
# re
# pathlib
# collections
# itertools
# functools
# operator
# calendar
# decimal
# fractions
# secrets
# csv


# 1. IMPORTING MODULES

import math

print(math.pi)


# 2. IMPORTING A SPECIFIC FUNCTION

from math import sqrt

print(sqrt(25))


# Now we do not need:

# math.sqrt(25)


# 3. IMPORTING WITH AN ALIAS

import math as m

print(m.sqrt(25))


# Alias gives the module another name.


# 4. IMPORTING MULTIPLE FUNCTIONS

from math import sqrt, floor, ceil

print(sqrt(25))
print(floor(4.9))
print(ceil(4.1))


# Avoid using:

# from math import *

# because it imports everything
# and can make code harder to understand.


# 5. MATH MODULE

import math


# math.pi

print(math.pi)

# 3.141592...


# math.e

print(math.e)

# Euler's number


# math.sqrt()

print(math.sqrt(25))

# 5.0


# math.pow()

print(math.pow(2, 3))

# 8.0


# math.floor()

print(math.floor(4.9))

# 4


# math.ceil()

print(math.ceil(4.1))

# 5


# math.trunc()

print(math.trunc(4.9))

# 4


print(math.trunc(-4.9))

# -4


# math.factorial()

print(math.factorial(5))

# 120


# 5 factorial:
# 5 * 4 * 3 * 2 * 1


# math.gcd()

print(math.gcd(12, 18))

# 6


# Greatest Common Divisor


# math.lcm()

print(math.lcm(12, 18))

# 36


# Least Common Multiple


# math.fabs()

print(math.fabs(-10))

# 10.0


# Similar to abs()
# but returns float.


# math.log()

print(math.log(math.e))

# 1.0


# Natural logarithm


# math.log10()

print(math.log10(1000))

# 3.0


# math.log2()

print(math.log2(8))

# 3.0


# math.exp()

print(math.exp(1))

# e raised to power 1


# math.sin()

angle = math.radians(30)

print(math.sin(angle))


# math.cos()

angle = math.radians(60)

print(math.cos(angle))


# math.tan()

angle = math.radians(45)

print(math.tan(angle))


# Trigonometric functions use radians.


# math.radians()

print(math.radians(180))

# Converts degrees to radians.


# math.degrees()

print(math.degrees(math.pi))

# 180.0


# math.hypot()

print(math.hypot(3, 4))

# 5.0


# math.isclose()

print(
    math.isclose(
        0.1 + 0.2,
        0.3
    )
)

# True


# Useful because floating-point numbers
# may not compare exactly.


# math.inf

infinity = math.inf

print(infinity)


# math.nan

not_a_number = math.nan

print(not_a_number)


# math.isfinite()

print(math.isfinite(100))

# True


print(math.isfinite(math.inf))

# False


# math.isinf()

print(math.isinf(math.inf))

# True


# math.isnan()

print(math.isnan(math.nan))

# True


# 6. RANDOM MODULE

import random


# Used to generate pseudo-random values.


# random.random()

number = random.random()

print(number)

# Float between 0.0 and 1.0


# random.randint()

number = random.randint(1, 10)

print(number)

# Integer between 1 and 10.
# Both values are included.


# random.randrange()

number = random.randrange(1, 10)

print(number)

# 1 to 9


# With step:

number = random.randrange(0, 20, 2)

print(number)


# random.uniform()

number = random.uniform(1.0, 10.0)

print(number)

# Random floating-point number.


# random.choice()

fruits = [
    "apple",
    "banana",
    "mango"
]

fruit = random.choice(fruits)

print(fruit)


# Picks one random item.


# random.choices()

fruits = [
    "apple",
    "banana",
    "mango"
]

result = random.choices(
    fruits,
    k=3
)

print(result)


# Can select the same item more than once.


# random.sample()

numbers = [
    1,
    2,
    3,
    4,
    5
]

result = random.sample(
    numbers,
    k=3
)

print(result)


# Selects unique items.


# random.shuffle()

numbers = [
    1,
    2,
    3,
    4,
    5
]

random.shuffle(numbers)

print(numbers)


# Changes the original list.


# random.seed()

random.seed(10)

print(random.randint(1, 100))


# Same seed can produce repeatable results.


# IMPORTANT:
# random should not be used
# for passwords or security tokens.


# 7. SECRETS MODULE

import secrets


# secrets is used when random values
# need to be secure.


# secrets.randbelow()

number = secrets.randbelow(10)

print(number)

# Random number:
# 0 to 9


# secrets.choice()

characters = "abcdef123456"

character = secrets.choice(characters)

print(character)


# secrets.token_hex()

token = secrets.token_hex(16)

print(token)


# Useful for secure tokens.


# secrets.token_urlsafe()

token = secrets.token_urlsafe(16)

print(token)


# 8. JSON MODULE

import json


# JSON stands for:
# JavaScript Object Notation


# Commonly used for:

# APIs
# web applications
# configuration files
# data exchange


# json.dumps()

student = {
    "name": "Alice",
    "age": 20,
    "course": "CSE"
}

json_text = json.dumps(student)

print(json_text)

print(type(json_text))

# str


# dumps:
# Python object -> JSON string


# Pretty JSON:

json_text = json.dumps(
    student,
    indent=4
)

print(json_text)


# Sort keys:

json_text = json.dumps(
    student,
    indent=4,
    sort_keys=True
)

print(json_text)


# json.loads()

json_text = """
{
    "name": "Alice",
    "age": 20
}
"""

student = json.loads(json_text)

print(student)

print(type(student))

# dict


# loads:
# JSON string -> Python object


# json.dump()

student = {
    "name": "Alice",
    "age": 20
}

# with open("student.json", "w") as file:
#     json.dump(
#         student,
#         file,
#         indent=4
#     )


# dump:
# Python object -> JSON file


# json.load()

# with open("student.json", "r") as file:
#     student = json.load(file)

# print(student)


# load:
# JSON file -> Python object


# IMPORTANT:

# dumps()
# Python -> JSON string

# loads()
# JSON string -> Python

# dump()
# Python -> JSON file

# load()
# JSON file -> Python


# 9. DATETIME MODULE

from datetime import datetime
from datetime import date
from datetime import timedelta


# Current date and time:

now = datetime.now()

print(now)


# Current date:

today = date.today()

print(today)


# Creating a date:

birthday = date(
    2005,
    8,
    15
)

print(birthday)


# Accessing parts:

today = date.today()

print(today.year)
print(today.month)
print(today.day)


# Creating datetime:

meeting = datetime(
    2026,
    9,
    4,
    18,
    30
)

print(meeting)


# Accessing datetime parts:

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


# strftime()

# Converts datetime to formatted string.

now = datetime.now()

formatted = now.strftime(
    "%d-%m-%Y"
)

print(formatted)


# Common format codes:

# %d
# Day

# %m
# Month number

# %Y
# Four-digit year

# %y
# Two-digit year

# %H
# Hour in 24-hour format

# %I
# Hour in 12-hour format

# %M
# Minute

# %S
# Second

# %A
# Full weekday

# %a
# Short weekday

# %B
# Full month name

# %b
# Short month name

# %p
# AM / PM


print(
    now.strftime(
        "%A, %d %B %Y"
    )
)


print(
    now.strftime(
        "%I:%M %p"
    )
)


# strptime()

# Converts string into datetime.

date_text = "04-09-2026"

converted_date = datetime.strptime(
    date_text,
    "%d-%m-%Y"
)

print(converted_date)


# timedelta()

today = date.today()

future = today + timedelta(days=7)

print(future)


past = today - timedelta(days=7)

print(past)


# Difference between dates:

date1 = date(
    2026,
    9,
    10
)

date2 = date(
    2026,
    9,
    4
)

difference = date1 - date2

print(difference.days)

# 6


# 10. TIME MODULE

import time


# time.time()

current_time = time.time()

print(current_time)


# Returns seconds since Unix epoch.


# time.sleep()

print("Start")

# time.sleep(2)

print("End")


# sleep(2)
# pauses program for 2 seconds.


# time.perf_counter()

start = time.perf_counter()

total = 0

for number in range(100000):
    total += number

end = time.perf_counter()

print(end - start)


# Useful for measuring execution time.


# time.localtime()

current = time.localtime()

print(current)


# time.strftime()

formatted = time.strftime(
    "%H:%M:%S"
)

print(formatted)


# 11. STATISTICS MODULE

import statistics


numbers = [
    10,
    20,
    30,
    40,
    50
]


# statistics.mean()

print(statistics.mean(numbers))

# Average


# statistics.median()

print(statistics.median(numbers))

# Middle value


# statistics.mode()

values = [
    1,
    2,
    2,
    3,
    4
]

print(statistics.mode(values))

# 2


# statistics.multimode()

values = [
    1,
    1,
    2,
    2,
    3
]

print(statistics.multimode(values))

# [1, 2]


# statistics.variance()

numbers = [
    10,
    20,
    30,
    40
]

print(statistics.variance(numbers))


# statistics.stdev()

print(statistics.stdev(numbers))


# Standard deviation


# 12. STRING MODULE

import string


# Useful predefined character collections.


print(string.ascii_lowercase)

# abcdefghijklmnopqrstuvwxyz


print(string.ascii_uppercase)

# ABCDEFGHIJKLMNOPQRSTUVWXYZ


print(string.ascii_letters)

# Lowercase + uppercase


print(string.digits)

# 0123456789


print(string.hexdigits)


print(string.punctuation)


print(string.whitespace)


# Example:

characters = (
    string.ascii_letters
    + string.digits
)

print(characters)


# 13. OS MODULE

import os


# Used for interacting
# with the operating system.


# Current working directory:

print(os.getcwd())


# List files:

print(os.listdir())


# Check if file/folder exists:

print(
    os.path.exists(
        "example.txt"
    )
)


# Check if path is file:

print(
    os.path.isfile(
        "example.txt"
    )
)


# Check if path is directory:

print(
    os.path.isdir(
        "."
    )
)


# Join paths safely:

path = os.path.join(
    "folder",
    "file.txt"
)

print(path)


# Get filename:

path = "folder/example.txt"

print(
    os.path.basename(path)
)


# Get directory:

print(
    os.path.dirname(path)
)


# File extension:

print(
    os.path.splitext(path)
)


# Create directory:

# os.mkdir("new_folder")


# Create nested directories:

# os.makedirs(
#     "folder1/folder2",
#     exist_ok=True
# )


# Rename:

# os.rename(
#     "old.txt",
#     "new.txt"
# )


# Delete file:

# os.remove("example.txt")


# Remove empty directory:

# os.rmdir("folder")


# Environment variable:

path_variable = os.getenv("PATH")

print(path_variable)


# 14. SYS MODULE

import sys


# Python version:

print(sys.version)


# Platform:

print(sys.platform)


# Command-line arguments:

print(sys.argv)


# Python executable location:

print(sys.executable)


# Module search paths:

print(sys.path)


# Exit program:

# sys.exit()


# Maximum integer information:

print(sys.maxsize)


# 15. PATHLIB MODULE

from pathlib import Path


# Modern way to work with file paths.


# Current folder:

current = Path.cwd()

print(current)


# Home folder:

home = Path.home()

print(home)


# Create path:

file_path = Path(
    "folder"
) / "example.txt"

print(file_path)


# Check existence:

print(file_path.exists())


# Check file:

print(file_path.is_file())


# Check directory:

print(file_path.is_dir())


# File name:

print(file_path.name)


# Extension:

print(file_path.suffix)


# File name without extension:

print(file_path.stem)


# Parent folder:

print(file_path.parent)


# Create folder:

folder = Path("example_folder")

# folder.mkdir(
#     exist_ok=True
# )


# Read text file:

# content = Path(
#     "example.txt"
# ).read_text()


# Write text file:

# Path(
#     "example.txt"
# ).write_text(
#     "Hello Python"
# )


# pathlib is often cleaner
# than using os.path.


# 16. RE MODULE

import re


# re means:
# Regular Expressions

# Used for searching and matching text.


text = "My number is 12345"


# re.search()

match = re.search(
    r"\d+",
    text
)

if match:
    print(match.group())

# Output:
# 12345


# \d means digit.

# + means one or more.


# re.findall()

text = "10 apples and 20 bananas"

numbers = re.findall(
    r"\d+",
    text
)

print(numbers)

# ['10', '20']


# re.match()

text = "Python is easy"

result = re.match(
    r"Python",
    text
)

print(result)


# match() checks from beginning.


# re.fullmatch()

result = re.fullmatch(
    r"\d+",
    "12345"
)

print(result)


# Entire string must match.


# re.sub()

text = "Hello World"

result = re.sub(
    r"World",
    "Python",
    text
)

print(result)

# Hello Python


# re.split()

text = "apple,banana,mango"

result = re.split(
    r",",
    text
)

print(result)


# 17. COLLECTIONS MODULE

from collections import Counter
from collections import defaultdict
from collections import deque


# Counter

letters = [
    "a",
    "b",
    "a",
    "c",
    "a"
]

counts = Counter(letters)

print(counts)

# Counter({'a': 3, ...})


print(counts["a"])

# 3


# most_common()

print(
    counts.most_common(1)
)


# defaultdict

students = defaultdict(list)

students["CSE"].append("Alice")

students["CSE"].append("Bob")

print(students)


# Missing keys automatically
# get the default value.


# deque

queue = deque(
    [
        1,
        2,
        3
    ]
)

queue.append(4)

print(queue)


queue.appendleft(0)

print(queue)


queue.pop()

print(queue)


queue.popleft()

print(queue)


# 18. ITERTOOLS MODULE

import itertools


# itertools provides useful tools
# for working with iterables.


# count()

counter = itertools.count(
    start=1,
    step=1
)


for _ in range(5):
    print(next(counter))


# Output:
# 1
# 2
# 3
# 4
# 5


# repeat()

result = itertools.repeat(
    "Python",
    3
)

print(list(result))

# ['Python', 'Python', 'Python']


# chain()

list1 = [
    1,
    2
]

list2 = [
    3,
    4
]

result = itertools.chain(
    list1,
    list2
)

print(list(result))

# [1, 2, 3, 4]


# combinations()

values = [
    1,
    2,
    3
]

result = itertools.combinations(
    values,
    2
)

print(list(result))


# permutations()

result = itertools.permutations(
    values,
    2
)

print(list(result))


# product()

result = itertools.product(
    [1, 2],
    ["A", "B"]
)

print(list(result))


# 19. FUNCTOOLS MODULE

import functools


# functools contains tools
# for working with functions.


# reduce()

numbers = [
    1,
    2,
    3,
    4
]

result = functools.reduce(
    lambda a, b: a + b,
    numbers
)

print(result)

# 10


# Equivalent idea:

# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10


# lru_cache()

@functools.lru_cache(maxsize=None)
def square(number):
    return number ** 2


print(square(5))


# Cache stores previous results.


# 20. OPERATOR MODULE

import operator


print(
    operator.add(
        10,
        20
    )
)

# 30


print(
    operator.sub(
        10,
        5
    )
)

# 5


print(
    operator.mul(
        10,
        5
    )
)

# 50


print(
    operator.truediv(
        10,
        5
    )
)

# 2.0


print(
    operator.mod(
        10,
        3
    )
)

# 1


print(
    operator.pow(
        2,
        3
    )
)

# 8


# Comparison:

print(
    operator.eq(
        10,
        10
    )
)

# True


print(
    operator.gt(
        10,
        5
    )
)

# True


# 21. DECIMAL MODULE

from decimal import Decimal


# Decimal is useful when
# exact decimal calculations matter.


normal = 0.1 + 0.2

print(normal)

# May display:
# 0.30000000000000004


exact = (
    Decimal("0.1")
    + Decimal("0.2")
)

print(exact)

# 0.3


# Useful for:
# finance
# money
# precise decimal calculations


# 22. FRACTIONS MODULE

from fractions import Fraction


fraction1 = Fraction(
    1,
    2
)

fraction2 = Fraction(
    1,
    4
)

result = fraction1 + fraction2

print(result)

# 3/4


print(float(result))

# 0.75


# 23. CALENDAR MODULE

import calendar


# Check leap year:

print(
    calendar.isleap(
        2024
    )
)

# True


# Number of leap years:

print(
    calendar.leapdays(
        2000,
        2030
    )
)


# Display month:

print(
    calendar.month(
        2026,
        9
    )
)


# Display full year:

# print(
#     calendar.calendar(
#         2026
#     )
# )


# Weekday:

weekday = calendar.weekday(
    2026,
    9,
    4
)

print(weekday)


# 0 = Monday
# 1 = Tuesday
# 2 = Wednesday
# 3 = Thursday
# 4 = Friday
# 5 = Saturday
# 6 = Sunday


# 24. CSV MODULE

import csv


# CSV means:
# Comma-Separated Values


# Writing CSV:

# students = [
#     ["Name", "Age"],
#     ["Alice", 20],
#     ["Bob", 21]
# ]

# with open(
#     "students.csv",
#     "w",
#     newline=""
# ) as file:
#     writer = csv.writer(file)

#     writer.writerows(students)


# Reading CSV:

# with open(
#     "students.csv",
#     "r"
# ) as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# Dictionary CSV:

# with open(
#     "students.csv",
#     "r"
# ) as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)


# 25. SHUTIL MODULE

import shutil


# Used for higher-level file operations.


# Copy file:

# shutil.copy(
#     "source.txt",
#     "copy.txt"
# )


# Copy file with metadata:

# shutil.copy2(
#     "source.txt",
#     "copy.txt"
# )


# Move file:

# shutil.move(
#     "source.txt",
#     "folder/source.txt"
# )


# Copy complete folder:

# shutil.copytree(
#     "folder1",
#     "folder2"
# )


# Delete complete folder:

# shutil.rmtree(
#     "folder_name"
# )


# Be careful with rmtree().
# It deletes everything inside the folder.


# 26. UUID MODULE

import uuid


# UUID creates unique identifiers.

identifier = uuid.uuid4()

print(identifier)


print(type(identifier))


# Convert to string:

identifier = str(
    uuid.uuid4()
)

print(identifier)


# 27. HASHLIB MODULE

import hashlib


text = "Hello Python"

encoded = text.encode()


result = hashlib.sha256(
    encoded
)

print(
    result.hexdigest()
)


# Common algorithms:

# hashlib.md5()
# hashlib.sha1()
# hashlib.sha256()
# hashlib.sha512()


# Do not use MD5 or SHA1
# for modern password security.


# 28. BASE64 MODULE

import base64


text = "Hello Python"

encoded = base64.b64encode(
    text.encode()
)

print(encoded)


decoded = base64.b64decode(
    encoded
)

print(
    decoded.decode()
)


# Base64 is encoding,
# not encryption.


# 29. COPY MODULE

import copy


# Shallow copy:

original = [
    [1, 2],
    [3, 4]
]

shallow = copy.copy(
    original
)


# Deep copy:

deep = copy.deepcopy(
    original
)


deep[0][0] = 100

print(original)

print(deep)


# deepcopy() creates independent
# nested objects.


# 30. PICKLE MODULE

import pickle


# pickle converts Python objects
# into binary format.


student = {
    "name": "Alice",
    "age": 20
}


# Saving:

# with open(
#     "student.pkl",
#     "wb"
# ) as file:
#     pickle.dump(
#         student,
#         file
#     )


# Loading:

# with open(
#     "student.pkl",
#     "rb"
# ) as file:
#     student = pickle.load(file)


# IMPORTANT:
# Never unpickle untrusted files.


# 31. ENUM MODULE

from enum import Enum


class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


print(Direction.NORTH)

print(Direction.NORTH.name)

print(Direction.NORTH.value)


# Enum is useful for fixed named values.


# 32. DATACLASSES MODULE

from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    course: str


student = Student(
    name="Alice",
    age=20,
    course="CSE"
)

print(student)


# dataclass automatically creates
# useful class methods such as __init__().


# You can learn this properly
# when you study OOP.


# 33. TYPING MODULE

from typing import Optional


def find_user(
    name: str
) -> Optional[str]:
    if name == "Alice":
        return name

    return None


print(
    find_user(
        "Alice"
    )
)


# typing helps with type hints.


# Modern Python also supports:

numbers: list[int] = [
    1,
    2,
    3
]

student: dict[str, str] = {
    "name": "Alice"
}


# 34. IMPORTANT MODULE SUMMARY

# math
# Mathematical calculations.

# random
# Random numbers and selections.

# secrets
# Secure random values.

# json
# JSON data.

# datetime
# Dates and times.

# time
# Time and delays.

# statistics
# Mean, median, mode, standard deviation.

# string
# Character constants.

# os
# Operating system interaction.

# sys
# Python interpreter information.

# pathlib
# File and folder paths.

# re
# Regular expressions.

# collections
# Special collection types.

# itertools
# Tools for iterables.

# functools
# Tools for functions.

# operator
# Operators as functions.

# decimal
# Precise decimal calculations.

# fractions
# Fraction calculations.

# calendar
# Calendar utilities.

# csv
# CSV files.

# shutil
# File and directory operations.

# uuid
# Unique IDs.

# hashlib
# Hashing.

# base64
# Encoding and decoding.

# copy
# Shallow and deep copying.

# pickle
# Saving Python objects in binary form.

# enum
# Fixed named values.

# dataclasses
# Easier data classes.

# typing
# Type hints.


# 35. MODULES YOU SHOULD LEARN FIRST

# As a beginner, focus mainly on:

# math
# random
# json
# datetime
# time
# os
# sys
# statistics
# pathlib
# re


# Then learn:

# collections
# itertools
# functools
# decimal
# csv
# secrets


# You do NOT need to memorize every function.

# Learn:
# what the module is used for
# how to import it
# the most common functions
# how to read documentation when needed


# END OF PYTHON STANDARD LIBRARY NOTES