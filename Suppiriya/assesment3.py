def add(a,c):
    return a+c
def sub(a,c):
    return a-c 
def div(a,c):
    return a/c
def mul(a,c):
    return a*c
choice = input("Enter your operator:")
a = int(input("Enter your first operator:"))
c = int(input("Enter your second operator:"))
if (choice == "+"):
    print("The addition of the given number is :" , (add(a,c)))
elif (choice == "-"):
    print("The subraction of the given number is :" , (sub(a,c)))
elif (choice == "*"):
    print("The multiplication of the given number is :" , (mul(a,c)))
elif (choice == "/"):
    print("The division of the given number is :" , (div(a,c)))
else:
    print("please enter the correct choice:")