num = 0
my_list = []
list_len = int(input())

while num != list_len:
    num = num + 1
    user_input = int(input())
    my_list.append(user_input)

def is_list_even(my_list):
    is_even = False
    even_list = []
    for x in my_list:
        if x % 2 == 0:
            even_list.append(x)
    if len(even_list) == list_len:
        is_even = True
    return is_even

def is_list_odd(my_list):
    is_odd = False
    odd_list = []
    for x in my_list:
        if x % 2 == 1:
            odd_list.append(x)
    if len(odd_list) == list_len:
        is_odd = True
    return is_odd

is_list_even(my_list)
is_list_odd(my_list)

if is_list_even(my_list) == False and is_list_odd(my_list) == False:
    print('not even or odd')
elif is_list_even(my_list) == True:
    print('all even')
elif is_list_odd(my_list) == True:
    print('all odd')
