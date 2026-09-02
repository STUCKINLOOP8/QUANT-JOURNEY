#Take a string and print its length.
#Take a string and print it in uppercase and lowercase.
#Count how many times a given character appears in a string.


strg = input("enter the string:")
print(len(strg))

strg = strg.upper()
print(strg)

strg = strg.lower()
print(strg)


character = input("enter the character you want to look for:")
num = strg.count(character)
print(num)

#without the use of built-in function
count = 0
for char in strg:
   if char == character:
      count=count+1
   
print(count)