name = "Sambhav"
string = f"hi my name is {name}!"  #f string
print(string)


name = name.lower()
print(name)
name = name.upper()
print (name)


sentence = "this is a sentence"
sentence = sentence.title()  #capitalizes the first letter of each word in the string
print(sentence)


#notes

"""
PYTHON STRING MANIPULATION

Strings are sequences of characters used to store text.

Example:
name = "Python"

Strings are:
- Ordered
- Indexed
- Immutable
"""


# 1. CREATING STRINGS

name = "Python"
message = 'Hello World'

print(name)
print(message)


# 2. STRING INDEXING

# Indexing starts from 0.

word = "Python"

print(word[0])   # P
print(word[1])   # y
print(word[-1])  # n


# 3. STRING SLICING

# Syntax:
# string[start:end]

word = "Python"

print(word[0:3])   # Pyt
print(word[2:6])   # thon
print(word[:4])    # Pyth
print(word[2:])    # thon
print(word[::-1])  # nohtyP


# 4. STRING LENGTH

text = "Python"

print(len(text))   # 6


# 5. UPPERCASE AND LOWERCASE

text = "Python Programming"

print(text.upper())   # PYTHON PROGRAMMING
print(text.lower())   # python programming


# 6. CAPITALIZE AND TITLE

text = "python programming"

print(text.capitalize())  # Python programming
print(text.title())       # Python Programming


# 7. REMOVE EXTRA SPACES

text = "   Python   "

print(text.strip())   # Removes spaces from both sides
print(text.lstrip())  # Removes spaces from left
print(text.rstrip())  # Removes spaces from right


# 8. REPLACE TEXT

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)


# 9. FIND TEXT

text = "Python Programming"

print(text.find("Python"))        # 0
print(text.find("Programming"))   # 7

# Returns -1 if not found
print(text.find("Java"))          # -1


# 10. CHECK IF TEXT EXISTS

text = "I am learning Python"

print("Python" in text)       # True
print("Java" not in text)     # True


# 11. COUNT CHARACTERS OR WORDS

text = "banana"

print(text.count("a"))   # 3
print(text.count("n"))   # 2


# 12. STARTSWITH AND ENDSWITH

text = "python.py"

print(text.startswith("python"))  # True
print(text.endswith(".py"))       # True


# 13. SPLIT STRING

text = "Python Java C++"

languages = text.split()

print(languages)

# Output:
# ['Python', 'Java', 'C++']


# Split using a specific separator

data = "Ansh,20,BTech"

values = data.split(",")

print(values)


# 14. JOIN STRINGS

languages = ["Python", "Java", "C++"]

result = ", ".join(languages)

print(result)

# Output:
# Python, Java, C++


# 15. STRING CONCATENATION

first_name = "Ansh"
last_name = "Rawat"

full_name = first_name + " " + last_name

print(full_name)


# 16. STRING REPETITION

word = "Hi "

print(word * 3)

# Output:
# Hi Hi Hi


# 17. F-STRINGS

# Recommended way to insert variables into strings.

name = "Ansh"
age = 20

print(f"My name is {name} and I am {age} years old")


# Expressions can also be used inside f-strings.

a = 10
b = 20

print(f"Sum = {a + b}")


# 18. STRING IMMUTABILITY

# Strings cannot be changed directly.

word = "Python"

# This will cause an error:
# word[0] = "J"

# Correct approach:

word = "J" + word[1:]

print(word)


# 19. CHECK STRING CONTENT

text = "Python123"

print(text.isalpha())    # False - contains numbers
print(text.isdigit())    # False - contains letters
print(text.isalnum())    # True
print(text.islower())    # False
print(text.isupper())    # False


# 20. ESCAPE CHARACTERS

# \n -> new line
# \t -> tab
# \" -> double quote
# \' -> single quote
# \\ -> backslash

print("Hello\nWorld")

print("Name:\tAnsh")

print("He said \"Hello\"")


# 21. MULTILINE STRINGS

message = """
Hello,
I am learning Python.
This is a multiline string.
"""

print(message)


# 22. LOOP THROUGH A STRING

word = "Python"

for char in word:
    print(char)


# 23. REVERSE A STRING

word = "Python"

reversed_word = word[::-1]

print(reversed_word)


# 24. PALINDROME CHECK

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# QUICK SUMMARY

# []             -> access character using index
# [start:end]    -> slicing
# len()          -> length of string
# upper()        -> uppercase
# lower()        -> lowercase
# capitalize()   -> capitalize first letter
# title()        -> capitalize each word
# strip()        -> remove extra spaces
# replace()      -> replace text
# find()         -> find position
# count()        -> count occurrences
# split()        -> string to list
# join()         -> list to string
# startswith()   -> check beginning
# endswith()     -> check ending
# in             -> check if value exists
# f""            -> formatted string
# [::-1]         -> reverse string
