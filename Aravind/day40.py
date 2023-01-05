from functools import reduce
 
def do_sum(x1, x2): 
    return x1 + x2

print(reduce(do_sum, [1, 2, 3, 4]))

from functools import reduce
def sumTwo(a,b):
    return a+b
result = reduce(sumTwo, ['a','r','a','v','i'])
print(result)