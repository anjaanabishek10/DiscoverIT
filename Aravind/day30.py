class Animal:  
    def speak(self):  
        print("Animal Speaking")   
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()
a=Animal()  
d.bark()  
d.speak()
a.speak()  