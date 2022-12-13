z = ''

while z not in ('Done', 'done', 'd'):
    z = input()
    if z in ('Done', 'done', 'd'):
        this = 'nothing'
    else:
        y = -1
        newWord = []
        x = range(len(z) - 1, y, -1)
        for i in x:
            newWord.append(z[i])
        print(''.join(str(i) for i in newWord))