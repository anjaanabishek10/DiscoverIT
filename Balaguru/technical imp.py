#reverse string
a="balaguru"
print(a[::-1])

#pallindrome
a="appa"
if(a==a[::-1]):
 print("yes")
else:
 print("no")

#no of given char in string
a="aravind"
print(a.count("a"))

a="aravind"
for i in set(a):
 print(i,a.count(i))

#sub string count
a="balaguruguru"
print(a.count("guru"))

#vowels and constant(count,separate)
vow=["a","e","i","o","u"]
a="balagurusee"
a_v=[]
a_c=[]
for i in a:
    if(i in vow):
        a_v.append(i)
    else:
        a_c.append(i)
print(a_v,a_c)

#vowels count
vow=["a","e","i","o","u"]
a="balagurusee"
a_v=[]
a_c=[]
for i in a:
    if(i in vow):
        a_v.append(i)
    else:
        a_c.append(i)
print(len(a_v))

#char is vow or not
a="b"
print("yes")if(a in vow)else print('no')

#rev string
a,b=10,20
a,b=b,a
print(a,b)

a,b=1,2
a=a+b
b=a-b
a=a-b
print(a,b)

