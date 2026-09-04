#Print all even numbers between 1 and n.

n = int(input("Enter n:"))
for i in range(0,n+1):
   even_num=i%2
   if even_num==0:
    print(i)
    
    