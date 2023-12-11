num = [1,2,3]

first, second, third = num

# if we have more values in list but need  only few to assign variable we can do something like this
n= [1,2,3,4,5,6]

first , second , *other = n
# print(first,other)

first, *other, last = n

print(first,last)


