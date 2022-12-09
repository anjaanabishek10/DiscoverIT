a=b=[10000000]
print(a is b)
a=b=[2116]
print(a is not b)

a=20
b=20
if(a is b):
    print("same")
else:
    ptint("not same")
a=10
b=30
if(a is b):
    print("same")
else:
    print("not same")

if(a is not b):
    print("not same")