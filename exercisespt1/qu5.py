#Take three numbers and print the largest.

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 > num2 and num1 > num3:
   print("The largest number is :" , num1)
elif num2 > num3 and num2 > num3:
   print("The largest number is :" , num2)
else:
   print("The largest number is :" , num3)