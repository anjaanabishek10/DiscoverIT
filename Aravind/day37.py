fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


def num (n) :
    return n * 2
          
lst = [2, 44, 5.5, 6, -7]
x = map(num, lst) 
print(x) 
print(list(x)) 