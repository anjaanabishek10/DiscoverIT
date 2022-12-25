class Students:
   def __init__(self, name, rank, points):
      self.name = name
      self.rank = rank
      self.points = points

   def details(self):
      print("I am "+self.name)
      print("I got Rank ",+self.rank)
      print("I got points ",+self.points)
      
st1 = Students("Steve", 1, 100)
st2 = Students("Chris", 2, 90)
st3 = Students("Mark", 3, 76)
st4 = Students("Kate", 4, 60)


st1.details()
st2.details()
st3.details()
st4.details()