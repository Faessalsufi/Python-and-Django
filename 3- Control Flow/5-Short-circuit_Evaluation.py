high_income = False
good_credit = True
student = False

if high_income and good_credit and not student:
    print("eligible")

# If we are using logical operator and between two variables in this case if the high income get false then it will not check the good credit and the student because it knows if high income is fault and it doesn't matter what comes after that is why python is a short circuit evaluation