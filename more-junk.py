z = -15
y = 10

x = range(z, y + 1, 5)

if z > y:
    print("Second integer can't be less than the first.")
else:
    for i in x:
        print(i, end=' ')
    print()