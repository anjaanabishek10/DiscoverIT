
a=10
b=20
c=30
if (a>=b and a>=c):
 print("a is small")
elif (b>=a and b>=c):
 print("b is small")
elif (c>=a and c>=b):
 print("c is small")
else:
 print("all are big")

bike=10
petrol=5
while(petrol==5):
    if (bike!=0):
        print("ride")
        bike=bike-1
    else:
        break

small=["a","b","c","l","m","g","u","s","r"]
capital=["A","B","C","L","M","G","U","S","R"]
din="balaguru"
for i in din:
    a=small.index(i)
    print(capital[a])