# Making the 1st array
a=[]
n=int(input("Number of elements in array:\n"))
print("Enter the elements of the First array")
for i in range(0,n):
   l=int(input())
   a.append(l)
# Making the 2nd array
b=[]
#n=int(input("Number of elements in array:\n"))
print(("Enter the elements of the Second array\n"))
for i in range(0,n):
    l=int(input())
    b.append(l)
 
print("The Array's are\n")
print(a)
print(b)

if a==b:
 print("\nTrue\n")
else:
 print("\nFalse\n")

