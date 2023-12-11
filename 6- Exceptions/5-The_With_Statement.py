try:
    with open("app.py") as file, open("another.py") as another:
        print("file opened")
        # file.__enter__
        # file.__exit__
    age = int(input("age: "))
    xfactor = 10 / age 
except (ValueError,ZeroDivisionError):
    print("Please enter a valid age")
else:
    print("No exception thrown")
    #! now we don't need to close the file if we are using with statement
# finally:
#     file.close() 