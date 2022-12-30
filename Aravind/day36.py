#left triangle
n=5
for i in range(1,6):
    text=i * '*'
    print(text.ljust(n))
    
#right triangle
n=5
for i in range(1,6):
    text=i * '*'
    print(text.rjust(n)) 
    
#right reversed triangle
for i in reversed(range(1,6)):
    text=i * '*'
    print(text.rjust(n)) 
    
#left reversed triangle
n=5
for i in reversed(range(1,6)):
    text=i * '*'
    print(text.ljust(n)) 
    
#full triangle 
n=5
for i in range(1,6):
    text=i * '* '
    print(text.center(2*n)) 
    
#reversed full triangle
n=5
for i in reversed(range(1,6)):
    text=i * '* '
    print(text.center(2*n))
    
#number triangle 
n=5
for i in range(1,6):
    text=i * '{} '.format(i)
    print(text.center(2*n))  
    
#reversed number triangle
n=5
for i in reversed(range(1,6)):
    text=i * '{} '.format(i)
    print(text.center(2*n)) 
    
#alpabetic full triangle
alpa=['Y','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=5
for i in range(1,6):
    text=i * '{} '.format(alpa[i])
    print(text.center(2*n))                            