#min and max
a=[5,6,7,4,2,34,86,56]
a.sort()
print(a[0])

print(a[-1])


#remove char in string
a='aravind'
b=a.find('r')
print(a[0:b]+a[b+1:len(a)])
c=a.replace('a','b')
print(c)

#remove char in list
a=[3,4,5,6,6,7,8]
a.remove(6)
print(a)

#sum of arry
arr=[5,76,7,8,23,90]
print(sum(arr))

#odd and even
a=[9,8,7,6,5,4,3,2,1]
a_odd=[]
a_even=[]
for i in a:
    if (i%2==0):
        a_even.append(i)
    else:
        a_odd.append(i)
print(a_even,a_odd)

print(len(a_even),len(a_odd))     

#odd or even
a=4
if(i%2==0):
    print('even')
else:
    print('odd')           