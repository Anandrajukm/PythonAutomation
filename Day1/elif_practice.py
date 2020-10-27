marks = int(input("Please enter your marks: "))
if marks < 25:
    print("Your result is fail")
elif marks >=35 and marks <=55:
    print("You are pass:")
elif marks > 65 and marks <=75:
    print("You are first calss")
elif marks >75 and marks <=100:
    print("You are disti8ction")

else:
    print("Please enter valid markes")