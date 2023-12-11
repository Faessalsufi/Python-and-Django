point = () #? empty tuple
point = (1,) #? single value tuple
point = (1,2) #? normal tuple

point = tuple([1,2,3])
print(point[0])
print(point[0:2])

x,y,z = point

if 10 in point:
    print("exists")

#! We cam't change the values of tuples