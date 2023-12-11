try:
    age = int(input("age: "))
except ValueError as ex :
    print("Please enter a valid age")
    # print(ex)
    # print(type(ex))
else:
    print("No exception thrown")

print("execution continue")