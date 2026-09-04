#Find the sum of digits of a number.
#Example: 472 → 13

num = (input("enter the number:"))
total = 0
for digit in num:
    total =  total + int(digit)
print(total)
  
   