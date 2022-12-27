#fibinocci series
n=10
a=[2,3]
while(True):
  if (sum(a[-1:-3:-1]) > n):
     break
  a.append(sum(a[-1:-3:-1]))
print(a)

#factorial series
n=3
ans=n
while(n>1):
   n=n-1
   ans=ans*n
print(ans)
