from timeit import timeit
#! Raise exception if you really have to it comes with a cost (time) 

code1 = """
def calculate_xfactor(age):
    if age<= 0 :
        raise ValueError ("age cannot be zero or less")
    return 10/age

try:
    calculate_xfactor(-3)
except ValueError as error:
    pass  
"""


#imp Try to solve the exception without raising it 
code2 = """
def calculate_xfactor(age):
    if age<= 0 :
        return None
    return 10/age


xfactor= calculate_xfactor(-3)
if xfactor == None:
    pass
"""

print("first code: ",timeit(code1,number=10000)) #* Slow because we raised an exception
print("second code: ",timeit(code2,number=10000)) #* 4 Times faster than code1