class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

a = Person ("Aravind", 36)

print(a.name)
print(a.age)



class Dog:
 
    def __init__(self, breed):
        self.breed = breed
 
    def bark(self):
        print(f'{self.breed} is barking.')
 
 
d = Dog('Labrador')
d.bark()
