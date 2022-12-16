x=lambda a,b:a*b
print(x(3,5))
c=lambda a,b,c:(a+b-c)
print(c(3,5,6))
def aravi(h):
    return lambda b:b%h
x=aravi(9)
print(x(8))    
def name():
    for i in range(10):
        print(i)        
name()        