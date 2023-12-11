items = [
    ("product1",6),
    ("product2",12),
    ("product3",3)
]

# Dirty code
# def sort_items(item):
#     return item[1]

items.sort(key=lambda item:item[1])
print(items)
# key=lambda parameters:expression