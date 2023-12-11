def calculate_xfactor(age):
    if age<= 0 :
        raise ValueError ("age cannot be zero or less")
    return 10/age

try:
    calculate_xfactor(-3)
except ValueError as error:
    print(error)