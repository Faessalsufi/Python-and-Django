try:
    age = int(input("age: "))
    xfactor = 10 / age 
except (ValueError,ZeroDivisionError)  :#* we can declare multiple errors 
    print("Please enter a valid age")

#! code repeat   
#! if one of the expect clause matches then it will not repeat the other exception code for the same error
# except ZeroDivisionError:
#     print("Please enter a valid age")
else:
    print("No exception thrown")