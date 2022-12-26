n=8
ans=n
while(n>1):
    n=n-1
    ans=ans*n
print(ans)    

# vowels and consonant 
vow=['a','e','i','o','u']
a='suppiriya'
a_v=[]
a_c=[]
for i in a:
    if(i in vow):
        a_v.append(i)
    else:
        a_c.append(i)
print(a_v,a_c)
print(set(a_v),set(a_c))

# swapcase
a,b=23,45
a=a+b
b=a-b
a=a-b
print(a,b) 


#reverse string
a=['a','r','a','v','i','n','d']
print(a[::-1])

#palindrome
a='appa'
if(a==a[::-1]):
    print('yes')
else:
    print('no')               