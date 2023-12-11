items = [
    ("product1",6),
    ("product2",12),
    ("product3",3)
]

#todo prices= list(map(lambda item:item[1],items))
prices = [item[1] for item in items]
# [expression item in items]

#todo filtered =list(filter(lambda item:item[1]>=6,items))
filtered = [item for item in items if item[1]>=6]
print(filtered)
# [expression item in items]
