from sys import getsizeof

values = [x*2 for x in range(10000)]
print(getsizeof(values))

# for x in values:
#     print(x)

values = (x*2 for x in range(10000))
print(getsizeof(values))
# for x in values: # iteration on gen
#     print(x)
# print(values)


#! we can't access length generator
