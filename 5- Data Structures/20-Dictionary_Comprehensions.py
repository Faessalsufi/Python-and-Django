# values = []
# for x in range(5):
#     values.append(x*2)

# ? They are identical

# values = [x*2 for x in range(5)]
# print(values)


# * Set
# values = {x*2 for x in range(5)}
# print(values)


# * Dictionary
# values = {x: x*2 for x in range(5)}
# print(values)


values = {}
for x in range(5):
    values[x] = x*2


#! Comprehensions don't work with tuples
