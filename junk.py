word = 'pissword'
password = []

for x in word:
    if ord(x) == 105:
        password.append('1')
    elif ord(x) == 97:
        password.append('@')
    elif ord(x) == 109:
        password.append('M')
    elif ord(x) == 66:
        password.append('8')
    elif ord(x) == 115:
        password.append('$')
    else:
        password.append(x)
password.append('!')
print(''.join(str(x) for x in password))