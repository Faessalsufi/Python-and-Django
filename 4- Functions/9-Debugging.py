def multi(*num):
    total = 1 
    for n in num:
        total *= n
    return total
    

print ("start")
print (multi(1,2,3))