import random
import string
# print(random.random())
# print(random.randint(1, 10))
# print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9], k=2))
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

numbers = [1, 4, 5, 6, 8, 2, 4, 1, 5]
random.shuffle(numbers)
# print(numbers)


letters = "".join(random.choices(string.ascii_letters, k=6))

numbers = "".join(random.choices(string.digits, k=3))

symbols = "".join(random.choices("!@#$%^&*()_+=", k=2))

password = letters + numbers + symbols
# random.shuffle(password)
print(password)
