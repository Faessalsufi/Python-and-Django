items = [
    ("product1",6),
    ("product2",12),
    ("product3",3)
]

prices = []

# for item in items:
#     prices.append(item[1])
# print(prices)

prices= list(map(lambda item:item[1],items))
print(prices)