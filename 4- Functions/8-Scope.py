message = "a"

def greet(name):
    message = "b"

greet("John")
print(message) # the value of message will be "a"



# in this case message and name are local variables we can't use them outside the function

# we can have same name parameter and variable as above in different function