numbers = [1,1,2,3,4]
first = set(numbers)
second = {1,5}

print(first | second) # union
print(first & second) # intersection
print(first - second) # difference 
print(first ^ second) # Semantic difference
#! Set is an unordered collection of unique item we can't have duplicates and we can't access them using index

#? print(first[0])   Error