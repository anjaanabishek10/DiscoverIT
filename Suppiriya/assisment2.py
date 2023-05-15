marks = int(input())
if(marks >= 90):
    print("O")  
elif(marks >= 80):
    print("A+")
elif(marks >= 70):       
    print("A")
elif(marks >= 60):
    print("B+")
elif(marks >= 50):
    print("B")
elif(marks < 0):
    print("negative number should not taken")
elif(marks > 100):
    print("mark should not be greater than 100")    
else:
    print("fail")               
                    