letters = [ "a", "b","c"]

# Add
letters.append("d")
letters.insert(0,"_")

# Remove

letters.pop(0)
letters.remove("b") # It will delete first occurrence of the "b"
del letters[0:1]
letters.clear()
print(letters)