x = int(input())
y = 0
a = []
c = []

while y != x:
    z = int(input())
    y = y + 1
    c.append(z)
        
b = int(input())

d = []
for i in c:
    if i <= b:
        d.append(i)
print(','.join(str(i) for i in d), end=',')
