#1
temperature = 25

if temperature > 30:
    print("its very hot")
        
elif temperature > 25:
    print("its hot")
    
else:
    print("its not hot")
    
    
#2
has_ticket = True
age = 18

if has_ticket:
    if age>=18:
        print("enjoy the movie")
    else:
        print("needs supervision")
        
else:
    print("please buy a ticket")
    
    
    
 
 
 
"""
PYTHON CONTROL FLOW

Control flow decides which parts of a program should run.

Main control flow statements in Python:
1. if
2. if-else
3. if-elif-else
4. nested if
"""


# 1. IF STATEMENT

# Runs only when the condition is True.

age = 20

if age >= 18:
    print("You are an adult")


# 2. IF-ELSE

# if runs when the condition is True.
# else runs when the condition is False.

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 3. IF-ELIF-ELSE

# Used when there are multiple conditions.

marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

else:
    print("Grade C")


# 4. COMPARISON OPERATORS IN CONDITIONS

x = 10

if x == 10:
    print("x is equal to 10")

if x != 5:
    print("x is not equal to 5")

if x > 5:
    print("x is greater than 5")

if x < 20:
    print("x is less than 20")


# 5. LOGICAL OPERATORS IN CONDITIONS

age = 20
has_id = True

# and -> both conditions must be True
if age >= 18 and has_id:
    print("Entry allowed")


# or -> at least one condition must be True
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")


# not -> reverses the condition
is_raining = False

if not is_raining:
    print("You can go outside")


# 6. NESTED IF

# An if statement inside another if statement.

age = 20
has_license = True

if age >= 18:

    if has_license:
        print("You can drive")

    else:
        print("You need a license")

else:
    print("You are too young to drive")


# 7. CHECKING MULTIPLE VALUES

number = 10

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")


# 8. EVEN OR ODD

number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 9. CHECK VALUE IN A LIST

languages = ["Python", "Java", "C++"]

if "Python" in languages:
    print("Python is in the list")


# 10. SHORT-HAND IF

age = 20

if age >= 18: print("Adult")


# 11. TERNARY OPERATOR

# Short form of if-else.

age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)


# 12. PASS IN IF STATEMENT

# pass is used when you want to leave
# a block empty temporarily.

age = 20

if age >= 18:
    pass


# QUICK SUMMARY

# if            -> check a condition
# else          -> run when if condition is False
# elif          -> check another condition
# nested if     -> if inside another if
# and           -> both conditions must be True
# or            -> at least one condition must be True
# not           -> reverses True/False
# pass          -> placeholder, does nothing   

    
  