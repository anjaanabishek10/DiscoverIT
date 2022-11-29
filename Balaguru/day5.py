a=(1,2,3,4,5,6,7)
a=tuple(a)
print(a)

a=(1,2,3,4,5,6,7)
a=list(a)
a[2]=5
a=tuple(a)
print(a)
a=(1,2,3)
b=(4,5,6)
c=a+b
print(c)

a={1,2,3,4,5,6,5,2}
print(a)

a={1,20,30,55,66}
a.add(11)
print(a)

a={1,2,3,4,5,6}
a.remove(3)
print(a)
b={1:"balaguru",2:"aravind",3:"abi"}
print(b)

a={21:"guru",25:"bala",10:"aravind"}
a[15]="abishek"
print(a)

a={1:"bala",2:"aravind",3:"abi",4:"python"}
print(a.get(1))

