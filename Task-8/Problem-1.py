a=int(input("Begign with number\n"))
b=int(input("End with number\n"))
c=""
d=".  0.  0.  0.  0.  0. "
for i in range(a,b):
    c=c+str(i)+d
print(c + str(b))