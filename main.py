# this code prints out the grade of a person
"""
score = input('Enter your score: ')
student_score = float(score)

if student_score > 100:
    print('Error')
elif student_score >= 90:
    print('Congratulations! Your grade is A')
    print('Keep it up!')
elif student_score >= 75:
    print('Excellent! Your grade is B')
    print('Push harder!')
elif student_score >= 65:
    print('Good! Your grade is C')
    print('You can improve!')
elif student_score >= 55:
    print('Credit! Your grade is D')
    print('Step up!')
else:
    print('Poor! Your grade is F')
    print('You failed!')
"""

while True:
    Password = input("Please enter your password: ")
    password = len(Password)
    if password >= 8:
        print("You have successfully logged in!")
        break
    elif password <= 8:
        print("Invalid password")
        continue


# print(password)


def computegrade(score):
    while True:

        try:

            if score >= 1:
                return "Invalid score"
            elif score >= 0.9:
                return "Congratulations! Your grade is A"
            elif score >= 0.8:
                return "Excellent! Your grade is B"
            elif score >= 0.7:
                return "Good! Your grade is C"
            elif score >= 0.6:
                return "Credit! Your grade is D"
            else:
                return "Poor! Your garde is F"
        except:
            print("Invalid Input")
            break


marks = input("Enter your score: ")
score = float(marks)
Grade = computegrade(score)
print(Grade)
