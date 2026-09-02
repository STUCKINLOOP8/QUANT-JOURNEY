"""
PYTHON LOOPS

Loops are used to repeat a block of code multiple times.

Main types of loops in Python:
1. for loop
2. while loop

Useful loop statements:
- break
- continue
- pass
"""


# 1. FOR LOOP

# Used to iterate over a sequence.

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# 2. RANGE()

# range(stop)
for i in range(5):
    print(i)

# range(start, stop)
for i in range(2, 6):
    print(i)

# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)


# 3. LOOP THROUGH A LIST

languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)


# 4. LOOP THROUGH A STRING

name = "Python"

for char in name:
    print(char)


# 5. WHILE LOOP

# Repeats while a condition is True.

count = 1

while count <= 5:
    print(count)
    count += 1


# 6. BREAK

# break immediately stops the loop.

for i in range(10):
    if i == 5:
        break

    print(i)


# 7. CONTINUE

# continue skips the current iteration
# and moves to the next one.

for i in range(5):
    if i == 2:
        continue

    print(i)


# 8. PASS

# pass does nothing.
# It is used as a placeholder.

for i in range(5):
    if i == 2:
        pass

    print(i)


# 9. NESTED LOOP

# A loop inside another loop.

for i in range(3):
    for j in range(2):
        print(i, j)


# 10. FOR LOOP WITH INDEX

languages = ["Python", "Java", "C++"]

for i in range(len(languages)):
    print(i, languages[i])


# Better Python way: enumerate()

for index, language in enumerate(languages):
    print(index, language)


# 11. LOOP THROUGH DICTIONARY

student = {
    "name": "Ansh",
    "course": "B.Tech",
    "year": 2
}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Keys + Values
for key, value in student.items():
    print(key, value)


# 12. ELSE WITH LOOP

# else runs when the loop finishes normally.
# It does NOT run if the loop stops using break.

for i in range(3):
    print(i)
else:
    print("Loop completed")


# QUICK SUMMARY

# for       -> repeat over a sequence
# while     -> repeat while condition is True
# break     -> stop the loop completely
# continue  -> skip current iteration
# pass      -> do nothing / placeholder
# range()   -> generate sequence of numbers
# enumerate() -> get index and value together