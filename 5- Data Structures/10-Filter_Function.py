items = [
    ("product1",6),
    ("product2",12),
    ("product3",3)
]

filtered =list(
    filter(lambda item:item[1]>=6,items)
    )
print(filtered)