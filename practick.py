operations = ["++X", "++X","X++"]

x = 0

for item in operations:
    if item == '--X' or item == '--X'[::-1]:
        x -= 1
    else:
        x += 1

print(x)