numbers = [3,30,6,42,24,60]

# numbers.sort(reverse=True)
# print(sorted(numbers,reverse=True))
# print(numbers)

items = [
    ("product1",6),
    ("product2",12),
    ("product3",3)
]

def sort_items(item):
    return item[1]


items.sort(key=sort_items)
print(items)