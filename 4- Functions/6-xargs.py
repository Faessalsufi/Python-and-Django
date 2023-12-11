# def multiply(x,y):
#     return x * y


# multiply(2,4)


def multi(*num):
    total = 1 
    for n in num:
        total *= n
    return total

print(multi(2,3,4,5))