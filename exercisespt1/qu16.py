#to check if the value is palindrome or not.

value = input("Enter the value:")
if value == value[::-1]:
  print("true")
else:
  print("false")
  
  
#mistake: done use for loophere , and you cannot put string under the range().
  
