a={1:'aravind',2:'balguru',3:'anand'}
a[4]='guru'
b=a.values()
c=a.keys()
print(a)
print(b)
print(c)
print(a[2])
name={1:'aravind',2:'balguru',3:'anand'}
new=list(name)
new.pop(2)
name=dict(new)
print(name)