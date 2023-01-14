try:
  print(x)
except ArithmeticError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
 
 
y=49
try:
  print(x)
except:
  print("An exception occurred")
   