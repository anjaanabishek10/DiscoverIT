def sum(a,b):
    sum=a+b
    return sum
print(sum(25,45))


list=[]
n=int(input("Enter the number of element in the list "))
for i in range(n):
    list.append(int(input()))
value=int(input("Enter the value to be searched "))
lb=0
ub=n
while(lb<=ub):
    mid=(lb+ub)//2
    if list[mid]==value:
        print("Value is present in list ")
        break
    elif list[mid]>value:
        ub=mid-1
    elif list[mid]<value:
        lb=mid+1