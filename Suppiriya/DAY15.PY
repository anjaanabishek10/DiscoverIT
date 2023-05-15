class grandpa():
    bal1 = 100000
class father(grandpa):
    bal2 = 1000
class son(father,grandpa):
    bal3 = 100
class son2(father,grandpa):
    bal4 = 10
g = grandpa()
f = father()
s = son()
s2 = son2()
print(g.bal1,f.bal1,f.bal2,s.bal1,s.bal2,s.bal3,s2.bal1,s2.bal2,s2.bal4)
