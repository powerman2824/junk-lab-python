x = 0
z = []
y = ''

while x > -1:
    x = int(input())
    if x > -1:
        z.append(x)
print(f'{min(z)} and {max(z)}')

