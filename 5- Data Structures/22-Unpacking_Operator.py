num = [1, 2, 3]
print(num)
print(*num)  # without [] and ,

values = [*range(5), * "hello"]

first = [1, 2]
second = [3]
values = [*first, *second]
print(values)


first = {"x": 1}
second = {"x": 6, "y": 2}

values = {**first, **second, "z": 1}
print(values)

# to takeout the individual values in any iterable unpacking is used
