def save_user(**user):
    print(user["name"],user["id"])


save_user(id = 1 , name = "John", age = 24)
# if we use double ** in parameter than we can give values in key value format as an argument