# WAP to veerify if it is raining or not 

answer = input("Is it Raining?? Enter Yes or No : ")

if answer == "yes":
    print("Bring your umbrella")
elif answer == "no":
    print("No need of umbrella")
else:
    print("Enter valid Answer")


#WAP to verify if the user is eligible to vote

age = int(input("Enter your age : "))

if age >= 18 :
    print("You are eligible to vote")
elif age <= 18:
    print("Grow up")
else:
    print("Enter valid age ")

# WAP to Score a student 

score = int(input("Enter your Score : "))

if score <= 100 and score >= 90:
    print("Grade A+")
elif score < 90 and score >= 80:
    print("Grade A")
elif score < 80 and score >= 70:
    print("Grade B+")
elif score < 70 and score >= 60:
    print("Grade B")
else:
    ("You Failed")


#WAP to Check the attendance and assingments to mark there in report card

assign  = input("Is your assignment completed:")
att =  int(input("Enter your Attendance"))

if assign == "yes" and att >= 70 :
    print("You can give the exam")
elif assign == "no" and att >= 70:
    print("Submit your assignment first")
elif assign == "yes" and att <= 70 :
    print("your attendance is not completed")
else:
    print("Enter valid answers")

