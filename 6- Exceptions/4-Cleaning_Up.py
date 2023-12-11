try:
    file = open("app.py")
    age = int(input("age: "))
    xfactor = 10 / age 
#! we can't close the file here because if any exception are thrown on line 3 or 4 then next line of code won't be execute 

except (ValueError,ZeroDivisionError)  :
    print("Please enter a valid age")
else:
    print("No exception thrown")
finally:
    file.close() #? That's why we"re using finally clause it will always execute weather exception are thrown or not